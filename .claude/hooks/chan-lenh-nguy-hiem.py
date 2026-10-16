#!/usr/bin/env python3
"""Hook PreToolUse (Bash): chặn lệnh trái quy tắc kho, trước khi lệnh chạy.

Chặn:
  1. Xóa tệp của kho bằng `rm` hoặc `git rm` (CLAUDE.md: "Không xóa tệp", chép bản cũ vào 04_Archives/).
     Cho phép xóa trong thư mục tạm và thư mục sinh ra khi dựng: /tmp, node_modules, .next,
     __pycache__, khung_*, kiem_*, dist, build, .venv. `git rm --cached` cũng được (không xóa tệp).
  2. `git push` vào main (main chỉ nhận thay đổi qua PR) và `git push --force` / `-f`
     (`--force-with-lease` trên nhánh claude/ vẫn được).

  3. Lệnh phá việc chưa commit: `git reset --hard`, `git clean -f`, `git checkout -- .`,
     `git restore .`; và `curl|wget ... | sh|bash` (chạy mã tải về).
  4. Ghi đè qua Bash vào tệp bí mật hoặc tệp ĐÃ CÓ trong 04_Archives/ (mv, cp, sed -i, tee, truncate,
     dd of=, chuyển hướng > >>), cùng quy tắc với bao-ve-tep.py (công cụ Write/Edit).
  5. Đọc tệp bí mật (.env, *.pem, *.key, id_rsa*, credentials.json, JarvisMat) bằng cat, head, tail, grep...

Lỗi đọc dữ liệu thì cho qua (fail open), để hook hỏng không chặn nhầm cả phiên.
Thử tay:
  echo '{"tool_input":{"command":"rm memory/MEMORY.md"}}' | python3 .claude/hooks/chan-lenh-nguy-hiem.py
"""
import json
import os
import re
import shlex
import subprocess
import sys

KHO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CHO_PHEP = re.compile(r"(^|/)(node_modules|\.next|__pycache__|khung_[^/]*|kiem_[^/]*|dist|build|\.venv|\.pytest_cache)(/|$)")

BI_MAT = re.compile(
    r"(^|/)(\.env(\.(?!example$|sample$)[^/]+)?|[^/]+\.pem|[^/]+\.key|id_rsa[^/]*|id_ed25519[^/]*|credentials\.json)$"
    r"|(^|/)JarvisMat(/|$)"
)
LENH_DOC = {"cat", "head", "tail", "less", "more", "bat", "nl", "tac", "grep", "egrep", "rg", "awk",
            "sed", "strings", "xxd", "od", "base64", "source", "."}
MA_NGUON_TAI = re.compile(r"\b(curl|wget)\b[^|;&\n]*\|\s*(sudo\s+)?(ba|z|da)?sh\b")
HEREDOC = re.compile(r"(<<-?\s*(['\"]?)(\w+)\2[^\n]*)\n.*?\n[ \t]*\3[ \t]*(?=\n|$)", re.S)
CHUYEN_HUONG = re.compile(r"(?<![0-9&>\-])>>?\s*([^\s&|;<>()]+)")


def duong_tuyet_doi(d, thu_muc):
    return os.path.normpath(os.path.join(thu_muc, os.path.expanduser(d)))


def xet_ghi(duong, thu_muc):
    """Chặn ghi vào tệp bí mật hoặc tệp đã có trong 04_Archives/."""
    if not duong or duong.startswith("-") or duong in ("/dev/null", "/dev/stderr", "/dev/stdout"):
        return
    p = duong_tuyet_doi(duong, thu_muc)
    if BI_MAT.search(p.replace(os.sep, "/")):
        tra_loi("Tệp bí mật (khóa, mật khẩu, .env, JarvisMat) không được ghi qua Claude. "
                "Nếu cần, hãy báo PM tự sửa hoặc ghi vào biến bí mật của môi trường.")
    rel = os.path.relpath(p, KHO).replace(os.sep, "/")
    if rel.startswith("04_Archives/") and os.path.exists(p) and not os.path.isdir(p):
        tra_loi("Tệp trong 04_Archives/ là bản lưu, không ghi đè. Chép ra nơi làm việc rồi sửa bản chép, "
                "hoặc tạo bản mới với hậu tố _vN.")


