#!/usr/bin/env python3
"""Hook Write|Edit|MultiEdit: chặn hoặc nhắc từ PM đã cấm, theo bảng ở memory/context/so-tu-cam.md.

Đăng ký hai lần trong .claude/settings.json:
  - PreToolUse: từ mức "chặn" thêm mới thì từ chối ghi (permissionDecision: deny), Claude sửa rồi ghi lại.
  - PostToolUse: từ mức "nhắc" thêm mới thì nhắc qua additionalContext, tệp vẫn được ghi.
Chỉ tính chữ MỚI: đếm từng mẫu ở chữ cũ (old_string, hoặc tệp trên đĩa khi Write) và chữ mới,
chỉ báo khi số lần tăng. Nhờ vậy sửa tệp cũ còn sẵn từ cấm (như CLAUDE.md) vẫn được.
Muốn thêm từ: thêm dòng vào bảng trong so-tu-cam.md, không sửa tệp này.
Lỗi đọc dữ liệu, bảng hay biểu thức hỏng thì cho qua (fail open), để hook hỏng không chặn cả phiên.
Mỗi lần chặn ghi một dòng vào .claude/hook-chan.log (không đưa lên git) để đếm lỗi lặp.
Thử tay:
  echo '{"hook_event_name":"PreToolUse","tool_name":"Edit","tool_input":{"file_path":"a.md","old_string":"","new_string":"đã chốt"}}' | python3 .claude/hooks/chan-tu-cam.py
"""
import datetime
import json
import os
import re
import subprocess
import sys
import unicodedata

KHO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SO_TU_CAM = os.path.join(KHO, "memory", "context", "so-tu-cam.md")
NHAT_KY = os.environ.get("CHAN_TU_CAM_LOG") or os.path.join(KHO, ".claude", "hook-chan.log")

DUOI_CHU = (".md", ".txt", ".html", ".htm", ".js", ".jsx", ".ts", ".tsx", ".py", ".json", ".csv", ".xml")
DUOI_OFFICE = (".py", ".xml")
DUOI_VAN_XUOI = (".md", ".txt")  # chỉ ở văn xuôi mới bỏ qua chữ trong ngoặc kép (trích nguyên văn)

# Tệp ghi chép chính các từ cấm, kho lưu trữ, mã hook và kiểm thử, bộ nhớ tự động của Claude.
BO_QUA = re.compile(
    r"(^|/)(04_Archives|\.claude/hooks|tests)/"
    r"|(^|/)memory/context/(so-tu-cam|so-loi-lap|lich-su-claude-md|mau-bai-hoc)\.md$"
    r"|/\.claude/projects/"
    r"|(^|/)memory/(.*/)?[^/]*(tu[_-]cam|tranh[_-]an[_-]du|khong[_-]dung[_-]tu[_-]chot|khong[_-]dem[_-]so[_-]dau[_-]muc|khong[_-]co[_-]gian[_-]ky[_-]tu)[^/]*\.md$"
)
TRICH = re.compile(r"`[^`\n]*`|\"[^\"\n]*\"|“[^”\n]*”")


