# Mẫu kịch bản và bản chỉ đạo

Nội dung: Mẫu 1 Kịch bản danh sách trạng thái; Mẫu 2 Câu lệnh giao bộ dựng (đến 30 giây); Mẫu 3 Bản chỉ đạo dài (trên 30 giây); cuối tệp: Ghép tạo rồi vẽ đè.

Ba mẫu: (1) kịch bản dạng danh sách trạng thái, dùng cho mọi video; (2) câu lệnh giao bộ dựng cho video ngắn; (3) bản chỉ đạo dài cho video nhiều phiên. Cấu trúc học từ bài nguồn (mục 04, 06, 10) và hai mẫu công khai của @twoclipping, @verbove; câu chữ viết lại bằng tiếng Việt, không chép nguyên văn.

Vì sao viết trạng thái chứ không viết cảm hứng: lời như "năng động, cao cấp" để bộ dựng tự đoán, và nó đoán về kiểu mặc định (chữ giữa nền chuyển màu, mọi thứ mờ dần hiện ra). Một danh sách trạng thái cho bộ dựng biết từng khung phải có gì, nên kết quả kiểm được và sửa được từng dòng.

---

## Mẫu 1 - Kịch bản dạng danh sách trạng thái

Lưu thành `YYMMDD_<DuAn>_KichBan_<TenVideo>_v1.md`. Điền đủ các phần; phần nào không áp dụng thì ghi "không".

```markdown
# Kịch bản: <tên video>

## Đầu vào
- Sản phẩm: <tên> (<đường dẫn>), nhóm: <ứng dụng | hàng hóa | dịch vụ | khóa học>
- Người mua: <ai>; vấn đề bằng lời của họ: "<...>"
- Lời hứa một câu: <...>
- Mục tiêu: <ra mắt | bán | nhắc lại>; nơi đăng: <...>; khổ: <9:16, 1:1, 16:9>; độ dài: <giây>
- Bằng chứng: <con số hoặc kết quả> - nguồn: <tệp, trang, ngày>
- Lời kêu gọi: "<...>" -> <đường dẫn, QR, tên shop>
- Phương án mở đầu PM chọn: <vấn đề | kết quả | hành động lạ mắt>
- Phong cách PM chọn: <tên>; mẫu tham chiếu: <tệp hoặc "không">

## Hướng hình
- Nền: <màu hex>; một màu nhấn: <hex>; phông tiêu đề: <...>; phông chữ thường: <...>
- Cách kể: <ví dụ: một khối không cắt, con trỏ điều khiển | hộp sản phẩm rơi vào và xoay | dải thời gian ba trạm>
- Lò xo: <cứng cho nút, vừa cho thẻ, nặng cho chữ lớn và logo>, nảy tối đa <rất nhẹ | không>
- Cấm: <tiêu đề giữa nền chuyển màu, mờ dần hiện ra, nhãn góc, phát sáng, hạt bung, nhịp chết, + điều PM không muốn>

## Âm thanh
- Nhạc: <tự tổng hợp | tệp PM có quyền>, <nhịp>/phút, <số> ô nhịp, bắt đầu ở nhịp mạnh
- Tiếng động: <bấm khi con trỏ nhấn, lướt khi khối đổi hình, thịch khi sản phẩm rơi, ting khi giá hiện>
- Giọng đọc: <không | có, xem phần lời đọc>

## Danh sách trạng thái
| Ô nhịp.nhịp | Giây | Trạng thái trên hình | Chữ (nguyên văn) | Chuyển động | Âm thanh | Tài liệu |
|---|---|---|---|---|---|---|
| 1.1 | 0,0 | <...> | "<...>" | <vào bằng gì, lò xo nào> | <tiếng gì> | assets/<tệp> |
| 1.3 | 1,0 | <...> | | | | |
| ... | | | | | | |
| 10.4 | 19,5 | <khung kết đứng yên> | "<lời kêu gọi>" | <đứng yên> | <hết nhạc> | assets/logo.svg |

## Thành phần dùng lại
<nút, thẻ, con trỏ, khung điện thoại, nhãn giá, thanh trước và sau, ...> - mỗi thành phần một dòng: hình dạng, màu, cỡ, lò xo.

## Kiểm thời gian đọc
| Dòng chữ | Số ký tự | Cần đứng yên (giây) | Thực có (giây) | Đạt |
|---|---|---|---|---|

## Bẫy kỹ thuật
- Không dùng will-change cho thứ máy quay phóng (chữ mờ).
- Khung cuối bằng khung đầu nếu lặp (vị trí và vận tốc con trỏ).
- <bẫy riêng của video này>

## Bắt đầu
Hỏi những đầu vào còn thiếu. Gửi danh sách trạng thái trên lưới nhịp và ảnh phác từng nhịp lớn, chờ PM duyệt rồi mới viết mã.
```

