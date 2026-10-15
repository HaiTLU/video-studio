#!/usr/bin/env python3
"""Tạo lời đọc tiếng Việt bằng VieNeu-TTS (Apache 2.0, chạy trên CPU, không gửi chữ ra ngoài).

Cài một lần (môi trường riêng, ngoài kho):
    python3 -m venv ~/.vieneu && ~/.vieneu/bin/pip install vieneu "onnxruntime==1.22.1"
onnxruntime 1.30 báo lỗi "External data path escapes model directory" với bộ nhớ đệm
Hugging Face, nên ghim bản 1.22.1 (thử 8/10/2026, vieneu 3.8.3).

Dùng:
    ~/.vieneu/bin/python loi_doc_vieneu.py loi-doc.txt --ra audio/vo [--giong "Hải Đăng"]
loi-doc.txt: mỗi dòng một câu; dòng trống bị bỏ qua.
Ra: vo_01.wav, vo_02.wav... và vo_do-dai.json (độ dài từng câu, giây) để đặt câu vào lưới nhịp.
Xem danh sách giọng: --ds-giong
"""
import argparse
import json
import pathlib
import wave

from vieneu import Vieneu


def do_dai(tep):
    with wave.open(str(tep)) as w:
        return round(w.getnframes() / w.getframerate(), 2)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("tep_chu", nargs="?")
    p.add_argument("--ra", default="vo")
    p.add_argument("--giong", default="Hải Đăng")
    p.add_argument("--ds-giong", action="store_true")
    a = p.parse_args()

    tts = Vieneu()
    if a.ds_giong:
        for nhan, _ in tts.list_preset_voices():
            print(nhan)
        return
    if not a.tep_chu:
        p.error("thiếu tệp lời đọc")

    cau = [d.strip() for d in pathlib.Path(a.tep_chu).read_text(encoding="utf-8").splitlines() if d.strip()]
    thu_muc = pathlib.Path(a.ra)
    thu_muc.mkdir(parents=True, exist_ok=True)
    ket_qua = []
    for i, c in enumerate(cau, 1):
        tep = thu_muc / f"vo_{i:02d}.wav"
        tts.save(tts.infer(c, voice=a.giong), str(tep))
        ket_qua.append({"tep": tep.name, "cau": c, "giay": do_dai(tep)})
        print(f"{tep.name}  {ket_qua[-1]['giay']}s  {c}")
    (thu_muc / "vo_do-dai.json").write_text(json.dumps(ket_qua, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Tổng: {round(sum(k['giay'] for k in ket_qua), 2)}s, giọng {a.giong}")


if __name__ == "__main__":
    main()
