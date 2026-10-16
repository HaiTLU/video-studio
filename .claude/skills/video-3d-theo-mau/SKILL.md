---
name: video-3d-theo-mau
description: Làm lại video đồ họa chuyển động 3D đang thịnh hành theo một video mẫu, cho nội dung của TTC hoặc Trường Đại học Thăng Long. Claude phân tích video mẫu từng cảnh, soạn gói câu lệnh (prompt) cho công cụ tạo video AI để PM tự chạy, và dựng phần chữ, logo, khung cuối bằng mã để đúng nhận diện ĐHTL. Dùng khi PM gõ /video-3d-theo-mau hoặc nhờ "làm video 3D theo mẫu này", "bắt chước video motion 3D", "phân tích video mẫu thành câu lệnh". Không dùng giọng đọc. Video quảng cáo khóa 20 giây thuần mã thì dùng /video-khoa-hoc.
---

# Video 3D theo video mẫu

Nội dung: Phân công; Quan hệ với kỹ năng video khác; Bước 0 đến 5 (đầu vào, phân tích mẫu, câu lệnh, dựng mã, ghép, tái dùng); Kiểm trước khi giao; Thư mục; Rủi ro; Lỗi hay gặp; Gợi ý model.

Nguồn: bản tóm tắt một video hướng dẫn tạo lại video đồ họa chuyển động 3D bằng AI mà không cần After Effects (PM gửi 1/10/2026). Các mốc thời gian, tên mô hình và công cụ dưới đây lấy từ bản tóm tắt đó; Claude chưa xem trực tiếp video nên phần nào là cách làm của tác giả thì ghi là "theo video", không khẳng định là đúng hay mới nhất. Tên mô hình và giao diện công cụ ngoài hay đổi, PM kiểm tra lại khi dùng.

## Phân công (PM chốt 1/10/2026: kết hợp cả hai)

| Phần | Ai làm | Bằng gì |
|---|---|---|
| Phân tích video mẫu, viết câu lệnh từng cảnh | Claude | Tách khung hình bằng ffmpeg, xem từng ảnh |
| Cảnh 3D chân thật (vật thể, máy quay, chất liệu) | PM tự chạy | Công cụ tạo video AI (theo video: Google Flow, mô hình Omni 1.1 Flash) |
| Chữ, logo, khung cuối, số liệu, cách đăng ký | Claude | HyperFrames như `video-khoa-hoc` (`video-khoa-hoc/dung-hyperframes.md`) |
| Ghép clip, nhạc, tiếng động | Claude (mặc định) hoặc PM | ffmpeg; hoặc CapCut nếu PM muốn tự ghép |
| **Giọng đọc** | **Không làm** | PM chốt không dùng giọng đọc AI |

Claude không gọi dịch vụ trả phí thay PM và không đưa tài khoản hay khóa API của PM vào kho.

## Quan hệ với các kỹ năng video khác

- Bộ màu, phông, logo, thư mục lưu, rà từng giây P0-P2: theo `video-khoa-hoc`. Bản chỉ đạo, bảng nhịp, nhạc khớp nhịp, chấm điểm: theo `video-chuyen-dong`. Không chép lại ở đây.
- Kỹ năng này chỉ thêm: phân tích video mẫu thành gói câu lệnh 3D, nhận và ghép clip do PM tạo, và tái dùng phong cách cho nội dung mới.

## Bước 0 - Nhận đủ đầu vào

Thiếu mục nào thì hỏi PM một lần bằng hộp thoại (`AskUserQuestion`), không đoán:

- **Video mẫu**: tệp hoặc đường dẫn tải được do PM gửi. Đường dẫn bị chặn (như YouTube đòi đăng nhập) thì nhờ PM gửi tệp.
- **Nội dung mới**: video cho việc gì (AI Lab, khóa học, hội thảo...), thông điệp một câu, chữ phải hiện trên màn hình (PM cung cấp, chép nguyên văn), độ dài, khổ (9:16, 16:9 hoặc cả hai).
- **Điều không muốn**: ví dụ không có người, không chữ chạy.
- **Ai ghép cuối**: Claude ghép bằng ffmpeg hay PM ghép bằng CapCut.