**Cách điền danh sách trạng thái**

- Một dòng cho mỗi việc xảy ra; ít nhất một dòng mỗi nhịp hoặc mỗi nửa ô nhịp. Nhịp không có dòng nào là nhịp chết.
- "Trạng thái trên hình" mô tả kết quả nhìn thấy: vật gì, ở đâu trong khung, cỡ, đang làm gì. Ví dụ tốt: "Nút Ghi đỏ giữa khung, con trỏ từ góc dưới phải đi tới, bấm; nút co lại thành chấm đỏ nhấp nháy cạnh đồng hồ 00:00:01". Ví dụ dở: "Giới thiệu tính năng ghi âm một cách ấn tượng".
- "Chữ" chép nguyên văn, kể cả dấu câu. Chữ do PM đưa thì không sửa.
- Khoảnh khắc lớn (sản phẩm xuất hiện, bằng chứng, logo) đặt ở nhịp đầu ô nhịp (nhịp mạnh).
- Đổi trạng thái đặt ở nhịp; tiếng động đặt ở đỉnh âm đo được, không đặt tay.

---

## Mẫu 2 - Câu lệnh giao bộ dựng (video đến 30 giây)

Dùng khi kịch bản đã duyệt. Viết lại theo kịch bản, không gửi nguyên mẫu trống.

```text
Làm video quảng cáo <độ dài> giây cho <sản phẩm> (<đường dẫn>), năng lượng như đoạn showreel của một nhà thiết kế chuyển động giỏi. Làm hết sức.

Kịch bản đã duyệt: docs/kichban.md. Làm đúng từng dòng của danh sách trạng thái; chỗ nào kịch bản không ghi thì tự quyết nhưng không trái hướng hình.

Tài liệu
- Chỉ dùng tệp trong ./assets (đã liệt kê trong kịch bản). Không vẽ lại giao diện hay sản phẩm theo trí tưởng tượng; cắt và làm chuyển động chính thứ thật.
- Màu, phông, lò xo, nhịp lấy từ docs/motion.md.

Dựng
- Theo kỹ năng video-chuyen-dong: dự án HyperFrames (video-khoa-hoc/dung-hyperframes.md), mỗi nhịp lớn một cảnh con, chuyển động bằng GSAP trên dòng thời gian dừng sẵn; không chuyển tiếp CSS, không hẹn giờ, không giữ trạng thái giữa các khung; nhiễu có hạt giống cố định.
- Lò xo dạng công thức đóng; giá trị đổi đích nhiều lần thì cộng một lò xo cho mỗi lần đổi.
- Vị trí tính theo hàm bố cục để xuất được <các khổ> từ cùng mã.

Âm thanh
- Nhạc <nhịp>/phút tổng hợp bằng mã (hoặc tệp audio/track.wav, đo nhịp bằng beats.py trước). Tiếng động lấy thời điểm từ events.json do chính trang xuất ra.

Trước khi dựng đủ
- Dựng một khung mỗi nhịp thành ảnh ghép, tự xem, chấm theo cham-diem.md, sửa 3 lỗi tệ nhất, lặp tới khi mọi tiêu chí từ 8 trở lên (tối đa 3 vòng). Gửi ảnh ghép và điểm cho tôi rồi mới dựng đủ.
```

Lý do một số câu (bài nguồn, mục 03): gọi tên một thể loại người xem đã quen ("showreel") cho bộ dựng sẵn luật của thể loại đó (cắt nhanh, mỗi cảnh một kỹ thuật, cái hay nhất lên trước); "làm hết sức" tăng công sức khi chạy ở mức suy nghĩ cao. Câu đầu vẫn phải gắn với sản phẩm thật, không để bộ dựng tự khoe kỹ thuật.

---

## Mẫu 3 - Bản chỉ đạo dài (video trên 30 giây, nhiều phiên, có trợ lý con)

