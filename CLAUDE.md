# CLAUDE.md

Kho sản xuất video của Nguyễn Nam Hải (PM), Trưởng mảng Đào tạo ngắn hạn, Trường Đại học Thăng Long (ĐHTL). Kho tài liệu chính vẫn là `HaiTLU/thanglong_kb`; kho này chỉ để làm video. Trả lời bằng tiếng Việt, dễ hiểu.

## Cách làm một video

1. **Hỏi trước, chạy sau.** Video mới: hỏi PM bằng `AskUserQuestion` (2-4 lựa chọn, khuyến nghị đứng đầu) về mục đích, người xem, khổ (9:16, 16:9, 1:1), độ dài, phong cách, nguồn chữ và số liệu, hạn. PM chọn "Bắt đầu chạy tự động" thì làm đến khi xong, chỉ dừng khi cần làm việc không quay lại được (đăng công khai, gửi ra ngoài, chi tiền).
2. **Chọn kỹ năng theo loại video:**

   | Loại video | Kỹ năng chính | Tra thêm |
   |---|---|---|
   | Giới thiệu khóa học TTC | `video-khoa-hoc` | `video-chuyen-dong`, `embedded-captions` |
   | Quảng cáo, ra mắt sản phẩm (SonicRec, AI Lab, ứng dụng web) | `video-quang-cao-san-pham` | `product-launch-video`, `pr-to-video`, `video-ui-bien-hinh` |
   | Hoạt hình giải thích, reel mạng xã hội | `video-chuyen-dong` | `faceless-explainer`, `motion-graphics`, `video-sang-tao`, `music-to-video` |
   | Cảnh 3D theo mẫu | `video-3d-theo-mau` | `hyperframes-creative` |
   | Chuyển động cho web, ứng dụng | `gsap-core` và nhóm `gsap-*` | `motion-design` (nguyên tắc thời lượng, easing) |
   | Cắt video người nói, thêm phụ đề | `talking-head-recut` | `embedded-captions` |
   | Video hàng loạt từ dữ liệu bằng React | `remotion` | `remotion-to-hyperframes` |
   | Thêm tiếng động, nhạc | `sound-layer` | `hyperframes-audio`, `media-use` |
   | Xem video người khác gửi | `watch` | |

   Việc của TTC và ĐHTL đi qua kỹ năng tiếng Việt của kho trước (`video-*`); kỹ năng gốc tiếng Anh (`hyperframes-*`, `general-video`...) chỉ dùng tra cứu phần dựng.
3. **Dựng bằng HyperFrames, ghim bản `0.8.134`.** Hướng dẫn chung: `.claude/skills/video-khoa-hoc/dung-hyperframes.md`. Đầu phiên chạy `export HYPERFRAMES_NO_TELEMETRY=1 DO_NOT_TRACK=1`. Không dùng dựng trên đám mây, không dùng tính năng cần khóa API.
4. **Tạo thư mục video bằng** `bash scripts/moi-video.sh <DuAn> <TenVideo> [portrait|landscape|square]`. Mỗi video một thư mục `videos/YYMMDD_DuAn_TenVideo/` gồm mã, bảng nhịp, `TIEN-DO.md` khi chưa xong.
5. **Kiểm trước khi giao:** `lint`, `check`, `snapshot` ở các mốc chuyển cảnh, rồi gọi trợ lý con `ra-soat-video` rà từng giây; sửa hết lỗi P0. Chữ trên màn hình rà theo `humanizer` và `.claude/skills/humanizer/tieng-viet.md`.
6. **Giao:** MP4 không đưa vào git (đã chặn trong `.gitignore`); đặt ở `videos/<thư mục>/out/` rồi gửi PM hoặc chép lên Google Drive khi PM cho phép.

## Nhận diện ĐHTL

Bảng màu, phông, logo: `brand/MAU.md`. Phông và logo đã có trong `brand/`, chép vào `assets/` của video, không tải Google Fonts cho chữ chính, không vẽ lại logo.

## Quy tắc chữ (mọi chữ Claude viết: lời trên video, tệp MD, chat)

- Chỉ dùng gạch ngắn `-`, không dùng gạch dài. Không emoji, biểu tượng trong tệp.
- Ưu tiên từ tiếng Việt thông dụng, viết dễ hiểu nhất có thể; không dùng từ trong `memory/context/so-tu-cam.md` (hook `chan-tu-cam.py` tự chặn).
- Số liệu trên video phải có nguồn; không có thì bỏ, không tự ước.
- Bài học đã rút ra: `memory/bai-hoc/` (đọc khi làm video lần đầu trong phiên).

## Tệp, nhánh, an toàn

- Tên tệp: `YYMMDD_DuAn_NoiDung.ext`. Không xóa tệp; bản cũ chép vào `04_Archives/<DuAn>/` với hậu tố `_v1`, `_v2`.
- Kho này được đẩy thẳng lên `main` (PM cho phép 16/10/2026, chỉ áp dụng cho kho video-studio); commit nhỏ, tiêu đề tiếng Việt, không đẩy đè lịch sử. Việc lớn hoặc muốn PM xem trước thì vẫn mở nhánh `claude/<tên-việc>` và PR.
- Hook trong `.claude/hooks/` chặn xóa tệp, `--force`, đọc ghi tệp bí mật. Bị chặn thì làm theo cách đúng hook nêu.
- Kỹ năng chép từ kho `thanglong_kb` ngày 15/10/2026. Một số dòng trong kỹ năng còn nhắc `01_Projects/`, `memory/projects/`, `04_Archives/Projects/KhoTaiLieu/`: đó là ghi chú nguồn gốc ở kho cũ, không phải tệp của kho này. Nguồn và giấy phép từng kỹ năng ngoài: `NGUON.md` hoặc `LICENSE` trong thư mục kỹ năng, tổng hợp ở `tai-lieu/NGUON-KY-NANG.md`.
