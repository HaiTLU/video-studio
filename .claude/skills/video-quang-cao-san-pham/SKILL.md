---
name: video-quang-cao-san-pham
description: Lên kịch bản và làm video quảng cáo cho bất kỳ sản phẩm nào (ứng dụng, phần mềm, hàng hóa vật lý, dịch vụ, khóa học), dựng bằng mã. Gom thông tin và tài liệu thật, chọn khung câu chuyện theo loại sản phẩm, viết kịch bản dạng danh sách trạng thái trên lưới nhịp, dừng cho PM duyệt, chuyển phần dựng hình sang kỹ năng dựng, rồi chấm theo tiêu chí của một quảng cáo. Dùng khi PM gõ /video-quang-cao-san-pham hoặc nhờ "làm video quảng cáo sản phẩm", "video bán hàng", "video ra mắt app", "video giới thiệu sản phẩm", "viết kịch bản quảng cáo", "video Shopee, TikTok cho món hàng". Video quảng cáo khóa ngắn hạn TTC theo khuôn 20 giây có sẵn thì dùng /video-khoa-hoc; video giới thiệu đơn vị, hội thảo, phòng thí nghiệm (không bán gì) thì dùng /video-chuyen-dong.
---

# Video quảng cáo sản phẩm

Nội dung: Ý chính; Các tệp trong kỹ năng; Quy trình bước 0 đến 9 (nhận việc, gom thông tin, gom tài liệu, chọn khung, kịch bản, bản chỉ đạo, dựng, chấm, giao, đo); Thư mục; Lỗi hay gặp; Gợi ý model.

Kỹ năng này lo phần "quảng cáo": bán cái gì, cho ai, chứng minh bằng gì, mời làm gì, và kịch bản từng nhịp. Phần dựng hình bằng mã (HyperFrames, lò xo, `beats.json`, xuất MP4, rà từng giây) đã có ở các kỹ năng dựng; ở đây chỉ trỏ tới, không chép lại.

Nguồn chính: khóa học 12 bước "How to build motion design studio with Opus 5.5" của @0xMovez trên X (27/9/2026) và các bài mẫu khóa học dẫn. Quy tắc nào lấy từ bài, quy tắc nào do Claude thêm theo cách làm quảng cáo phổ biến: xem `NGUON.md`. Các con số lượt xem, chi phí, thời gian làm trong bài là lời tác giả, không dùng làm căn cứ.

## Ý chính

- Câu lệnh chỉ quyết định khoảng một phần mười video, phần còn lại là khung làm việc (lời tác giả bài nguồn). Khung đó gồm: tài liệu thật, kịch bản theo nhịp, luật cấm kiểu đồ họa sáo rỗng, âm thanh, và vòng tự xem lại khung hình.
- Câu lệnh một dòng chỉ thử được bộ dựng, không thử được ý tưởng vì nó không chứa ý tưởng nào. Hàng trăm người dùng cùng một câu lệnh thì ra hàng trăm video na ná nhau. Không làm quảng cáo từ câu lệnh một dòng.
- Một quảng cáo trả lời đủ năm câu: người xem gặp vấn đề gì, sản phẩm là gì, nó làm được gì (cho thấy, không kể), bằng chứng nào, giờ bấm vào đâu.

## Các tệp trong kỹ năng

| Tệp | Đọc khi nào |
|---|---|
| `theo-loai-san-pham.md` | Bước 1-3: thông tin cần hỏi, tài liệu thật, bằng chứng, khung câu chuyện, điều cấm cho từng nhóm (ứng dụng, hàng hóa, dịch vụ, khóa học) |
| `mau-kich-ban.md` | Bước 4-5: mẫu kịch bản dạng danh sách trạng thái, câu lệnh giao bộ dựng, mẫu bản chỉ đạo dài |
| `cham-diem.md` | Bước 7: khổ và vùng an toàn, lệnh tạo ảnh ghép, câu lệnh tự phê bình, thang điểm, mức lỗi |
| `giong-doc-linh-vat.md` | Khi PM chọn có giọng đọc hoặc nhân vật linh vật |
| `vi-du/` | Kịch bản đã điền cho SonicRec (ứng dụng) và Bounce của CombiHome (hàng hóa) |
| `NGUON.md` | Nguồn từng quy tắc, giấy phép, đường dẫn bài gốc |

