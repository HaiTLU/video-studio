# Mẫu theo loại sản phẩm

Nội dung: Ứng dụng, phần mềm; Hàng hóa vật lý; Dịch vụ; Khóa học; Bài học sau khi đăng.

Mỗi nhóm có: thông tin cần hỏi thêm (ngoài bảng chung ở `SKILL.md`), tài liệu thật cần có, bằng chứng hợp lệ, khung năm nhịp, kỹ thuật hình hợp nhóm, điều cấm. Khung năm nhịp gốc lấy từ bài nguồn (mục 04, viết cho phần mềm); bản cho hàng hóa, dịch vụ, khóa học do Claude chuyển thể theo cách làm quảng cáo phổ biến (xem `NGUON.md`).

Thời lượng ghi cho bản 20 giây ở nhịp 120 (mỗi ô nhịp 2 giây, 10 ô nhịp). Đổi độ dài thì giữ tỷ lệ; nhịp khác thì làm tròn theo ô nhịp.

---

## Ứng dụng, phần mềm

Ví dụ trong kho: SonicRec, web Chuẩn hóa văn bản, web Kế hoạch TTC.

**Hỏi thêm**

| Mục | Ví dụ |
|---|---|
| 8-12 trạng thái giao diện kể được câu chuyện dùng | Mở app, bấm Ghi, đồng hồ chạy, bấm Đánh dấu, Dừng và soạn, trang Word hiện ra |
| Dữ liệu thật hiển thị ở từng trạng thái | Tên cuộc họp mẫu, thời lượng, ba dòng việc cần làm |
| Nền tảng (máy tính, điện thoại, web) | Mac và Windows |
| Trang tải hoặc trang đăng ký | Đường dẫn, mã QR |

**Tài liệu thật**: ảnh chụp màn hình ở độ phân giải gấp 2-3 lần; logo dạng SVG; màu và phông từ CSS của app. Màn hình có tên người, số điện thoại, tên thiết bị: dựng lại bằng HTML dữ liệu mẫu, giữ đúng bố cục, khoảng cách, chữ trên nút.

**Bằng chứng hợp lệ**: số đo tự làm có ghi cách đo ("biên bản 1 giờ họp xong trong 2 phút, đo trên máy Mac M2 ngày ..."); số người dùng, đánh giá cửa hàng ứng dụng có ảnh chụp; lời người dùng thật có đồng ý. Không có thì dùng "kết quả hiện ra trên màn hình" làm bằng chứng.

**Khung năm nhịp**

| Nhịp | Giây | Việc trên hình |
|---|---|---|
| Mở | 0-2 | Nỗi khổ trong 3-5 chữ, chữ lớn động; hoặc kết quả cuối (tệp Word đầy chữ) bật ra trước |
| Sản phẩm xuất hiện | 2-6 | Giao diện tự lắp từng mảnh: khung cửa sổ, thanh bên, nút chính; logo nhỏ ở góc app, không phải góc video |
| Ba điều làm được | 6-14 | Con trỏ thật làm ba việc, mỗi việc hai ô nhịp; máy quay phóng vào vùng đang thay đổi |
| Bằng chứng | 14-16 | Một con số có nguồn, hoặc kết quả cuối phóng to đọc được |
| Kết | 16-20 | Logo, lời kêu gọi ("Dùng thử 30 ngày"), đường dẫn hoặc QR; đứng yên ít nhất 2,5 giây |

**Kỹ thuật hình hợp nhóm** (bài nguồn, mục 06, và hai mẫu @twoclipping, @verbove):

- **Một khối không cắt**: một phần tử duy nhất đổi kích thước, bo góc, màu qua từng trạng thái (nút, thanh tải, dấu tích, thẻ, biểu đồ, bảng lệnh), nội dung bên trong đổi sau một lớp mờ ngắn.
- **Con trỏ điều khiển mọi thay đổi** bằng bấm, gõ, kéo thật. Khi giữ chuột kéo, giá trị tính theo vị trí con trỏ; thả ra thì lò xo về từ chỗ đang đứng.
- Chữ trong khối đang đổi hình vào sau khi khối bắt đầu đổi, ra trước lần đổi kế tiếp.
- Thanh chỉ thẻ (tab) cho hai cạnh hai lò xo khác nhau để nó giãn khi chạy.
- Máy quay phóng để mỗi trạng thái lấp đầy khung.
- Khung cuối bằng khung đầu (kể cả vị trí và vận tốc con trỏ) khi đăng dạng lặp.

**Cấm**: vẽ màn hình không có trong app; tính năng chưa phát hành (kiểm bản đang phát hành, như SonicRec kiểm trang hướng dẫn cài v2.11); giao diện giả kiểu "bảng điều khiển chung chung"; con trỏ di chuyển thẳng đều như máy.

---

## Hàng hóa vật lý

Ví dụ trong kho: giấy thơm quần áo Bounce, đồ Kirkland, Denkmit của shop CombiHome trên Shopee.

