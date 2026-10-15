# video-studio

Kho sản xuất video của Trung tâm Đào tạo ngắn hạn, Trường Đại học Thăng Long. Claude Code đọc `CLAUDE.md` và các kỹ năng trong `.claude/skills/` để viết, dựng và kiểm video bằng HyperFrames (HTML, GSAP ra MP4).

## Bắt đầu

1. Mở kho bằng Claude Code (máy hoặc claude.ai/code), nói loại video cần làm. Claude hỏi lại vài câu rồi chọn kỹ năng phù hợp.
2. Tự tạo thư mục video: `bash scripts/moi-video.sh DaoTaoNganHan TiengAnhGiaoTiep portrait`.
3. Xem và chỉnh: trong thư mục video chạy `npm run dev` (HyperFrames Studio, kéo chỉnh dòng thời gian, sửa chữ).
4. Dựng: `npm run render`, tệp MP4 ra thư mục `out/` (không đưa lên git).

Cần Node.js 22 trở lên và ffmpeg.

## Thư mục

| Thư mục | Chứa gì |
|---|---|
| `.claude/skills/` | 40 kỹ năng video, chuyển động, âm thanh, chữ |
| `.claude/agents/` | trợ lý con `ra-soat-video` (rà từng giây), `kiem-chung`, `do-tim` |
| `.claude/hooks/` | chặn xóa tệp, đẩy thẳng lên main, từ cấm |
| `brand/` | bảng màu, phông Thang Long Sans, Manrope, logo ĐHTL |
| `videos/` | mỗi video một thư mục `YYMMDD_DuAn_TenVideo/`; có sẵn video mẫu "Chấm đỏ" giới thiệu TTC |
| `tai-lieu/` | bản hướng dẫn mẫu, thư viện câu lệnh Skillry, nguồn và giấy phép kỹ năng |
| `memory/` | bài học khi làm video, sổ từ cấm |
| `04_Archives/` | bản cũ trước khi sửa |