## Quy trình

Không bỏ bước. Mỗi chỗ ghi **Dừng** là hỏi PM bằng hộp thoại (`AskUserQuestion`) rồi mới đi tiếp.

### Bước 0 - Nhận việc

Xác định bốn điều; điều nào chưa rõ thì đưa vào hộp hỏi ở Bước 1:

1. **Loại sản phẩm**: ứng dụng/phần mềm, hàng hóa vật lý, dịch vụ, khóa học. Sản phẩm lai (phần mềm kèm dịch vụ cài đặt) thì chọn loại của thứ khách trả tiền nhiều nhất.
2. **Mục tiêu**: ra mắt (người xem chưa biết sản phẩm), bán (đã biết, cần lý do mua ngay), nhắc lại (đã xem, cần ưu đãi). Mục tiêu quyết định lời kêu gọi ở nhịp cuối.
3. **Nơi đăng**: TikTok, Reels, Shorts, Shopee Video (dọc 9:16); Facebook, Zalo (1:1 hoặc 4:5); YouTube, trang web, màn hình hội trường (16:9).
4. **Độ dài**: mặc định 20 giây. 15 giây cho quảng cáo trả tiền; 30-45 giây khi cần cho thấy quy trình (dịch vụ) hoặc nhiều tính năng; trên 45 giây thì làm thêm theo mục "Video dài hơn 30 giây" của `video-chuyen-dong`.

Khóa ngắn hạn TTC đúng khuôn 20 giây (khai giảng, học phí, đăng ký): chuyển sang `video-khoa-hoc`; chỉ lấy phần khóa học trong `theo-loai-san-pham.md` khi cần khung câu chuyện khác.

### Bước 1 - Gom thông tin

Bảng chung cho mọi sản phẩm dưới đây; bảng riêng từng nhóm ở `theo-loai-san-pham.md`. Thiếu mục nào thì gộp vào **một** hộp hỏi (tối đa 4 câu; câu nào phụ thuộc câu trước thì để hộp sau). Không tự bịa.

| Mục | Ví dụ |
|---|---|
| Tên sản phẩm, đường dẫn | SonicRec, trang tải của SonicRec |
| Người mua là ai | Thư ký cuộc họp ở trường học, công ty nhỏ |
| Vấn đề của họ, bằng lời của họ | "Họp xong mất cả buổi chiều gõ biên bản" |
| Một câu sản phẩm hứa | Họp xong là có biên bản |
| Ba điều sản phẩm làm được (có thật, quay hoặc chụp được) | Ghi âm, đánh dấu chỗ quan trọng, ra tệp Word |
| Một bằng chứng có nguồn | Số đo, đánh giá, số lượng bán, chứng nhận; ghi nguồn |
| Lời kêu gọi và nơi đến | "Dùng thử 30 ngày" và đường dẫn hoặc mã QR |
| Giá hoặc ưu đãi (không bắt buộc) | 50.000 đồng/tháng |
| Nhận diện | Màu, phông, logo; sản phẩm của Trường thì theo `video-khoa-hoc` |
| Video hoặc ảnh mẫu PM thích (không bắt buộc) | Tệp hoặc đường dẫn; chỉ học cách làm |
| Điều không muốn (không bắt buộc) | Không nền đỏ, không chữ chạy |
| Giọng đọc, linh vật | Mặc định không; có thì đọc `giong-doc-linh-vat.md` |

**Luật nội dung (luật cứng):**

