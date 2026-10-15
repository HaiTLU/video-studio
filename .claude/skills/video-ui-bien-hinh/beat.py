"""Đo lưới nhịp của bài nhạc và đỉnh của tiếng động UI. Chỉ cần numpy và ffmpeg.

  python3 beat.py nhac.mp3 --bpm 120 --bars 7      -> beats.json (nhịp, phách mạnh, điểm cắt)
  python3 beat.py --peak click.wav pop.wav         -> độ lệch đỉnh (giây) của từng tiếng động
  python3 beat.py nhac.mp3 --mix su_kien.json -o nhac_cat.wav --beats-json beats.json
      -> cắt nhạc theo start/duration trong beats.json, fade 10 ms, trộn tiếng động.
      su_kien.json: [{"t": 0.5, "file": "click.wav", "gain": 0.7}, ...]  (t tính từ điểm cắt)

Đặt tiếng động: thời điểm bắt đầu = thời điểm sự kiện - độ lệch đỉnh, để đỉnh rơi đúng phách.
Đuôi tiếng động tràn qua cuối vòng được cuộn về đầu, để vòng lặp không tách tiếng.
"""
import argparse, json, subprocess, sys
import numpy as np

SR = 22050


def load(path, sr=SR):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(sr),
                          "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32)


def onset_envelope(y, hop=256, n=1024):
    """Spectral flux: tổng phần năng lượng phổ tăng lên giữa hai khung liền nhau."""
    win = np.hanning(n)
    frames = np.lib.stride_tricks.sliding_window_view(y, n)[::hop] * win
    mag = np.log1p(np.abs(np.fft.rfft(frames, axis=1)))
    flux = np.maximum(0, np.diff(mag, axis=0))
    low = flux[:, : int(150 * n / SR)].sum(1)            # dải dưới 150 Hz: trống kick
    env = flux.sum(1)
    env = (env - env.mean()) / (env.std() + 1e-9)
    lag = (hop + n / 2) / SR                              # flux[k] ứng với giữa khung k+1
    return env, low, SR / hop, lag


def tempo(env, fps, guess, spread=0.08):
    """Tự tương quan, chỉ tìm quanh BPM đoán (±8%) để không nhầm nửa hay gấp đôi."""
    ac = np.correlate(env, env, "full")[len(env) - 1:]
    lags = np.arange(len(ac))
    bpm = 60 * fps / np.maximum(lags, 1)
    ok = (bpm > guess * (1 - spread)) & (bpm < guess * (1 + spread))
    lag = lags[ok][np.argmax(ac[ok])]
    # tinh chỉnh dưới một khung bằng parabol
    a, b, c = ac[lag - 1], ac[lag], ac[lag + 1]
    lag = lag + 0.5 * (a - c) / (a - 2 * b + c)
    return 60 * fps / lag


def phase(env, fps, bpm):
    """Pha của lưới phách: dịch lưới sao cho tổng onset rơi trên phách lớn nhất."""
    period = 60 * fps / bpm
    best, best_s = 0.0, -1e9
    for off in np.linspace(0, period, 200, endpoint=False):
        idx = np.round(np.arange(off, len(env) - 1, period)).astype(int)
        s = env[idx].sum()
        if s > best_s:
            best, best_s = off, s
    return best / fps


def downbeat(low, fps, bpm, t0, meter=4):
    """Phách mạnh: trong 4 cách chọn phách đầu ô nhịp, lấy cách có kick mạnh nhất."""
    spb = 60 / bpm
    scores = []
    for k in range(meter):
        ts = np.arange(t0 + k * spb, len(low) / fps - 0.1, meter * spb)
        scores.append(low[np.round(ts * fps).astype(int)].mean())
    return t0 + int(np.argmax(scores)) * spb, scores


def peak_offset(path):
    y = load(path, 48000)
    return float(np.argmax(np.abs(y)) / 48000)


def mix(song, events_path, beats_path, out, sr=48000):
    import wave
    bj = json.load(open(beats_path))
    y = load(song, sr)
    a, n = int(round(bj["start"] * sr)), int(round(bj["duration"] * sr))
    y = y[a:a + n].astype(np.float64).copy()
    f = int(0.01 * sr)
    y[:f] *= np.linspace(0, 1, f)
    y[-f:] *= np.linspace(1, 0, f)
    for e in json.load(open(events_path)):
        s = load(e["file"], sr).astype(np.float64) * e.get("gain", 1.0)
        i0 = int(round((e["t"] - np.argmax(np.abs(s)) / sr) * sr))
        idx = (i0 + np.arange(len(s))) % n          # cuộn qua mép vòng
        np.add.at(y, idx, s)
    peak = np.abs(y).max()
    if peak > 0.98:
        y *= 0.98 / peak
    w = wave.open(out, "wb")
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
    w.writeframes((y * 32767).astype("<i2").tobytes()); w.close()
    print(f"{out}: {n / sr:.3f} giây, đỉnh {peak:.2f}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("song", nargs="?")
    ap.add_argument("--bpm", type=float, default=120)
    ap.add_argument("--bars", type=int, default=7)
    ap.add_argument("--start-bar", type=int, default=0, help="bỏ qua N ô nhịp đầu (intro)")
    ap.add_argument("--peak", nargs="*")
    ap.add_argument("--mix", help="su_kien.json: trộn tiếng động vào nhạc đã cắt")
    ap.add_argument("--beats-json", default="beats.json")
    ap.add_argument("-o", default="beats.json")
    a = ap.parse_args()

    if a.mix:
        mix(a.song, a.mix, a.beats_json, a.o)
        return

    if a.peak:
        for p in a.peak:
            print(f"{p}\t{peak_offset(p):.4f}")
        return

    y = load(a.song)
    env, low, fps, lag = onset_envelope(y)
    bpm = tempo(env, fps, a.bpm)
    t0 = phase(env, fps, bpm)
    db, scores = downbeat(low, fps, bpm, t0)
    db += lag
    spb = 60 / bpm
    start = db + a.start_bar * 4 * spb
    n = a.bars * 4
    out = {
        "bpm": round(bpm, 3),
        "spb": spb,
        "start": round(start, 4),              # cắt nhạc từ đây (phách mạnh)
        "duration": round(n * spb, 4),         # độ dài vòng lặp
        "beats": [round(i * spb, 4) for i in range(n)],   # tính từ điểm cắt
        "kick_score_by_offset": [round(float(s), 3) for s in scores],
    }
    json.dump(out, open(a.o, "w"), indent=1)
    print(json.dumps({k: out[k] for k in ("bpm", "start", "duration")}))
    if abs(bpm - a.bpm) > 1:
        print(f"Chú ý: đo được {bpm:.2f} BPM, lệch BPM đoán. Nghe lại trước khi dùng.", file=sys.stderr)


if __name__ == "__main__":
    main()
