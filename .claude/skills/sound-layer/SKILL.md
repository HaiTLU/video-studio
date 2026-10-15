---
name: sound-layer
description: Thêm lớp tiếng động thật (bản ghi CC0, không tổng hợp) vào video chuyển động đã dựng hình, đặt từng tiếng theo mốc thời gian của chính hoạt ảnh, trộn, rồi chạy bước kiểm tra tự động trên tệp MP4. Dùng khi PM nhờ "thêm tiếng động cho video", "âm thanh video nghe rẻ tiền", "làm sound design", "tiếng khớp hình", hoặc khi một video làm bằng /video-chuyen-dong, /video-khoa-hoc, /video-quang-cao-san-pham cần tiếng chạm, lướt, hiện logo. Chỉ thêm tiếng, không dựng hình; nhạc nền và giọng đọc vẫn theo kỹ năng video đang dùng.
---

# Lớp tiếng động thật cho video

Nguồn nền: kho `Bodila51/opus-sound-layer` (MIT), tác giả bài 0xCodila, bài đăng 9/10/2026. Chi tiết nguồn và phần kho tự thêm: `NGUON.md`. PM duyệt đưa vào kho ngày 11/10/2026.

Vấn đề: Claude không nghe được âm thanh nên tiếng tự tổng hợp thường lệch hình và nghe rẻ. Cách làm ở đây: dùng bản ghi thật, lấy mốc từ hoạt ảnh, nhìn sóng âm để chọn, để bước kiểm tra tự động quyết định đạt hay không, người nghe lại ở cuối.

## Khi nào dùng, khi nào không

- Dùng cho video đã có hình (HyperFrames, Remotion hay bộ dựng nào xuất được thời điểm khung) cần tiếng chạm, lướt, hiện logo, chuyển cảnh.
- Không dùng thay `hyperframes-audio` (trộn nhạc và giọng đã có trong bản dựng) hay `music-to-video` (dựng hình theo nhạc). Hai việc nối nhau: sound-layer đặt tiếng động và xuất `mix.wav`; nhạc nền và giọng đọc theo kỹ năng video đang dùng.
- Máy cần `ffmpeg` và `uv`. Kiểm: `ffmpeg -version`, `uv --version`. Thiếu `uv` thì cài (`pip install uv`), đây là lỗi kỹ thuật, tự xử lý.

## Luật cứng (từ kho gốc, giữ nguyên)

- Không tự viết lại các tệp trong `scripts/`, không nới ngưỡng nào để kiểm tra "đạt".
- Không tổng hợp tiếng chạm, bấm, lướt bằng mã; không dùng tiếng trò đùa. Thiếu loại tiếng thì tìm bản ghi thật (bước 2).
- Tiếng chỉ đặt ở hành động thật. Mỗi khoảng 4 giây có tối đa một tiếng chủ đạo (logo hiện, màn tiết lộ).
- Không gọi âm thanh là "tốt". Báo đúng kết quả kiểm; chất lượng nghe do người quyết.

## Các bước

Đặt thư mục làm việc ngay trong thư mục dự án video; lệnh dưới chạy từ đó, `S` là `.claude/skills/sound-layer`.

**1. Bảng mốc (cues).** Xuất `audio/cues.json` từ chính thời gian của hình (lò xo, hàm easing, `data-start`), không gõ số khung tay. Định dạng: `uv run $S/scripts/mix.py --schema`. Gắn nhãn từng mốc: `cut` (đổi cả khung), `move` (khung có tốc độ lớn nhất), `land` (khung chuyển động dừng), `appear` (phần tử hiện ra). Tiếng chủ đạo dạng "thump+tap" kèm `stop_before` (ngắt nhạc ngay trước) và `build` (tiếng dâng lên).

**2. Chọn tiếng.** Lần đầu: `uv run $S/scripts/sfx.py kit` (tải thư viện về `audio/kit`; chạy nền hoặc cho 10 phút). Thư viện gồm 1.139 âm CC0, 19 loại (hit, boom, riser, reverse, transition, whoosh, swish, glitch, ui, click, key, tick, tap, pop, thump, paper, chime, shimmer, zap), đếm theo `library.json`: 7 gói Kenney và 619 bản Freesound.
- Chọn từng tiếng: `sfx.py browse --type <loại> --like "<chất liệu, độ nặng, tâm trạng>"`, rồi MỞ `audio/browse.png` xem sóng âm, ghi `id` vào mốc. Giữ một họ âm cho cả phim (ví dụ kính và gió, hoặc kim loại và trầm); lặp lại thì đổi biến thể.
- Thiếu loại: `sfx.py search "<chất liệu hành động>" --type <loại>` (Openverse, không cần khóa), xem bằng `sfx.py sheet`, loại bản có hai sự kiện trong một đoạn, tiếng nền đều, tiếng bấm lọt vào tiếng lướt, sóng sin sạch trên tiếng vật thể. Đạt thì `sfx.py add FILE --type <loại> --credit "<nguồn, giấy phép>"`.
- Nhạc nền: nhạc PM có quyền dùng, hoặc vòng nhạc CC0.

**3. Dựng.** Xuất hình không tiếng, rồi:
```bash
uv run $S/scripts/mix.py audio/cues.json
ffmpeg -i video.mp4 -i audio/mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 256k -shortest out/final.mp4
uv run $S/scripts/qa.py out/final.mp4
```

**4. Kiểm.** Mỗi dòng FAIL sửa bằng cách đổi mốc hoặc đổi tiếng, tối đa 2 vòng. Mở `audio/qa.png`, mô tả điều thấy tại từng mốc chủ đạo. Còn FAIL sau 2 vòng thì báo PM, không nới ngưỡng.

**5. Giao.** `final.mp4`, `audio/kit/CREDITS.md`, và `LISTEN.md` ghi 5 mốc thời gian để PM nghe bằng tai. Báo kết quả kiểm, không khen âm thanh.

## Giới hạn và rủi ro

- Mới chạy thử `mix.py --schema`, chưa thử trên video thật của PM; chạy lần đầu trên một video ngắn rồi mới dùng rộng (PM chọn "đưa vào kho ngay", lần dùng đầu coi là thử).
- Bài đăng ghi "26 recordings" nhưng README và `library.json` cho 1.139 âm; theo tệp mã. Chưa kiểm từng âm có đúng CC0.
- Âm Freesound và Kenney đều ghi CC0 trong kho gốc; video công bố của Trường vẫn nên giữ `CREDITS.md` kèm bản dựng.
- Lần chạy `kit` cần mạng ra `kenney.nl`, `freesound.org`, `cdn.freesound.org`; phiên web có thể chặn. Bị chặn thì báo PM, không tìm đường vòng.