## Bước 1 - Phân tích video mẫu từng cảnh (theo video: 0:58-1:51)

1. Tách khung hình: `ffmpeg -i mau.mp4 -vf fps=2 mau_%03d.png`, cộng thêm khung ngay trước và sau mỗi lần đổi cảnh. Xem lần lượt từng ảnh.
2. Lập bảng cảnh. Mỗi cảnh ghi: giây bắt đầu và kết thúc, vật thể chính, chất liệu và màu, góc máy (cận, toàn, từ trên, từ dưới), chuyển động máy quay, ánh sáng, cách nối sang cảnh sau, chữ trên màn hình (nếu có).
3. Viết `phong-cach-<ten>.md`: nhịp cảnh, bảng màu, kiểu chuyển cảnh, kết cấu chất liệu.
4. **Chỉ học cách làm** (nhịp, góc máy, chất liệu, chuyển cảnh). Không lấy nội dung, logo, nhân vật, câu chữ hay hình của video mẫu. Bản chỉ đạo ghi rõ điều này.
5. Video mẫu của người khác mà PM định đăng lại theo phong cách gần giống: nhắc PM cân nhắc bản quyền và nhờ Marcom duyệt.

Claude chỉ thấy các ảnh tĩnh nên chuyển động máy quay và nhịp chỉ suy ra được từ chênh lệch giữa các khung. Phần nào suy luận thì ghi "suy luận từ khung hình", không ghi như đã quan sát.

## Bước 2 - Soạn gói câu lệnh cho công cụ tạo video AI (theo video: 1:51-4:39)

Claude viết, PM tự chạy. Mỗi cảnh một câu lệnh, gồm:

- Mô tả cảnh bằng tiếng Anh ngắn (công cụ tạo video thường hiểu tiếng Anh tốt hơn): vật thể, chất liệu, bối cảnh, ánh sáng, góc máy, chuyển động máy, độ dài cảnh.
- Nội dung đã thay bằng chủ đề mới của PM, theo phong cách đã rút ra ở Bước 1.
- **Mô tả kết quả nhìn thấy** (vật thể, chất liệu, ánh sáng, chuyển động), không mô tả kỹ thuật; **nêu phong cách ngay câu đầu**.
- **Dòng chỉ dẫn âm thanh** (theo video): mô tả thiết kế âm thanh mong muốn (tiếng động, nhạc nền nhẹ) **và ghi rõ "no voiceover, no speech, no on-screen text"**. Luôn thêm dòng này vì PM không dùng giọng đọc và chữ sẽ do mã dựng.
- Không đưa người thật có thể nhận ra, logo của bên thứ ba, tên thương hiệu khác vào câu lệnh.

Đầu ra: tệp `CauLenh_CanhXX.md` hoặc một tệp `GoiCauLenh.md` có bảng các cảnh. Kèm hướng dẫn ngắn cho PM: tạo từng cảnh, tải về, đặt tên `canh01.mp4`, `canh02.mp4`... vào thư mục `clip_ai/`.

**Dự toán và làm đợt nhỏ:** kèm gói câu lệnh là bảng dự toán (số cảnh, số lần tạo dự kiến, chi phí hoặc điểm nếu PM biết). Đề nghị PM chạy **đợt nhỏ trước** (2 cảnh), xem chất lượng, chỉnh câu lệnh rồi mới chạy tiếp các cảnh còn lại.

**Dừng cho PM duyệt gói câu lệnh và dự toán** trước khi PM chạy, vì mỗi lần tạo có thể tốn điểm hoặc phí.

## Bước 3 - Nhận clip và dựng phần mã

Khi PM đưa clip:

1. Kiểm tra từng clip: độ dài, khổ hình, có bị chữ hay giọng lạ không. Clip có chữ sai hoặc méo thì báo PM tạo lại cảnh đó.
2. Dựng bằng mã các lớp phủ: tiêu đề, 3 điểm nổi bật, ngày khai giảng, logo, cách đăng ký, khung cuối. Dùng đúng màu, phông, logo theo `video-khoa-hoc`. Chữ chép nguyên văn từ thông tin PM cung cấp.
3. Khung cuối do mã dựng và đứng yên đủ lâu để đọc, vì clip AI thường không giữ được chữ đúng.
4. Áp luật cứng và kiểm tra tự động của `video-khoa-hoc` (mục Cách dựng) cho phần mã lớp phủ; xem ảnh ghép từng cảnh trước khi ghép.