- Mọi con số, lời khen, đánh giá, số khách phải do PM đưa và có nguồn. Không có nguồn thì bỏ nhịp bằng chứng, thay bằng cảnh cho thấy sản phẩm đang làm việc. Không bịa số.
- Không dùng "nhất", "duy nhất", "tốt nhất", "số một" hoặc từ cùng nghĩa khi không có tài liệu chứng minh (Luật Quảng cáo 2012, Điều 8 khoản 11). Không so sánh trực tiếp với sản phẩm cùng loại của người khác (Điều 8 khoản 9). Luật đã có sửa đổi; kiểm bản hiện hành trước khi đăng quảng cáo trả tiền.
- Thực phẩm, mỹ phẩm, thuốc, thiết bị y tế, dịch vụ giáo dục có điều kiện riêng về nội dung quảng cáo: nhắc PM kiểm với pháp chế hoặc truyền thông trước khi đăng.
- Ảnh người thật, giọng người thật, logo hãng khác: chỉ dùng khi có quyền. Hàng nhập khẩu bán lại (Bounce, Kirkland) dùng ảnh tự chụp, không lấy ảnh quảng cáo của hãng.

### Bước 2 - Gom tài liệu thật

Nguyên tắc từ bài nguồn: **không vẽ lại sản phẩm theo trí tưởng tượng; cắt và làm chuyển động chính thứ thật.**

1. Lưu mọi thứ vào `assets/` trong thư mục video. **Liệt kê cho PM xem trước khi làm chuyển động** (tên tệp, nội dung, kích thước, nguồn).
2. Ứng dụng: chụp màn hình thật bằng `playwright-cli` ở độ phân giải gấp 2-3 lần khung xuất để chữ không vỡ khi phóng (video SonicRec đầu tiên bị mờ vì phóng đoạn quay 1312 điểm ảnh). Màn hình có thông tin cá nhân thì dựng lại giao diện bằng HTML với dữ liệu mẫu, giữ đúng bố cục thật.
3. Hàng hóa: ảnh tự chụp, nền trơn, đủ góc theo danh sách trong `theo-loai-san-pham.md`. Thiếu ảnh thì **dừng**, nhờ PM chụp theo danh sách đó.
4. Dịch vụ, khóa học: ảnh hoặc đoạn quay buổi làm việc thật, sản phẩm đầu ra (báo cáo, chứng chỉ mẫu đã che tên), lịch, địa điểm.
5. Màu và phông: lấy từ trang web hoặc bộ nhận diện của sản phẩm (đọc CSS, tệp phông). Phông phải có dấu tiếng Việt; kiểm khung đầu trước khi dựng tiếp.
6. Khóa API (giọng đọc, tạo ảnh) để trong biến môi trường do PM tự lưu; bản chỉ đạo chỉ ghi tên biến.

### Bước 3 - Chọn khung câu chuyện và phong cách

1. Lấy khung năm nhịp của nhóm sản phẩm trong `theo-loai-san-pham.md`. Khung gốc (bài nguồn, mục 04), thời lượng cho bản 20 giây:

   | Nhịp | Việc | Giây |
   |---|---|---|
   | Mở | Vấn đề trong tối đa 5 chữ, chữ rất to và động | 0-2,5 |
   | Sản phẩm xuất hiện | Sản phẩm tự lắp ráp từng phần trên màn hình | 2,5-6 |
   | Ba điều làm được | Mỗi điều là một khoảnh khắc thật: con trỏ bấm, tay dùng, kết quả hiện ra | 6-14 |
   | Bằng chứng | Một con số hoặc một kết quả có nguồn | 14-16,5 |
   | Kết | Logo, lời kêu gọi, nơi đến; đứng yên đủ lâu để đọc | 16,5-20 |

