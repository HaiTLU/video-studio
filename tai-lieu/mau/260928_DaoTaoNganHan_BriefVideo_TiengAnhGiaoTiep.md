# Bản hướng dẫn làm video 20 giây - Khóa Tiếng Anh giao tiếp (TTC)

**Cách dùng:** điền các chỗ `[ĐIỀN]`, mở **phiên Claude Code mới** trong kho này, dán toàn bộ phần "Lời dặn gửi Claude" bên dưới. Nên chọn Opus 5.5, mức high.

**Trước khi dán, cần anh quyết:**
- Bộ màu: **đã chốt (a)** ngày 29/9/2026 - Indigo `#000066`, Scarlet `#f32409` (chỉ làm điểm nhấn), nền Cultured `#f9f5f4`, phông Thang Long Sans và Manrope (tệp phông trong `01_Projects/Web_ChuanHoaVanBan/src/app/fonts/`).
- Cách nhanh hơn: gõ `/video-khoa-hoc` kèm thông tin khóa, kỹ năng tự điền khung này.
- Video phải được bộ phận truyền thông hoặc Marcom duyệt trước khi đăng.

---

## Lời dặn gửi Claude

Làm một video quảng cáo **20 giây, khổ dọc 9:16** (dùng cho Facebook, Zalo, TikTok) cho khóa **Tiếng Anh giao tiếp** của Trung tâm Đào tạo ngắn hạn và Chuyển giao Công nghệ (TTC), Trường Đại học Thăng Long. Sau đó xuất thêm bản **16:9** từ cùng một dòng thời gian (sắp xếp lại bố cục, không cắt xén).

### 1. Ý chính (một câu)
Nói tiếng Anh tự tin trong công việc và cuộc sống sau `[ĐIỀN: số tuần]` tuần, học ngay tại Trường Đại học Thăng Long.

### 2. Thông tin thật (chỉ dùng đúng các thông tin này, không tự thêm)
- Đối tượng: `[ĐIỀN: sinh viên / người đi làm / ...]`
- Khai giảng: `[ĐIỀN: ngày]` - Lịch học: `[ĐIỀN]` - Địa điểm: `[ĐIỀN]`
- Học phí hoặc ưu đãi: `[ĐIỀN, hoặc bỏ dòng này]`
- Đăng ký: `[ĐIỀN: đường dẫn hoặc mã QR, số điện thoại]`
- Logo: dùng tệp `01_Projects/Web_ChuanHoaVanBan/public/logo-tlu.png` (không tự vẽ lại logo).
- Không đưa lời hứa không có thật (ví dụ "đảm bảo 100%", "giáo viên bản ngữ" nếu không đúng).

### 3. Phong cách
- Màu: Indigo `#000066` chủ đạo, Scarlet `#f32409` làm điểm nhấn, nền sáng Cultured `#f9f5f4`; gọn gàng, trẻ trung, không lòe loẹt.
- Chữ: tiêu đề Thang Long Sans, chữ thường Manrope; chép tệp phông từ `01_Projects/Web_ChuanHoaVanBan/src/app/fonts/` vào thư mục video, không dựa vào Google Fonts.
- Không dùng hình người thật. Được dùng hình khối, biểu tượng đơn giản, bong bóng hội thoại, chữ động.
- Tránh kiểu mặc định "chữ giữa màn hình trên nền chuyển màu, mọi thứ mờ dần hiện ra".

### 4. Dàn cảnh (20 giây)

| Giây | Nội dung | Chữ trên màn hình |
|---|---|---|
| 0-2 | Móc câu: bong bóng hội thoại tiếng Anh bật lên liên tiếp | "Ngại nói tiếng Anh?" |
| 2-6 | Tình huống quen thuộc: họp, phỏng vấn, du lịch (vẽ bằng hình khối) | "Họp. Phỏng vấn. Du lịch." |
| 6-11 | Khóa học giải quyết: 3 điểm nổi bật hiện lần lượt | `[ĐIỀN: 3 điểm, ví dụ học nhóm nhỏ, luyện nói mỗi buổi...]` |
| 11-15 | Thông tin khóa: khai giảng, lịch học, địa điểm | Theo mục 2 |
| 15-20 | Kêu gọi: logo Trường, cách đăng ký, khung hình cuối đứng yên đủ lâu để đọc | "Đăng ký ngay: `[ĐIỀN]`" |

Mỗi 3-4 giây có một chuyển động mới. Chữ đủ to để đọc trên điện thoại, tối đa 8 từ mỗi dòng.

### 5. Âm thanh
Nhạc nền **tự tổng hợp bằng mã** (không dùng nhạc có bản quyền), nhịp vui vẻ khoảng 110-120 nhịp/phút, các lần chuyển cảnh khớp với nhịp. Không dùng giọng đọc AI.

### 6. Cách làm (kỹ thuật)
- Chỉ dùng cách đơn giản nhất: **một tệp `index.html`** có hàm `seek(t)` vẽ đúng khung hình ở thời điểm t; dùng Playwright chụp từng khung (60 hình/giây) và ffmpeg ghép thành MP4. Không dùng dịch vụ trả phí, không cần khóa API.
- Chuyển động dùng lò xo có công thức (không dùng đường cong cố định), để nhìn mượt và vẫn vẽ lại được bất kỳ khung nào.
- Nếu máy chưa có ffmpeg thì cài (`apt-get install ffmpeg`).
- Làm việc trong thư mục `01_Projects/DaoTao_NganHan/Marketing đào tạo ngắn hạn/Video_TiengAnhGiaoTiep/`.

### 7. Các mốc (không bỏ qua mốc nào)
1. Viết kế hoạch và dàn cảnh chi tiết, **dừng lại cho tôi duyệt**.
2. Vẽ 5 khung hình tĩnh (một khung mỗi cảnh), **dừng lại cho tôi duyệt**.
3. Dựng bản đầy đủ, ghép nhạc, xuất video.

### 8. Vòng tự soát lỗi
Sau mỗi lần dựng, chụp khung hình ở các giây 1, 4, 8, 13, 18, tự chấm từng khung theo thang 10 (chữ rõ, bố cục, màu, dấu tiếng Việt, đúng thông tin). Ghi 3 lỗi nặng nhất, sửa, dựng lại. Dừng khi mọi khung đạt từ 8 điểm, **tối đa 3 vòng**.

### 9. Thành phẩm
- `TiengAnhGiaoTiep_9x16.mp4` và `TiengAnhGiaoTiep_16x9.mp4`
- Một ảnh đại diện (poster) và một ảnh ghép tất cả cảnh
- Mã nguồn gọn kèm `README.md` ghi cách dựng lại khi đổi ngày khai giảng hoặc học phí

---

**Ghi chú:** bản hướng dẫn phỏng theo khung "bản hướng dẫn đạo diễn" trong bài của @0xMovez về làm video bằng Opus 5.5 (27/9/2026). Clip ngắn thế này thường mất khoảng 30-60 phút; gõ `/usage` trước và sau để xem chi phí.
