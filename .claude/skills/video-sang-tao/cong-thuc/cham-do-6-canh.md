# Công thức: Chấm đỏ 6 cảnh (video TTC, 8/10/2026)

Nguồn: prompt phim chuyển động PM gửi 8/10/2026 (khung 6 khối: inputs, direction, structure, build, gotchas, start; nội dung gốc quảng bá một model AI, không dùng lại) và video đã dựng ở `videos/261008_DaoTaoNganHan_GioiThieuTTC_ChamDo/` (mã, bảng nhịp, ảnh tĩnh).

| Mục | Ghi |
|---|---|
| Độ dài, khổ | 15 giây, 16:9, 60 khung/giây, lặp liền |
| Nhịp | 120 nhịp/phút, 30 phách |
| Vật nối | Một chấm đỏ: núm nút, dấu chấm câu, đầu biểu đồ, đĩa phủ khung, tâm vòng chữ, dấu chấm cuối thẻ |
| Cảnh | Mở (nút bật, chữ rơi, còn "Kỹ năng.") - Lò xo (chấm nhảy, vẽ đường lò xo vọt) - Hình (đĩa phủ khung, vuông xoay, viên thuốc, co về chấm) - Chữ (vòng 5 từ quanh chấm, mở thành chấm nhỏ) - Lưới chấm (lan ra, lật đen) - Thẻ cuối rồi quay ngược về khung đầu |
| Màu | Trắng ngà #f4efe8, đen #0a0a0a, một màu nhấn (đỏ Scarlet #f32409) |
| Phông | Be Vietnam Pro 700 và 900 |
| Chuyển cảnh | Luôn do vật nối gây ra: chấm nhảy, chấm phình, đĩa co, sóng lưới chấm |
| Chuyển động | Lò xo dạng đóng; biểu đồ vọt khoảng 16 phần trăm; chữ rơi từng chữ cái lệch 30 mili giây |
| Điểm nhấn | Đường biểu đồ và chấm cùng một hàm lò xo; khối đổi trạng thái liền mạch |

Ba điều làm phim này đẹp:
1. Một vật nối duy nhất, mọi cảnh chuyển đều do nó gây ra, nên phim thành một mạch.
2. Danh sách cấm cắt hẳn kiểu đồ họa sáo (chuyển sắc, phát sáng, hạt, cắt cảnh ngẫu nhiên).
3. Cổng duyệt rẻ trước khi dựng đủ, và khung cuối khớp khung đầu nên phát lặp không giật.

Điều làm khác cho ĐHTL: chấm không đặt trên chữ i (tiếng Việt có dấu) mà làm dấu chấm cuối câu; biểu đồ không số thật; vòng chữ dùng 5 mảng khóa TTC.

Lỗi hay gặp khi làm theo: xem bảng Lỗi đã gặp ở `../references/quy-trinh-dung.md`.