2. **Phác ba phương án mở đầu khác hẳn nhau**: mở bằng vấn đề, mở bằng kết quả, mở bằng một hành động lạ mắt của sản phẩm. Mỗi phương án một dòng mô tả và một khung phác. Hai giây đầu quyết định người xem có ở lại không, nên PM chọn, Claude không tự chọn.
3. Phong cách: làm như Bước 1 của `video-chuyen-dong` (3 phong cách hợp nhất từ danh mục lemo-opuscar, mẫu Skillry gần nhất, thêm "Theo video mẫu" nếu PM có). Riêng ứng dụng, đưa thêm lựa chọn "Một khối đổi hình xuyên suốt" (bài nguồn, mục 06): cả video là một phần tử đổi cỡ, bo góc, màu qua từng trạng thái, con trỏ điều khiển, không cắt cảnh, khung cuối bằng khung đầu.
4. Có video mẫu: tách khung mỗi 0,5 giây, viết `docs/style_guide.md` (màu mã hex, kiểu chữ, độ dài cảnh, kiểu chuyển cảnh, chuyển động máy quay, hạt nhiễu, cách chữ vào và ra). Chỉ lấy ngữ pháp của mẫu, không lấy nội dung, logo, nhân vật.
5. **Dừng**: một hộp gồm phương án mở đầu, phong cách, và nhịp nhạc nếu chưa rõ.

### Bước 4 - Viết kịch bản dạng danh sách trạng thái

Đây là phần viết kịch bản của kỹ năng. Mẫu đầy đủ ở `mau-kich-ban.md`. Tóm tắt:

- Viết danh sách **trạng thái** trên lưới nhịp, không viết cảm hứng chung chung ("năng động, hiện đại"). Mỗi nhịp có một việc xảy ra trên hình; không có nhịp chết.
- Mỗi dòng ghi: thời điểm (giây, ô nhịp, nhịp), trạng thái trên hình (vật gì, ở đâu, đang làm gì), chữ trên màn hình (nguyên văn), chuyển động (vào, đứng, ra, loại lò xo), âm thanh (tiếng gì gắn với hành động nào), tài liệu thật dùng trong khung (tên tệp ở `assets/`).
- Kèm danh sách thành phần dùng lại (nút, thẻ, con trỏ, khung điện thoại, nhãn giá), luật hình, và các bẫy kỹ thuật đã biết.
- Kiểm thời gian đọc: mỗi dòng chữ đứng yên ít nhất (số ký tự chia 15) cộng 1,5 giây (công thức trong `video-khoa-hoc`). Tối đa 8 từ một dòng. Chữ không nằm trong vùng giao diện nền tảng che (`cham-diem.md`).
- Lưu `YYMMDD_<DuAn>_KichBan_<TenVideo>_v1.md` trong thư mục dự án.
- **Dừng**: gửi PM kịch bản kèm ảnh ghép một khung phác cho mỗi nhịp lớn. PM duyệt rồi mới viết mã.

### Bước 5 - Bản chỉ đạo cho bộ dựng

- Video đến 30 giây, một phiên: dùng "Câu lệnh giao bộ dựng" trong `mau-kich-ban.md`, gắn kịch bản đã duyệt.
- Video dài, nhiều phiên hoặc chia trợ lý con: dùng mẫu bản chỉ đạo dài trong cùng tệp.
- Ghi `docs/motion.md` (khung, số khung mỗi giây, màu, các loại lò xo, nhịp, hạt giống nhiễu) theo `video-chuyen-dong`. Video thứ hai cùng nhãn hiệu đọc lại tệp này và dùng lại thư mục cũ: bộ dựng, nhạc, xuất tệp đã có nên nhanh hơn nhiều.

### Bước 6 - Dựng

Chuyển sang kỹ năng dựng, giữ nguyên kịch bản đã duyệt:

| Trường hợp | Kỹ năng dựng |
|---|---|
| Mặc định: hình phẳng, giao diện, chữ động, hàng hóa dạng ảnh cắt nền | `video-chuyen-dong` Bước 4-6: dự án HyperFrames (`video-khoa-hoc/dung-hyperframes.md`), mỗi nhịp lớn một cảnh con, `beats.json`, tiếng động theo `events.json` |
| Khóa ngắn hạn TTC | `video-khoa-hoc` |
| Cần vật thể 3D (máy tính, hộp sản phẩm xoay, logo đùn khối) | three.js trong dự án HyperFrames (HyperFrames tua sẵn three.js, xem `hyperframes-animation/adapters/`); hoặc `video-3d-theo-mau` khi theo mẫu và PM tự chạy công cụ tạo video AI |
| Video hướng dẫn có quay màn hình, phụ đề, nhiều bản theo lô | HyperFrames: phụ đề theo `embedded-captions`, nhiều bản theo lô bằng biến và `render --batch`. Dự án Remotion cũ ở kho sonicrec-congty muốn chuyển sang thì theo `remotion-to-hyperframes` |