## Bước 4 - Ghép hoàn thiện (theo video: 5:45-6:54)

- **Claude ghép**: trong dự án HyperFrames, mỗi clip AI là một thẻ `<video class="clip">` có `data-start`, `data-duration` trên một dòng, lớp phủ chữ và logo nằm dòng trên; PM mở Studio dời, cắt từng clip được. Thêm nhạc tự tổng hợp bằng mã (không dùng nhạc có bản quyền), tiếng động khớp nhịp theo `video-chuyen-dong` bước 5. Xuất 16:9 và 9:16 nếu cần.
- **PM ghép bằng CapCut**: Claude giao danh sách cảnh theo thứ tự kèm độ dài, tệp lớp phủ dạng PNG hoặc video nền trong suốt (HyperFrames xuất `render --format mov` hoặc `webm` có nền trong suốt), tệp nhạc, và bảng nhịp để PM kéo thả.
- Không có giọng đọc. Nếu PM sau này muốn có lời, phải hỏi lại PM và sửa quy tắc ở `video-chuyen-dong`; nhân bản giọng người thật cần người đó đồng ý rõ ràng.

## Bước 5 - Tái dùng phong cách cho nội dung khác (theo video: 6:54-9:33)

Giữ `phong-cach-<ten>.md`. Khi PM muốn một video khác cùng phong cách: thay kịch bản và thông điệp, để Claude viết lại bộ câu lệnh cho vật thể 3D phù hợp thông điệp mới (ví dụ thay vật thể sản phẩm bằng vật thể gợi khóa học hay AI Lab), rồi lặp Bước 2-4.

## Kiểm tra trước khi giao

- Đối chiếu từng chữ trên màn hình với thông tin PM cung cấp (tên khóa, ngày, học phí, cách đăng ký).
- Rà từng giây bằng một trợ lý con theo `video-khoa-hoc` (mức P0-P2, model `sonnet`, chỉ xem không sửa). Lỗi P0 sửa hết, tối đa 3 vòng.
- Clip AI: xem kỹ tay, ngón, chữ, vật thể biến dạng. Có chi tiết lạ thì tạo lại cảnh đó.
- Nhắc PM video phải qua Marcom hoặc bộ phận truyền thông duyệt trước khi đăng, và cân nhắc ghi chú là nội dung có dùng AI theo quy định của nền tảng đăng.

## Thư mục và tên tệp

`videos/<YYMMDD>_<DuAn>_<TenVideo>/`: `phong-cach-<ten>.md`, `GoiCauLenh.md`, thư mục `clip_ai/` (clip do PM tạo, không đưa lên kho nếu trên 20MB), mã nguồn lớp phủ, `beats.json`, ảnh xem trước. Tệp đặt tên `YYMMDD_<DuAn>_<NoiDung>.ext`.

## Rủi ro cần nói rõ với PM

- Công cụ tạo video AI có thể tốn điểm hoặc phí, PM tự theo dõi. Claude không biết mức giá hiện tại.
- Chất lượng cảnh 3D phụ thuộc công cụ ngoài, có thể phải tạo lại nhiều lần.
- Kỹ năng này chưa chạy thử trên một video thật, sẽ sửa lại sau lần dùng đầu.

## Lỗi hay gặp

Phần dựng bằng mã dùng chung danh sách "Lỗi hay gặp" trong `video-khoa-hoc/SKILL.md`. Riêng clip AI: hay hỏng tay, ngón, chữ và vật thể biến dạng; mỗi cảnh có thể phải tạo lại vài lần. Gặp lỗi riêng của kỹ năng này thì ghi thêm ở đây.

## Gợi ý model

Sonnet 5.5 - high cho phân tích video mẫu và soạn gói câu lệnh. Opus 5.5 - high khi dựng lớp phủ và ghép cả video. Trợ lý con rà từng giây dùng `sonnet`.