def xet_doc(tk, thu_muc):
    """Chặn đọc tệp bí mật bằng lệnh đọc phổ biến."""
    for t in tk[1:]:
        if t.startswith("-"):
            continue
        p = duong_tuyet_doi(t, thu_muc).replace(os.sep, "/")
        if BI_MAT.search(p):
            tra_loi("Tệp bí mật (khóa, mật khẩu, .env, JarvisMat) không được đọc qua Claude. "
                    "Cần giá trị nào thì báo PM nhập vào biến bí mật của môi trường.")


def xet_ghi_theo_lenh(tk, thu_muc):
    """Lệnh ghi hoặc di chuyển tệp: xét các đường dẫn bị ghi đè hoặc bị lấy đi."""
    ten = os.path.basename(tk[0])
    ts = [t for t in tk[1:] if not t.startswith("-")]
    if ten in ("cp", "install", "ln") and len(ts) >= 2:
        dich = ts[-1]
        if os.path.isdir(duong_tuyet_doi(dich, thu_muc)):
            for nguon in ts[:-1]:
                xet_ghi(os.path.join(dich, os.path.basename(nguon.rstrip("/"))), thu_muc)
        else:
            xet_ghi(dich, thu_muc)
    elif ten == "mv" and len(ts) >= 2:
        for nguon in ts[:-1]:
            xet_ghi(nguon, thu_muc)
        dich = ts[-1]
        if os.path.isdir(duong_tuyet_doi(dich, thu_muc)):
            for nguon in ts[:-1]:
                xet_ghi(os.path.join(dich, os.path.basename(nguon.rstrip("/"))), thu_muc)
        else:
            xet_ghi(dich, thu_muc)
    elif ten == "sed" and any(t == "-i" or t.startswith("-i") or t == "--in-place" for t in tk[1:]):
        for t in ts[1:]:
            xet_ghi(t, thu_muc)
    elif ten in ("tee", "truncate", "touch", "shred"):
        for t in ts:
            xet_ghi(t, thu_muc)
    elif ten == "dd":
        for t in tk[1:]:
            if t.startswith("of="):
                xet_ghi(t[3:], thu_muc)


def xet_git_pha_viec(sub, tk):
    co = set(t for t in tk if t.startswith("-"))
    if sub == "reset" and "--hard" in co:
        tra_loi("Quy tắc kho: `git reset --hard` xóa việc chưa commit. Hãy commit hoặc hỏi PM trước.")
    if sub == "clean" and any(re.fullmatch(r"-[a-zA-Z]*f[a-zA-Z]*", c) or c == "--force" for c in co):
        tra_loi("Quy tắc kho: `git clean -f` xóa tệp chưa theo dõi. Hãy hỏi PM trước.")
    if sub == "checkout" and "--" in tk and "." in tk:
        tra_loi("Quy tắc kho: `git checkout -- .` bỏ mọi thay đổi chưa commit. Hãy hỏi PM trước.")
    if sub == "restore" and "." in tk and "--staged" not in co:
        tra_loi("Quy tắc kho: `git restore .` bỏ mọi thay đổi chưa commit. Hãy hỏi PM trước.")


def tra_loi(ly_do):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": ly_do,
    }}, ensure_ascii=False))
    sys.exit(0)


def cac_lenh(chuoi):
    """Tách chuỗi lệnh theo ; && || | xuống dòng, trả về danh sách token của từng lệnh con."""
    for phan in re.split(r"\|\||&&|[;|\n]", chuoi):
        try:
            tk = shlex.split(phan, comments=True)
        except ValueError:
            tk = phan.split()
        # bỏ tiền tố kiểu sudo, env A=B, timeout 10
        while tk and (tk[0] in ("sudo", "env", "command", "nohup") or "=" in tk[0] and not tk[0].startswith("-")):
            tk = tk[1:]
        if tk and tk[0] == "timeout" and len(tk) > 2:
            tk = tk[2:]
        if tk:
            yield tk


def trong_kho(duong, thu_muc):
    if duong.startswith("~"):
        return False
    p = os.path.normpath(os.path.join(thu_muc, duong))
    if p.startswith(("/tmp/", "/var/tmp/")) or p in ("/tmp", "/var/tmp"):
        return False
    return p == KHO or p.startswith(KHO + os.sep)


