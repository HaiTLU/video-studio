---
name: remotion
description: Dựng video bằng Remotion (React) cho khóa học, bài giảng, báo cáo số liệu và video hàng loạt từ dữ liệu, có phụ đề tiếng Việt. Dùng khi PM nhắc Remotion, hoặc cần dựng nhiều video từ bảng dữ liệu, chứng nhận hàng loạt. Không dùng cho video đơn lẻ nhỏ, đã có video-chuyen-dong và video-khoa-hoc làm bằng HTML, Playwright, ffmpeg.
---

# Remotion

Bản ổn định tại 5/10/2026: 4.0.532. Bản 5 chưa phát hành, mọi mã viết theo cú pháp bản 4. Bộ nền màu, chữ, nhịp: Design System "Remotion Kit" (https://claude.ai/artifact/NSRqAUE8DXDhXg4rK4hMvE).

## Cổng 1: giấy phép (làm trước tiên)

Giấy phép Remotion miễn phí cho cá nhân, công ty tối đa 3 người và tổ chức phi lợi nhuận; từ 4 người phải mua. Văn bản không nêu tên trường đại học. Chưa có xác nhận bằng văn bản từ Remotion thì: chỉ thử trên máy, không đưa sản phẩm ra cho Trường, và nhắc PM hỏi Remotion qua remotion.pro. PM đã quyết không cài ngày 2/10 và 4/10/2026; đây là lần xem lại vì cần dựng hàng loạt. Hỏi PM bằng hộp thoại trước khi cài.

## Khi nào dùng Remotion, khi nào không

| Việc | Dùng |
|---|---|
| Video quảng bá đơn, làm một lần | `video-chuyen-dong` hoặc `video-khoa-hoc` (HTML, Playwright, ffmpeg) |
| Mỗi dòng bảng một video hay một ảnh (chứng nhận, thư mời, báo cáo từng khóa) | Remotion |
| Biểu đồ động từ Excel lặp lại hằng kỳ | Remotion |
| Phụ đề từng từ cho bài giảng dài | Remotion với `@remotion/captions` và Whisper |

## Quy trình

1. Hỏi PM bằng hộp thoại: loại video, khung hình (9:16, 16:9), dự án (màu, logo), nguồn dữ liệu.
2. Lập dự án: `npx create-video --yes --blank --no-tailwind <ten>` rồi `npx remotion skills add` (kỹ năng chính thức của Remotion, có `remotion-best-practices`; đọc nó trước khi viết).
3. Tạo `src/theme.ts` từ token của Remotion Kit; cảnh không ghi màu hay phông trực tiếp.
4. Dựng cảnh theo `references/mau-video.md`; quy tắc kỹ thuật ở `references/luat-ky-thuat.md`.
5. Kiểm tra: `npx remotion still` một khung có chữ tiếng Việt nhiều dấu và đọc ảnh; render cả video hai lần, so kết quả; xem lại từng cảnh. Dựng hàng loạt: thử 3 dòng dữ liệu trước.
6. Rà chữ trong video bằng `humanizer`; báo PM thời lượng, kích thước, nơi lưu.

## Việc thu thập dữ liệu giao trợ lý

Dò gói, phiên bản, mẫu: haiku. Đọc kỹ thuật, giấy phép, phản biện: sonnet. Tối đa 3 trợ lý mỗi yêu cầu theo CLAUDE.md; workflow nhiều trợ lý chỉ chạy khi PM yêu cầu rõ. Danh sách vai ở `references/mau-video.md` cuối tệp.
