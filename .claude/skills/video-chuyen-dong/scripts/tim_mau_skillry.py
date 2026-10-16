#!/usr/bin/env python3
"""Tìm mẫu video Skillry gần nhất với nội dung đang dựng, từ thư viện đã lưu.

Dùng: python3 tim_mau_skillry.py "từ khóa 1" "từ khóa 2" ... [--nhom motion|explainer|3d|interactive] [--top 5]
Từ khóa viết tiếng Anh (prompt gốc tiếng Anh): launch, course, data, logo, typography, timeline...
Nguồn: tai-lieu/thu-vien-prompt-skillry.md (279 prompt đầy đủ).
"""
import re, sys, pathlib

KHO = pathlib.Path(__file__).resolve().parents[4]
TEP = KHO / "tai-lieu/thu-vien-prompt-skillry.md"
NHOM = {"Chuyển động": "motion", "Giải thích": "explainer", "Cảnh 3D": "3d", "Tương tác": "interactive"}

def doc():
    nhom, mau = None, []
    for khoi in re.split(r"\n(?=## |### )", TEP.read_text(encoding="utf-8")):
        if khoi.startswith("## "):
            nhom = next((v for k, v in NHOM.items() if k in khoi.split("\n")[0]), None)
        elif khoi.startswith("### "):
            d = khoi.split("\n")
            ma, _, tg = d[0][4:].partition(" - ")
            skillry = re.search(r"Skillry: (\S+)", khoi)
            ky = re.search(r"kỹ thuật: ([^\n]+)", khoi)
            p = re.search(r"~~~text\n(.*?)\n~~~", khoi, re.S)
            mau.append(dict(ma=ma, tg=tg, nhom=nhom, url=skillry.group(1) if skillry else "",
                            kt=ky.group(1) if ky else "", prompt=p.group(1) if p else ""))
    return mau

def main(a):
    top, nhom = 5, None
    if "--top" in a: i = a.index("--top"); top = int(a[i + 1]); del a[i:i + 2]
    if "--nhom" in a: i = a.index("--nhom"); nhom = a[i + 1]; del a[i:i + 2]
    tk = [t.lower() for t in a]
    if not tk: sys.exit(__doc__)
    ds = []
    for m in doc():
        if nhom and m["nhom"] != nhom: continue
        p = m["prompt"].lower()
        diem = sum(min(p.count(t), 3) for t in tk) + (2 if "hyperframes" in (p + m["kt"].lower()) else 0)
        # prompt ngắn gọn nhưng đủ ý dễ học hơn prompt quá dài
        diem += 1 if 200 <= len(p) <= 1500 else 0
        if diem > 1: ds.append((diem, m))
    for diem, m in sorted(ds, key=lambda x: -x[0])[:top]:
        print(f"[{diem}] {m['ma']} | {m['nhom']} | {m['tg']} | {m['kt']}\n  {m['url']}\n  {m['prompt'][:300].replace(chr(10), ' ')}\n")

main(sys.argv[1:])