**Hỏi thêm**

| Mục | Ví dụ |
|---|---|
| Quy cách, biến thể, giá | Bounce hộp 80 tờ 279.000 đồng; hộp 120 tờ 379.000 đồng |
| Dùng thế nào, trong mấy bước | Bỏ một tờ vào máy sấy cùng quần áo |
| Trước và sau khi dùng | Quần áo bị tĩnh điện, dính lông; sau khi dùng mềm, thơm |
| Nguồn gốc, giấy tờ | Hàng nhập từ Mỹ, có tem phụ tiếng Việt (PM xác nhận) |
| Điểm bán | Shop Shopee, mã giảm giá, chương trình 11.11 |
| Uy tín shop (nếu dùng làm bằng chứng) | Số sao, số đơn, nhãn Shop Yêu Thích, kèm ảnh chụp trang |

**Tài liệu thật**: ảnh tự chụp, nền trơn sáng, ánh sáng đều. Danh sách góc nhờ PM chụp:

1. Mặt trước hộp, thẳng góc, đủ chữ trên nhãn.
2. Mặt sau và nhãn phụ tiếng Việt.
3. Góc nghiêng 3/4 thấy hai mặt hộp.
4. Sản phẩm bên trong (tờ giấy, viên, chai) đặt cạnh hộp.
5. Đang dùng: tay cầm, bỏ vào máy, xịt, rót.
6. Kết quả: quần áo gấp gọn, mặt bàn sạch.
7. Gói hàng của shop (hộp giao, lớp bọc) nếu muốn nói về đóng gói.

Ảnh cắt nền thì giữ bóng đổ thật hoặc vẽ bóng mềm dưới đáy, không để vật lơ lửng. Không có ảnh thật thì dừng, không thay bằng ảnh tạo bởi AI hay ảnh quảng cáo của hãng.

**Bằng chứng hợp lệ**: số sao và số đơn đọc từ trang shop (ghi ngày chụp); hình trước và sau tự chụp; thông số in trên bao bì (số tờ, dung tích); giấy tờ nhập khẩu. Không dùng lời hãng quảng cáo ở nước ngoài như bằng chứng của shop.

**Khung năm nhịp**

| Nhịp | Giây | Việc trên hình |
|---|---|---|
| Mở | 0-2 | Tình huống quen thuộc: áo dính lông, đồ sấy xong bị tĩnh điện; vẽ bằng hình khối hoặc ảnh thật, chữ 3-5 từ |
| Sản phẩm xuất hiện | 2-6 | Hộp rơi vào khung đúng nhịp mạnh, nảy nhẹ một lần, xoay 3/4 lộ nhãn; tên sản phẩm và quy cách hiện cạnh hộp |
| Cách dùng và lợi ích | 6-14 | Ba bước hoặc ba lợi ích, mỗi cái hai ô nhịp: ảnh đang dùng, biểu tượng đơn giản, chữ ngắn; so trước và sau bằng thanh trượt chia đôi màn hình |
| Bằng chứng | 14-16 | Số sao, số đơn của shop, hoặc nhãn phụ tiếng Việt phóng to |
| Kết | 16-20 | Giá, biến thể, "Mua tại shop CombiHome trên Shopee", mã giảm giá nếu có; hộp đứng yên giữa khung |

**Kỹ thuật hình hợp nhóm**:

- Ảnh cắt nền đặt lên nền trơn; chuyển động bằng lò xo nặng (vật có khối lượng), không trôi nổi.
- Giả 3D bằng hai đến ba lớp ảnh trượt khác tốc độ (thị sai); cần xoay thật thì dựng hộp bằng three.js dán ảnh từng mặt lên khối.
- Thanh trượt trước và sau: một đường dọc kéo qua ảnh, con trỏ hoặc ngón tay kéo, tiếng lướt khi kéo.
- Nhãn giá là một thành phần dùng lại: khối bo góc màu nhấn, số giá bật theo nhịp.
- Khổ dọc 9:16 là chính (Shopee Video, TikTok); bố cục để nút "Mua" của nền tảng không che giá.

**Cấm**: nói công dụng không ghi trên bao bì (ví dụ "diệt khuẩn" khi nhãn không ghi); dùng ảnh, video, nhạc quảng cáo của hãng; so sánh với sản phẩm hãng khác; "hàng chính hãng" khi PM chưa xác nhận có giấy tờ; nhắc giá gốc gạch bỏ khi không có giá bán thật trước đó.

---

## Dịch vụ

Ví dụ trong kho: đào tạo AI cho doanh nghiệp, tư vấn, hợp tác của TTC; dịch vụ cài đặt SonicRec.

**Hỏi thêm**