Quy tắc riêng cho quảng cáo khi dựng:

- **Mọi khổ từ một dòng thời gian.** Viết cảnh theo hàm bố cục (vị trí tính theo khổ), không theo điểm ảnh cố định. Xuất 9:16, 1:1, 16:9 từ cùng mã; sắp lại chữ và giao diện cho từng khổ, không cắt bản 16:9 thành dọc.
- **Lò xo theo loại vật** (bài nguồn, mục 08): nút, công tắc, cạnh dẫn thì cứng, nảy rất nhẹ; thẻ, khung chứa, máy quay thì vừa; chữ lớn, vật 3D, logo thì nặng, không nảy; linh vật, nhãn dán thì nảy rõ.
- **Luật hình cấm**: tiêu đề giữa màn hình trên nền chuyển màu; mọi thứ mờ dần hiện ra; nhãn chữ ở góc, viền khung; phát sáng trên giao diện; chùm hạt bung chung chung; chuyển thẳng từ nền tối sang màu nhấn; khoảng chết không có gì xảy ra; chữ phóng to bị mờ (không dùng `will-change` cho thứ máy quay phóng).
- **Âm thanh**: nhạc tự tổng hợp hoặc nhạc PM có quyền dùng. Nhịp mạnh cho khoảnh khắc lớn, nhịp thường cho đổi trạng thái, đỉnh âm cho tiếng động. Chuẩn hóa -14 LUFS. Video quảng cáo phải hiểu được khi tắt tiếng: mọi thông điệp chính có chữ trên hình.

### Bước 7 - Chấm điểm như một quảng cáo

Làm theo `cham-diem.md`:

1. Tạo ảnh ghép (2 khung mỗi giây), dải 12 khung quanh động tác nhanh, ảnh xem ở bề ngang 360 điểm ảnh, ảnh có lớp phủ vùng an toàn của nền tảng.
2. Tự chấm 8 tiêu chí thang 10 với vai "đạo diễn khó tính, không phải tác giả tự hào". Ghi 3 lỗi lớn nhất kèm giây vào `docs/review_log.md`, sửa, dựng lại đúng đoạn lỗi. Tối đa 3 vòng; hết 3 vòng còn tiêu chí dưới 8 thì báo PM.
3. Rà từng giây P0-P2 bằng trợ lý con `ra-soat-video` (model `sonnet`) theo `video-khoa-hoc`, cộng các lỗi P0 riêng của quảng cáo trong `cham-diem.md`.
4. Video đăng dạng lặp: phát nối hai lần, xem chỗ nối.

### Bước 8 - Giao

- Tệp: `<TenVideo>_9x16.mp4`, `_1x1.mp4`, `_16x9.mp4` (theo khổ đã chọn), ảnh đại diện, ảnh ghép, kịch bản, `review_log.md`, mã nguồn kèm `README.md` ghi cách đổi giá, ngày, lời kêu gọi rồi dựng lại.
- Tin báo PM: đường dẫn tệp, điểm vòng cuối, lỗi P1-P2 còn lại, điều sẽ làm tốt hơn ở bản sau.
- Nhắc PM: quảng cáo của Trường qua bộ phận truyền thông duyệt; quảng cáo trả tiền kiểm chính sách nền tảng; nhóm hàng có điều kiện kiểm pháp chế.

### Bước 9 - Đo sau khi đăng

Theo mục "Đo hiệu quả sau khi đăng" của `video-khoa-hoc`, thêm hai cột "Mục tiêu" (ra mắt, bán, nhắc lại) và "Phương án mở đầu". Có từ 3 video cùng nhãn hiệu thì so phương án mở đầu với tỷ lệ người xem qua giây thứ 3 và lượt bấm. Bài học ghi vào cuối `theo-loai-san-pham.md`, đúng nhóm sản phẩm.

