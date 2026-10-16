# Nhận diện ĐHTL cho video

Theo cẩm nang brand.thanglong.edu.vn, giống ứng dụng Chuẩn hóa văn bản (PM duyệt 29/9/2026).

| Tên | Mã | Dùng cho |
|---|---|---|
| Indigo | `#000066` | màu chủ đạo, chữ tiêu đề, khối lớn |
| Indigo nhạt | `#1a1a80` | khối phụ |
| Scarlet | `#f32409` | điểm nhấn: nút kêu gọi, gạch chân, con số quan trọng |
| Scarlet đậm | `#cf1d05` | điểm nhấn khi nền sáng |
| Cultured | `#f9f5f4` | nền sáng |
| Palatinate | `#1d53e6` | màu phụ, dùng ít |
| Chữ thường | `#0a0e18` | |
| Chữ phụ | `#5a6070` | |

- Scarlet chỉ làm điểm nhấn, không làm nền lớn; chữ nhỏ không đặt trên nền Scarlet.
- Phông tiêu đề: Thang Long Sans (`brand/fonts/ThangLongSans-Regular.otf`, `-Medium.otf`, `-Bold.otf`).
- Phông chữ thường: Manrope (`brand/fonts/Manrope-Variable.ttf`).
- Phông web dạng woff2 có dấu tiếng Việt (Be Vietnam Pro, Dancing Script, Roboto Mono): `brand/fonts/web/`.
- Logo: `brand/logo-tlu.png`. Xem logo đúng cỡ hiển thị trước khi giao (bài học `memory/bai-hoc/xem-logo-dung-co-hien-thi.md`).

```css
:root {
  --indigo: #000066; --indigo-nhat: #1a1a80;
  --scarlet: #f32409; --scarlet-dam: #cf1d05;
  --nen: #f9f5f4; --phu: #1d53e6;
  --chu: #0a0e18; --chu-phu: #5a6070;
}
```