Cấu trúc học từ các bản chỉ đạo dài trong bài nguồn (mục 10): chúng không tả một video mà "thuê một đoàn làm phim". Lưu thành `docs/ban-chi-dao.md`.

```markdown
Bạn là đạo diễn, người làm hoạt hình, người làm âm thanh và kỹ sư dựng cho một phim <độ dài> làm bằng mã. Đây là việc nhiều phiên; không vội dựng bản cuối.

## Phim trong một câu
<Câu tóm tắt và cảm giác người xem phải có ở giây cuối. Mọi quyết định kiểm lại với câu này.>

## Tham chiếu và đầu vào
- ./refs/: <video, khung hình, thư viện ảnh>. Lấy ngữ pháp, không lấy nội dung.
- ./assets/: tài liệu thật của sản phẩm (danh sách trong kịch bản).
- ./audio/track.wav: <dùng nguyên, đo nhịp trước | không có, tự tổng hợp>.
- Kỹ năng dùng được: video-chuyen-dong, <remotion:remotion-best-practices | video-3d-theo-mau>.
- Dịch vụ ngoài trong biến môi trường: <TÊN_BIẾN>. Ngân sách: <số tiền>. Dùng tiết kiệm.

## Hướng hình
<3-5 dòng: màu, chữ, kết cấu, ngôn ngữ máy quay. Các kiểu bị cấm.>

## Bảng nhân vật (khi có linh vật; xem giong-doc-linh-vat.md)
<tỷ lệ, bảng màu lấy từ bản vẽ, các nét mặt, phần nhận dạng không đổi dù đổi phong cách>

## Lưới nhịp
0:00-0:02  mở: <hình gây chú ý nhất>
0:02-0:10  <phần 1>
...        cứ 3-5 giây có một điểm thưởng thị giác mới
<cuối>     khung cuối dẫn về khung đầu (nếu lặp) hoặc đứng yên cho lời kêu gọi

## Chữ trên màn hình
<khi nào chữ to chiếm khung, khi nào nằm như phụ đề; bố cục chừa chỗ cho chữ>

## Quy trình và các cổng duyệt
1. Viết docs/style_guide.md và docs/shotlist.md (mỗi cảnh: khung, máy quay, chữ, tiếng). Gửi PM bảng cảnh, chờ duyệt.
2. Dựng ảnh tĩnh cho mọi cảnh. Ảnh ghép. Phê bình.
3. Bản nháp chuyển động 960x540, âm thanh tạm. Sửa nhịp trước khi làm đẹp.
4. Chuyển động đầy đủ, lượt làm đẹp, lượt âm thanh, dựng cuối.
5. Chia việc cho trợ lý con theo chương (tối đa 3, theo CLAUDE.md). Viết docs/huong-dan-canh.md trước để mọi trợ lý con viết mã cùng một kiểu; tệp dùng chung chỉ đọc.

## Vòng phê bình (mỗi cảnh, ít nhất 3 vòng)
Theo cham-diem.md. Ghi điểm và 3 lỗi lớn nhất vào docs/review_log.md. Sửa, lặp tới khi mọi tiêu chí từ 8.

## Sản phẩm giao
out/<ten>_<kho>.mp4 · out/loop_check.mp4 (nếu lặp) · out/poster.png · out/contact.png · README.md
```

Không bỏ cổng duyệt. Trong kho này PM duyệt ở cổng 1 (bảng cảnh) và trước khi dựng cuối; không áp dụng kiểu "PM không trả lời trong 10 phút thì cứ làm tiếp" của bài nguồn, vì CLAUDE.md yêu cầu hỏi trước.

---

## Ghép tạo rồi vẽ đè (khi cần chuyển động khó viết bằng mã)

Bài nguồn (mục 10) kể một cách: công cụ tạo video AI dựng cảnh nền có nhân vật và vật lý, rồi Claude vẽ lại toàn bộ bằng mã đè lên, người xem chỉ thấy lớp vẽ bằng mã. Lớp AI cho chuyển động khó tự viết; lớp mã cho hình đồng nhất, của riêng mình. Trong kho này chỉ dùng khi PM đồng ý dùng dịch vụ tạo video AI (tốn phí, có điều khoản riêng); PM tự chạy công cụ đó theo `video-3d-theo-mau`.