## Thư mục và tên tệp

- Sản phẩm có thư mục dự án: `videos/<YYMMDD>_<DuAn>_<TenVideo>/`; việc cá nhân như CombiHome: `02_Areas/Shopee/Video_<TenVideo>/`.
- Bên trong: `assets/`, `docs/` (style_guide, kịch bản, motion.md, review_log), `out/`, mã nguồn.
- Video trên 20MB không đưa lên kho, chỉ giữ mã nguồn, kịch bản, ảnh xem trước.

## Lỗi hay gặp

Phần dựng dùng chung "Lỗi hay gặp" của `video-khoa-hoc` và `video-chuyen-dong`. Lỗi riêng của quảng cáo ghi thêm ở đây khi gặp.

- **Đường dẫn kho có dấu tiếng Việt ở dạng tách dấu (NFD):** công cụ Write báo "another spelling" khi ghi vào kho; soạn tệp ở thư mục tạm rồi chép bằng lệnh (gặp 5/10/2026 khi tạo kỹ năng này).

Từ lần dựng thử đầu tiên (video Chuẩn hóa văn bản, 5/10/2026, `01_Projects/Web_ChuanHoaVanBan/Video_QuangCao/`):

- **Ứng dụng cần đăng nhập:** Claude không nhập mật khẩu thay PM. Hỏi PM chọn: PM tự đăng nhập trong trình duyệt để Claude chụp, PM gửi ảnh chụp, hoặc dựng lại giao diện từ mã nguồn (chữ trên nút chép nguyên văn từ mã, màu và phông từ CSS, dữ liệu mẫu). Lần đầu PM chọn dựng lại từ mã nguồn.
- **Canvas không xuất được ảnh** ("Tainted canvases may not be exported") khi vẽ ảnh tải từ `file://`: nhúng ảnh dạng chuỗi base64 trong một tệp `.js`, hoặc mở trang qua máy chủ cục bộ.
- **Phông có bản quyền của hệ điều hành** (Times New Roman, Arial): khai báo `src: local("Times New Roman")`, không chép tệp phông vào kho.
- **Mốc của con trỏ trong `track()` là lúc bắt đầu đi, không phải lúc tới nơi.** Lò xo con trỏ 260/30 cần khoảng 0,4 giây để tới. Muốn nắm một vật ở giây 4,5 thì đặt mốc tới vật ở giây 4,05; vật bám con trỏ bằng lò xo, không gắn cứng (gắn cứng làm vật nhảy cóc).
- **Kho bỏ qua `*.png` và `*.mp4`:** video và ảnh xem trước không lên git; để ở `xem-truoc/` trên Drive (thư mục chính, không chỉ trong worktree). Thư mục `out/` của một số dự án cũng bị bỏ qua.
- **Thư mục video nằm trong thư mục gốc của ứng dụng triển khai trên Vercel:** mỗi lần sửa video làm Vercel dựng lại. Thêm `.vercelignore` loại thư mục video.
- **Trợ lý con `ra-soat-video` có thể không được nạp trong phiên:** dùng trợ lý chung, model `sonnet`, với cùng lời dặn (chỉ xem, tệp tạm ở `/tmp`, trả lỗi theo P0-P2).
- **Sửa mã bằng thay chuỗi:** chuỗi cần thay nằm vắt hai dòng thì lệnh thay không báo lỗi mà bỏ qua; kiểm lại bằng `grep` mốc cũ sau khi sửa và dựng lại dải khung quanh chỗ sửa.

## Gợi ý model

- Kịch bản, bản chỉ đạo (Bước 0-5): Opus 5.5 hoặc opusplan, mức high.
- Dựng bản mới: Opus 5.5 mức high; ba giây đầu của video ra mắt quan trọng thì mức cao nhất có.
- Sửa nhỏ và dựng lại: Sonnet 5.5 mức medium.
- Rà từng giây: trợ lý con `sonnet`.
