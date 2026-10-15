"""Xuất dự án HyperFrames (thư mục có index.html, khung từ khung.html) thành video, mờ chuyển động bằng khung con.

  python3 render.py <thư mục dự án> --duration 14 --out video.mp4
  python3 render.py <thư mục dự án> --duration 14 --beats beats.json --out kiem/   # một ảnh mỗi phách + bảng ghép

Thay bản cũ (Playwright tự chụp, lưu ở 04_Archives/Projects/KhoTaiLieu/261008_KhoTaiLieu_video-ui-bien-hinh_render_v1.py).
HyperFrames dựng ở 60 x sub khung/giây; ffmpeg tmix trộn sub khung con thành 1 khung rồi giữ khung cuối mỗi nhóm,
ra 60 fps. Nhạc lấy từ thẻ <audio> trong index.html (HyperFrames tự trộn), ở đây chỉ chép sang.
"""
import argparse, json, os, shutil, subprocess, tempfile
from pathlib import Path

HF = ["npx", "-y", "hyperframes@0.8.134"]
ENV = {**os.environ, "HYPERFRAMES_NO_TELEMETRY": "1", "DO_NOT_TRACK": "1"}


def hf(args, cwd):
    subprocess.run(HF + args, cwd=cwd, env=ENV, check=True)


def render_video(a):
    fps, sub = 60, a.sub
    out = Path(a.out).resolve()
    hf(["check"], a.project)
    with tempfile.TemporaryDirectory() as tmp:
        raw = Path(tmp) / "raw.mp4"
        hf(["render", "--fps", str(fps * sub), "--quality", "delivery", "--output", str(raw)], a.project)
        # tmix: khung k = trung bình khung con k-sub+1..k. Giữ khung có k mod sub = sub-1 (framestep lấy lệch).
        vf = (f"tmix=frames={sub}:weights={' '.join(['1'] * sub)},"
              f"select='eq(mod(n\\,{sub})\\,{sub - 1})',setpts=N/({fps}*TB)") if sub > 1 else "null"
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(raw), "-vf", vf, "-r", str(fps),
                        "-c:v", "libx264", "-crf", "14", "-preset", "slow", "-pix_fmt", "yuv420p",
                        "-c:a", "copy", "-movflags", "+faststart", str(out)], check=True)
    n = subprocess.run(["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0", "-show_entries",
                        "stream=nb_read_frames", "-of", "csv=p=0", str(out)], capture_output=True, text=True)
    print(out, "khung:", n.stdout.strip(), "(phải bằng", round(a.duration * fps), ")")


def render_beats(a):
    beats = json.load(open(a.beats))["beats"]
    out = Path(a.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    # chụp sau phách 0.12 giây: lúc chuyển động đã rõ hướng nhưng chưa xong; thêm khung đầu và ngay trước T
    times = [(t + 0.12) % a.duration for t in beats] + [0, a.duration - 1e-6]
    with tempfile.TemporaryDirectory() as tmp:
        hf(["snapshot", "--no-end", "--at", ",".join(f"{t:.6f}" for t in times), "--output", tmp], a.project)
        shots = sorted(Path(tmp).glob("frame-*.png"))
        assert len(shots) == len(times), f"snapshot trả {len(shots)} ảnh, cần {len(times)}"
        for i, f in enumerate(shots[:len(beats)]):
            shutil.copy(f, out / f"phach_{i:02d}.png")
        shutil.copy(shots[-2], out / "dau.png")
        shutil.copy(shots[-1], out / "cuoi.png")
    cols = 7
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-framerate", "1", "-i", str(out / "phach_%02d.png"),
                    "-vf", f"scale=360:360,tile={cols}x{-(-len(beats) // cols)}:padding=8:color=white",
                    "-frames:v", "1", str(out / "bang_phach.png")], check=True)
    print(out / "bang_phach.png")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("project", help="thư mục dự án HyperFrames (có index.html)")
    ap.add_argument("--duration", type=float, required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--beats", help="beats.json: chỉ chụp một ảnh mỗi phách để duyệt")
    ap.add_argument("--sub", type=int, default=4)
    a = ap.parse_args()
    render_beats(a) if a.beats else render_video(a)
