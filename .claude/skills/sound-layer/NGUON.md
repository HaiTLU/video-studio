# Nguồn

- Thư mục `scripts/` (`sfx.py`, `mix.py`, `qa.py`, `library.json`), `README-goc.md`, `PROMPT-goc.md` chép nguyên từ kho github.com/Bodila51/opus-sound-layer, nhánh main, commit 52ac266 (10/10/2026).
- Giấy phép MIT (Bodila51), bản giấy phép ở `LICENSE-opus-sound-layer`. Không sửa tệp gốc; muốn cập nhật thì chép lại từ kho gốc. `SKILL.md` do kho ĐHTL viết bằng tiếng Việt, tóm quy trình trong `PROMPT-goc.md`.
- Âm thanh không lưu trong kho này: `sfx.py kit` tải gói CC0 của Kenney và bản ghi Freesound về thư mục dự án, ghi nguồn vào `audio/kit/CREDITS.md`.
- Nguồn gợi ý: ảnh chụp bài "Sound design for Opus 5.5: no more cheap beeps" (0xCodila, 9/10/2026) PM gửi ngày 11/10/2026.
- Đã rà mã bằng tìm kiếm lệnh hệ thống, địa chỉ mạng, lệnh xóa và đọc các đoạn liên quan trước khi chép (11/10/2026), chưa đọc từng dòng: chỉ gọi `ffmpeg`; mạng chỉ tới `kenney.nl`, `freesound.org`, `cdn.freesound.org` và `api.openverse.org`; xóa tệp chỉ trong thư mục thư viện âm do chính nó tạo; không đọc tệp ngoài phạm vi, không gửi dữ liệu đi.
- Đã chạy thử `mix.py --schema` (cài đủ thư viện qua `uv`, in đúng mẫu bảng mốc). Chưa chạy `kit`, dựng mix và `qa.py` trên video thật.