| Mục | Ví dụ |
|---|---|
| Khách nhận được gì cụ thể (đầu ra có thể chụp được) | Bộ quy trình, báo cáo, nhân viên dùng được công cụ sau 2 buổi |
| Quy trình mấy bước, mỗi bước bao lâu | Khảo sát 1 tuần, đào tạo 2 buổi, theo dõi 1 tháng |
| Ai làm (đơn vị, chuyên môn) | Giảng viên Trường Đại học Thăng Long |
| Kết quả của khách cũ (có đồng ý) | Số giờ tiết kiệm, ảnh buổi học, lời nhận xét có ký tên |
| Cách liên hệ | Số điện thoại, biểu mẫu, Zalo |

**Tài liệu thật**: ảnh hoặc đoạn quay buổi làm việc thật (người trong hình đã đồng ý); sản phẩm đầu ra đã che thông tin khách; logo khách chỉ khi có đồng ý bằng văn bản.

**Bằng chứng hợp lệ**: kết quả đo được của khách cũ, có đồng ý; số khóa, số học viên đã làm (từ báo cáo của đơn vị); chứng nhận, giấy phép hoạt động.

**Khung năm nhịp** (dịch vụ không có "vật" để cho xem, nên cho xem **quy trình và đầu ra**):

| Nhịp | Giây | Việc trên hình |
|---|---|---|
| Mở | 0-2,5 | Câu hỏi đúng nỗi lo của người mua ("Nhân viên chưa ai dùng AI?") |
| Lời hứa | 2,5-5 | Một câu hứa cụ thể, đo được, kèm thời gian |
| Quy trình | 5-13 | Đường đi ba bước: một dải thời gian hoặc một khối đi qua ba trạm, mỗi trạm hiện đầu ra của bước đó |
| Bằng chứng | 13-16 | Kết quả của khách cũ, hoặc con số của đơn vị, có nguồn |
| Kết | 16-20 | Logo, "Đặt lịch tư vấn", cách liên hệ |

**Kỹ thuật hình hợp nhóm**: dải thời gian hoặc bản đồ đường đi; mỗi trạm là thẻ đổi hình (cùng kỹ thuật "một khối không cắt"); đầu ra hiện bằng ảnh thật trong khung giấy hoặc màn hình.

**Cấm**: cam kết kết quả tuyệt đối ("tăng gấp đôi doanh thu"); dùng tên, logo, ảnh khách khi chưa có đồng ý; ảnh nhân viên mẫu lấy từ kho ảnh làm như người thật của đơn vị.

---

## Khóa học

Ví dụ trong kho: khóa ngắn hạn TTC (tiếng Anh giao tiếp, kỹ năng y tế cơ bản, ACCA, Tester), lớp trải nghiệm âm nhạc.

Khóa TTC đúng khuôn 20 giây có sẵn (câu mở, 3 tình huống, 3 điểm nổi bật, lịch, đăng ký) thì dùng `video-khoa-hoc`, không dùng mục này. Mục này dành cho khóa cần câu chuyện khác: ra mắt chương trình mới, khóa cho doanh nghiệp, khóa trực tuyến.

**Hỏi thêm**: tên khóa, đầu ra người học làm được sau khóa (động từ cụ thể), lịch, hình thức, học phí, chứng chỉ, giảng viên (có đồng ý dùng tên, ảnh), sản phẩm học viên làm trong khóa.

**Tài liệu thật**: ảnh lớp học thật, sản phẩm học viên (đã xin phép), mẫu chứng chỉ đã che tên, logo Trường theo `video-khoa-hoc`.

**Bằng chứng hợp lệ**: số khóa, số học viên đã học (từ báo cáo TTC); sản phẩm học viên thật; nhận xét học viên có đồng ý. Không dùng "cam kết việc làm", "đảm bảo đỗ".

**Khung năm nhịp**

| Nhịp | Giây | Việc trên hình |
|---|---|---|
| Mở | 0-2 | Khoảnh khắc người học muốn có ("Tự tin trình bày bằng tiếng Anh") hoặc nỗi lo hiện tại |
| Khóa học xuất hiện | 2-5 | Tên khóa, logo Trường, hình thức học |
| Trước và sau khóa | 5-13 | Ba việc người học làm được sau khóa, mỗi việc kèm một sản phẩm hoặc tình huống thật |
| Bằng chứng | 13-15,5 | Chứng chỉ mẫu, số học viên, sản phẩm học viên |
| Kết | 15,5-20 | Khai giảng, học phí, cách đăng ký; đứng yên đủ lâu |

**Cấm**: theo `video-khoa-hoc` (không lời hứa không có thật, tên khóa, ngày, học phí khớp nguyên văn); nhận diện màu và phông ĐHTL bắt buộc.

---

## Bài học sau khi đăng

Ghi theo nhóm sản phẩm, mỗi bài học kèm số video đã so và nguồn số liệu (Bước 9). Chưa đủ 3 video thì ghi "chưa đủ để kết luận".

- Ứng dụng: (chưa có)
- Hàng hóa: (chưa có)
- Dịch vụ: (chưa có)
- Khóa học: (chưa có)