def xet_rm(tk, thu_muc):
    dich = [t for t in tk[1:] if not t.startswith("-")]
    for d in dich:
        if trong_kho(d, thu_muc) and not CHO_PHEP.search(os.path.relpath(os.path.join(thu_muc, d), KHO)):
            tra_loi(f"Quy tắc kho: không xóa tệp ({d}). Muốn bỏ một tệp thì chép bản cũ vào "
                    "04_Archives/<DuAn>/ bằng cp. "
                    "Tệp tạm thì đặt trong thư mục scratchpad hoặc /tmp.")


def nhanh_hien_tai(thu_muc):
    try:
        return subprocess.run(["git", "-C", thu_muc, "rev-parse", "--abbrev-ref", "HEAD"],
                              capture_output=True, text=True, timeout=5).stdout.strip()
    except Exception:
        return ""


def xet_push(tk, thu_muc):
    co = [t for t in tk if t.startswith("-")]
    if "--force" in co or "-f" in co or any(re.fullmatch(r"-[a-zA-Z]*f[a-zA-Z]*", t) for t in co if not t.startswith("--")):
        tra_loi("Quy tắc kho: không đẩy đè lịch sử bằng `git push --force` / `-f`. "
                "Trên nhánh claude/ của chính phiên này dùng `--force-with-lease` nếu thật cần.")
    doi = [t for t in tk[2:] if not t.startswith("-")]
    refspec = doi[1:] if doi else []
    for r in refspec:
        dich = r.split(":")[-1].lstrip("+")
        if dich in ("main", "refs/heads/main"):
            tra_loi("Quy tắc kho: main chỉ nhận thay đổi qua PR. Đẩy lên nhánh claude/<tên-việc> rồi tạo PR.")
    if not refspec and nhanh_hien_tai(thu_muc) == "main":
        tra_loi("Quy tắc kho: đang ở nhánh main; main chỉ nhận thay đổi qua PR. "
                "Tạo nhánh claude/<tên-việc> từ main rồi đẩy nhánh đó.")


def main():
    try:
        du_lieu = json.load(sys.stdin)
        lenh = du_lieu.get("tool_input", {}).get("command", "")
        thu_muc = du_lieu.get("cwd") or os.getcwd()
    except Exception:
        sys.exit(0)
    lenh = HEREDOC.sub(lambda m: m.group(1), lenh)  # bỏ thân heredoc (lời nhắn commit, tệp mẫu)
    if MA_NGUON_TAI.search(lenh):
        tra_loi("Quy tắc kho: không chạy mã tải từ mạng qua đường ống (`curl ... | sh`). "
                "Tải về tệp trong thư mục tạm, đọc nội dung rồi mới chạy, hoặc hỏi PM.")
    for m in CHUYEN_HUONG.finditer(lenh):
        xet_ghi(m.group(1).strip("\"'"), thu_muc)
    for tk in cac_lenh(lenh):
        if tk[0] == "cd" and len(tk) > 1:
            thu_muc = os.path.normpath(os.path.join(thu_muc, os.path.expanduser(tk[1])))
            continue
        if tk[0] in ("rm", "/bin/rm", "unlink"):
            xet_rm(tk, thu_muc)
        if os.path.basename(tk[0]) in LENH_DOC:
            xet_doc(tk, thu_muc)
        xet_ghi_theo_lenh(tk, thu_muc)
        if tk[0] == "git":
            i, sub = 1, ""
            while i < len(tk):  # lệnh con của git, bỏ qua -C <thư mục>, -c <khóa=giá trị>
                if tk[i] in ("-C", "-c"):
                    if tk[i] == "-C" and i + 1 < len(tk):
                        thu_muc = os.path.normpath(os.path.join(thu_muc, tk[i + 1]))
                    i += 2
                    continue
                if tk[i].startswith("-"):
                    i += 1
                    continue
                sub = tk[i]
                break
            if sub == "rm" and "--cached" not in tk:
                xet_rm(["rm"] + [t for t in tk[tk.index("rm") + 1:]], thu_muc)
            xet_git_pha_viec(sub, tk)
            if sub == "push":
                xet_push(tk[tk.index("push") - 1:], thu_muc)
    sys.exit(0)


if __name__ == "__main__":
    main()
