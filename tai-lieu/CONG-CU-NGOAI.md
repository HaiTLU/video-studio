# Công cụ ngoài dùng khi cần

Không cài sẵn vào kho. Chạy bằng `npx` hoặc cài trong thư mục video cần dùng.

## SVGO - làm gọn tệp SVG

- Kho: github.com/svg/svgo, giấy phép MIT
- Dùng cho logo, biểu tượng SVG trước khi đưa vào `assets/` của video.
- Lệnh: `npx -y svgo@3 vao.svg -o ra.svg`
- Đã thử ngày 16/10/2026 trên một tệp SVG mẫu: nhỏ đi 12,6%, hình không đổi.
- Logo ĐHTL trong `brand/` là PNG; không vẽ lại thành SVG (CLAUDE.md).

## Satori - làm ảnh bìa hàng loạt từ HTML và CSS

- Kho: github.com/vercel/satori, giấy phép MPL-2.0 (bản npm 0.62.0)
- MPL-2.0 chỉ ràng buộc tệp mã của chính Satori. Dùng làm thư viện trong video thì không sao; không chép mã nguồn Satori vào kho này.
- Dùng khi cần ảnh bìa, thumbnail cho nhiều khóa cùng một mẫu.
- Phải nạp phông từ `brand/fonts/`, không tải Google Fonts. Kiểm chữ có dấu tiếng Việt hiện đúng trước khi làm hàng loạt.
- Chưa dựng thử trong kho này.