def doc_bang():
    """Trả về danh sách (mẫu đã biên dịch, chuỗi mẫu, mức, loại tệp, thay bằng)."""
    bang = []
    with open(SO_TU_CAM, encoding="utf-8") as f:
        for dong in f:
            dong = unicodedata.normalize("NFC", dong.strip())
            if not dong.startswith("|") or dong.startswith("|---") or dong.startswith("| Mẫu"):
                continue
            o = [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", dong.strip("|"))]
            if len(o) < 4 or o[1] not in ("chặn", "nhắc"):
                continue
            try:
                bang.append((re.compile(o[0], re.I | re.M), o[0], o[1], o[2], o[3]))
            except re.error:
                continue
    return bang


def lam_sach(chu, tep):
    chu = unicodedata.normalize("NFC", chu or "")
    ra, trong_khoi = [], False
    van_xuoi = tep.lower().endswith(DUOI_VAN_XUOI)
    for dong in chu.splitlines():
        if van_xuoi and dong.strip().startswith("```"):
            trong_khoi = not trong_khoi
            continue
        if trong_khoi or "nguyen-van" in dong:
            continue
        ra.append(TRICH.sub("", dong) if van_xuoi else dong)
    return "\n".join(ra)


def ban_tren_git(duong):
    """Nội dung tệp ở commit HEAD; tệp chưa có trên git thì trả về chuỗi rỗng."""
    try:
        r = subprocess.run(["git", "-C", os.path.dirname(duong) or ".", "show", "HEAD:./" + os.path.basename(duong)],
                           capture_output=True, timeout=5)
        return r.stdout.decode("utf-8", "replace") if r.returncode == 0 else ""
    except Exception:
        return ""


def cap_cu_moi(ti, tool, tep, su_kien):
    """Các cặp (chữ cũ, chữ mới) cần so."""
    if tool == "Write":
        # Trước khi ghi: chữ cũ là tệp trên đĩa. Sau khi ghi: tệp trên đĩa đã là chữ mới, nên lấy bản trên git.
        cu = ""
        try:
            duong = tep if os.path.isabs(tep) else os.path.join(KHO, tep)
            if su_kien != "PreToolUse":
                cu = ban_tren_git(duong)
            elif os.path.exists(duong):
                with open(duong, encoding="utf-8") as f:
                    cu = f.read()
        except Exception:
            cu = ""
        return [(cu, ti.get("content", ""))]
    if tool == "MultiEdit":
        return [(e.get("old_string", ""), e.get("new_string", "")) for e in ti.get("edits", [])]
    return [(ti.get("old_string", ""), ti.get("new_string", ""))]


def main():
    try:
        d = json.load(sys.stdin)
        su_kien = d.get("hook_event_name", "PreToolUse")
        tool = d.get("tool_name", "")
        ti = d.get("tool_input", {})
        tep = ti.get("file_path", "")
        tep_chuan = unicodedata.normalize("NFC", tep).replace(os.sep, "/")
        duoi = tep_chuan.lower()
        if not tep or BO_QUA.search(tep_chuan) or not duoi.endswith(DUOI_CHU):
            sys.exit(0)
        muc_can = "chặn" if su_kien == "PreToolUse" else "nhắc"
        bang = [b for b in doc_bang() if b[2] == muc_can and
                (b[3] != "office" or duoi.endswith(DUOI_OFFICE))]
        if not bang:
            sys.exit(0)
        cap = [(lam_sach(cu, tep_chuan), lam_sach(moi, tep_chuan)) for cu, moi in cap_cu_moi(ti, tool, tep, su_kien)]
        thay = []
        for mau, chuoi, _, _, thay_bang in bang:
            cu = sum(len(mau.findall(c)) for c, _ in cap)
            moi_ds = [m.group(0) for _, m_chu in cap for m in mau.finditer(m_chu)]
            if len(moi_ds) > cu:
                thay.append(f'"{moi_ds[-1]}" -> {thay_bang}')
    except SystemExit:
        raise
    except Exception:
        sys.exit(0)
    if not thay:
        sys.exit(0)
    ds = "\n".join("- " + t for t in thay[:10])
    if su_kien == "PreToolUse":
        try:
            with open(NHAT_KY, "a", encoding="utf-8") as f:
                for t in thay:
                    f.write(f"{datetime.date.today().isoformat()}\t{t.split(' -> ')[0]}\t{tep_chuan}\n")
        except Exception:
            pass
        ly_do = (f"Không ghi {tep}: có từ PM đã cấm (memory/context/so-tu-cam.md).\n{ds}\n"
                 "Viết lại câu theo nghĩa rồi ghi lại. Nếu là lời người khác nói được trích nguyên văn, "
                 "đặt trong ngoặc kép (tệp .md) hoặc thêm chữ nguyen-van trên dòng đó.")
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
                                                 "permissionDecision": "deny",
                                                 "permissionDecisionReason": ly_do}}, ensure_ascii=False))
    else:
        nhac = (f"Tệp {tep} vừa ghi có từ PM dặn tránh (memory/context/so-tu-cam.md, mức nhắc):\n{ds}\n"
                "Xem lại: nếu đang dùng nghĩa bóng thì sửa, nghĩa thường (mạch máu, phép thử thống kê) thì giữ.")
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse",
                                                 "additionalContext": nhac}}, ensure_ascii=False))
    sys.exit(0)


if __name__ == "__main__":
    main()
