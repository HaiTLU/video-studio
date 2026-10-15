# Nguồn của kỹ năng video-quang-cao-san-pham

Tạo 5/10/2026 theo yêu cầu của PM: "mở X và làm skill cách thức làm video quảng cáo sản phẩm tốt nhất, dù đó là sản phẩm nào, rất chi tiết". PM chọn: kỹ năng riêng, đủ bốn nhóm sản phẩm, có sẵn tùy chọn giọng đọc và linh vật, kèm ví dụ và dựng thử một video.

## Nguồn chính

- @0xMovez, "How to build motion design studio with Opus 5.5 (Full-course)", bài viết dài trên X, 27/9/2026: https://x.com/0xMovez/status/2104216919033192746. Đọc toàn văn qua api.fxtwitter.com ngày 5/10/2026. Gồm 12 mục: 01 khung hình là chương trình, 02 cài đặt, 03 câu lệnh một dòng, 04 nhắm vào sản phẩm, 05 tham chiếu, 06 danh sách trạng thái, 07 bộ dựng seek(t), 08 lò xo, 09 âm thanh, 10 bản chỉ đạo dài, 11 phê bình, 12 xuất bản và đóng gói thành kỹ năng.
- Các bài mẫu bài nguồn nhúng, đọc 5/10/2026:
  - @twoclipping, 24/9/2026 (status 2103273003555402193): mẫu câu lệnh dạng thẻ inputs, direction, structure, build, gotchas cho video giao diện "một khối không cắt", tác giả công khai cho người khác dùng lại.
  - @verbove, 25/9/2026 (status 2103483957266268381): cùng cấu trúc áp vào sản phẩm thật MakerMap, thêm thẻ export xuất mọi khổ song song.
  - @tdinh_me, 26/9/2026 (status 2103703135902740699): video ra mắt TypingMind; câu lệnh thêm ba dòng (đường dẫn sản phẩm, dùng ảnh chụp và logo thật, phải có nhạc). Bài chỉ có lời tác giả, câu lệnh nằm ở trả lời không đọc được.
  - @achxvi, 26 và 27/9/2026 (status 2103918792845963545, 2104014659615392078): video có nhân vật nói (giọng ElevenLabs) và lời chào bán dịch vụ làm video.

Các con số lượt xem, chi phí (khoảng 1.000 USD trước đây), thời gian làm (15-45 phút, 12 giờ) là lời các tác giả, kỹ năng không dùng làm căn cứ.

Kỹ năng không chép nguyên văn câu lệnh hay mã trong bài; cấu trúc được viết lại bằng tiếng Việt. Ba lệnh ffmpeg tạo ảnh ghép trong `cham-diem.md` là lệnh ffmpeg thông dụng, viết lại theo ý bài.

## Quy tắc nào từ đâu

| Quy tắc | Nguồn |
|---|---|
| Câu lệnh chỉ là một phần mười, phần còn lại là khung làm việc | Bài nguồn, mở đầu |
| Câu lệnh một dòng làm video na ná nhau, chỉ dùng thử bộ dựng | Bài nguồn, mục 03 (dẫn bộ dữ liệu của athemeroy) |
| Khung năm nhịp cho phần mềm, dùng tài liệu thật, liệt kê tài liệu trước khi làm chuyển động | Bài nguồn, mục 04 |
| Một phiên cho một nhãn hiệu | Bài nguồn, mục 04 |
| Gọi tên phong cách, đưa khung hình hoặc video mẫu, chỉ lấy ngữ pháp | Bài nguồn, mục 05 |
| Danh sách trạng thái, một khối không cắt, con trỏ điều khiển | Bài nguồn, mục 06; @twoclipping; @verbove |
| Bốn loại lò xo, cộng một lò xo cho mỗi lần đổi đích | Bài nguồn, mục 08 |
| Lưới nhịp, nhịp mạnh cho khoảnh khắc lớn, tiếng động ở đỉnh âm | Bài nguồn, mục 09 |
| Bản chỉ đạo dài, cổng duyệt, bảng nhân vật, ghép tạo rồi vẽ đè | Bài nguồn, mục 10 |
| Ảnh ghép, dải khung, xem ở 360 điểm ảnh, câu lệnh phê bình, lặp tới 8 điểm | Bài nguồn, mục 11 |
| Mọi khổ từ một dòng thời gian, không cắt 16:9 thành dọc | Bài nguồn, mục 12; @verbove |
| Khóa API trong biến môi trường, không dán vào câu lệnh | Bài nguồn, mục 04 |
| Khung năm nhịp cho hàng hóa, dịch vụ, khóa học | Claude chuyển thể từ mục 04 theo cách làm quảng cáo phổ biến (vấn đề, sản phẩm, cho thấy, bằng chứng, lời kêu gọi) |
| Tám tiêu chí chấm | Bảy tiêu chí của mục 11 (mở, đọc được, chuyển động, đa dạng, bố cục, nhận diện, âm thanh); Claude thêm "sản phẩm rõ trước giây 6" và "lời kêu gọi", gộp bố cục với nhận diện |
| Vùng an toàn 9:16 | Claude ước lượng theo giao diện phổ biến của các ứng dụng video ngắn; chưa đo, phải kiểm trên ứng dụng thật |
| Hiểu được khi tắt tiếng | Cách làm quảng cáo video ngắn phổ biến; Claude thêm |
| Luật nội dung (nhất, số một, so sánh) | Luật Quảng cáo số 16/2012/QH13, Điều 8 khoản 9 và 11; luật đã có sửa đổi, phải kiểm bản hiện hành |
| Thời gian đọc chữ, -14 LUFS, rà từng giây P0-P2 | Kỹ năng `video-khoa-hoc` có sẵn trong kho |
| Danh mục phong cách, mẫu Skillry, motion.md, review_log | Kỹ năng `video-chuyen-dong` có sẵn trong kho |
| Tốc độ đọc khoảng 3 âm tiết mỗi giây | Claude ước lượng, phải đo lại trên giọng thật |

## Kho mã bài nguồn liệt kê (chưa kiểm giấy phép từng kho)

Chỉ học cách làm; chép mã thì đọc giấy phép trước. Hai kho PDoomVideo và Battle-of-Austerlitz-Film đã đọc 2/10/2026, không có giấy phép (xem `video-chuyen-dong`).

- github.com/JohnHeibel/PDoomVideo, github.com/JohnHeibel/ClaudeAnimationBase
- github.com/buildwithhanif/claude-animation-skill
- github.com/heygen-com/hyperframes; Remotion: remotion.dev/docs/ai/skills
- github.com/WinterArc21/Battle-of-Austerlitz-Film
- github.com/guanmo-ai/awesome-ai-motion; github.com/athemeroy/awesome-opus-5-5-videos

## Rủi ro đã biết của kỹ năng

- Khung năm nhịp và tám tiêu chí chưa được kiểm bằng số liệu đăng thật; Bước 9 dùng để kiểm sau 3 video.
- Bài nguồn chủ yếu nói về phần mềm. Phần hàng hóa, dịch vụ, khóa học là chuyển thể, chưa có video mẫu lan truyền nào làm bằng cách này để đối chiếu.
- Luật Quảng cáo trích theo bản 2012; điều, khoản có thể đã đổi số sau sửa đổi.
