#!/usr/bin/env python3
"""Hook PostToolUse (Write|Edit): soát gạch dài và biểu tượng trong phần chữ vừa viết vào tệp .md.

Theo quy tắc 5 và 6 trong CLAUDE.md (chỉ gạch ngắn "-", không emoji hay biểu tượng trong DOCX, MD).
Chỉ nhắc Claude tự sửa, không chặn. Chỉ xét phần chữ mới (content của Write, new_string của Edit),
nên chữ cũ có sẵn trong tệp không bị nhắc. Bỏ qua 04_Archives/, kỹ năng humanizer và impeccable
(tài liệu gốc tiếng Anh) và mọi tệp không phải .md.
Thử tay:
  echo '{"tool_name":"Edit","tool_input":{"file_path":"a.md","new_string":"x — y ✅"}}' | python3 .claude/hooks/soat-chu.py
"""
import json
import re
import sys

BO_QUA = re.compile(r"(^|/)(04_Archives|\.claude/skills/(humanizer|impeccable|diagram-design|security-audit|playwright-cli))/")
GACH_DAI = re.compile("[\u2014\u2013]")
BIEU_TUONG = re.compile("[\u2190-\u21ff\u2600-\u27bf\u2b00-\u2bff\U0001f000-\U0001faff\u2794]")
TRONG_MA = re.compile(r"`[^`\n]*`")  # chữ trong dấu ` ` (ví dụ quy tắc liệt kê ký tự cấm) thì bỏ qua


def main():
    try:
        d = json.load(sys.stdin)
        ti = d.get("tool_input", {})
        tep = ti.get("file_path", "")
        chu = ti.get("content") if "content" in ti else ti.get("new_string", "")
    except Exception:
        sys.exit(0)
    if not tep.endswith(".md") or BO_QUA.search(tep) or not chu:
        sys.exit(0)
    loi = []
    trong_khoi_ma = False
    for so, dong in enumerate(chu.splitlines(), 1):
        if dong.strip().startswith("```"):
            trong_khoi_ma = not trong_khoi_ma
            continue
        if trong_khoi_ma:
            continue
        sach = TRONG_MA.sub("", dong)
        thay = GACH_DAI.findall(sach) + BIEU_TUONG.findall(sach)
        if thay:
            loi.append(f"dòng {so} của phần vừa viết: {' '.join(sorted(set(thay)))} | {dong.strip()[:80]}")
    if not loi:
        sys.exit(0)
    nhac = (f"Tệp {tep} vừa ghi có gạch dài hoặc biểu tượng, trái quy tắc 5-6 của CLAUDE.md "
            "(chỉ dùng gạch ngắn '-', không emoji). Sửa lại:\n" + "\n".join(loi[:8]))
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": nhac}},
                     ensure_ascii=False))
    sys.exit(0)


if __name__ == "__main__":
    main()
