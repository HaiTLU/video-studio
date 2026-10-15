#!/usr/bin/env python3
"""Hook PreToolUse (Write|Edit|MultiEdit|NotebookEdit|Read|Grep): bảo vệ tệp bí mật và kho lưu trữ.

Chặn:
  1. Ghi vào tệp bí mật: .env (trừ .env.example, .env.sample), *.pem, *.key, id_rsa*, id_ed25519*,
     credentials.json, và thư mục JarvisMat (văn bản mật của PM, CLAUDE.md mục Nhật ký phiên).
  2. Sửa tệp ĐÃ CÓ trong 04_Archives/ (CLAUDE.md: PM cần xem lại mọi bản trước). Tạo tệp mới
     trong 04_Archives/ vẫn được; lưu bản cũ vẫn dùng `cp` như quy tắc.

  3. Đọc tệp bí mật bằng công cụ Read hoặc Grep (cùng danh sách ở mục 1). Đọc 04_Archives/ vẫn được.
  4. Ghi vào kho nhớ tự động của Claude Code (~/.claude/projects/*ThangLong-KB*/memory/), trừ MEMORY.md:
     bộ nhớ đã gộp vào memory/ của kho từ 12/10/2026.

Mẫu "bảo vệ tệp bằng PreToolUse" lấy ý từ danh sách awesome-claude-code-hooks (CC0) và ví dụ hook
chính thức của Claude Code; mã viết lại, không chép, không gọi mạng, không cần thư viện ngoài.
Lỗi đọc dữ liệu thì cho qua (fail open), để hook hỏng không chặn nhầm cả phiên.
Thử tay:
  echo '{"tool_input":{"file_path":".env"}}' | python3 .claude/hooks/bao-ve-tep.py
"""
import json
import os
import re
import sys

KHO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BI_MAT = re.compile(
    r"(^|/)(\.env(\.(?!example$|sample$)[^/]+)?|[^/]+\.pem|[^/]+\.key|id_rsa[^/]*|id_ed25519[^/]*|credentials\.json)$"
    r"|(^|/)JarvisMat(/|$)"
)

# Kho nhớ tự động của Claude Code cho kho này (mọi thư mục dự án có tên chứa ThangLong-KB). Chỉ chừa MEMORY.md,
# nơi giữ mục lục ngắn trỏ sang memory/ của kho.
KHO_NHO_CU = re.compile(r"/\.claude/projects/[^/]*ThangLong-KB[^/]*/memory/(?!MEMORY\.md$)[^/]+$")


def tra_loi(ly_do):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": ly_do,
    }}, ensure_ascii=False))
    sys.exit(0)


def main():
    try:
        d = json.load(sys.stdin)
        ti = d.get("tool_input", {})
        doc = d.get("tool_name") in ("Read", "Grep")
        tep = ti.get("file_path") or ti.get("notebook_path") or ti.get("path") or ""
    except Exception:
        sys.exit(0)
    if not tep:
        sys.exit(0)
    tuyet_doi = os.path.abspath(tep if os.path.isabs(tep) else os.path.join(KHO, tep))
    tuong_doi = os.path.relpath(tuyet_doi, KHO).replace(os.sep, "/")

    if BI_MAT.search(tuyet_doi.replace(os.sep, "/")):
        tra_loi("Tệp bí mật (khóa, mật khẩu, .env, JarvisMat) không được " + ("đọc" if doc else "ghi") +
                " qua Claude. Nếu cần, hãy báo PM tự xử lý hoặc dùng biến bí mật của môi trường.")
    if doc:
        sys.exit(0)
    if KHO_NHO_CU.search(tuyet_doi.replace(os.sep, "/")):
        tra_loi("Kho nhớ tự động của Claude Code đã gộp vào memory/ của kho từ 12/10/2026 (PM quyết). "
                "Ghi bài học vào memory/context/bai-hoc/ và thêm một dòng vào mục Bài học của memory/MEMORY.md; "
                "dự án vào memory/projects/, tra cứu vào memory/context/tra-cuu/.")
    if (tuong_doi.startswith("04_Archives/") and os.path.exists(tuyet_doi)):
        tra_loi("Tệp trong 04_Archives/ là bản lưu, không sửa. Hãy chép ra nơi làm việc "
                "(cp) và sửa bản chép, hoặc tạo bản mới với hậu tố _vN.")
    sys.exit(0)


if __name__ == "__main__":
    main()
