# Chấm điểm video quảng cáo

Thói quen tạo ra khác biệt lớn nhất giữa video lan truyền và video "tàm tạm" là bắt Claude xem chính các khung mình dựng (bài nguồn, mục 11). Một video trong bài cần 163 lần gọi mô hình và gần 7 giờ; sửa nhiều vòng là cách làm bình thường, không phải thất bại.

## Khổ và vùng an toàn

| Khổ | Kích thước | Nơi đăng |
|---|---|---|
| 9:16 | 1080x1920 | TikTok, Reels, Shorts, Shopee Video, Zalo Video |
| 4:5 | 1080x1350 | Bảng tin Facebook, Instagram |
| 1:1 | 1080x1080 | Facebook, Zalo, sàn thương mại |
| 16:9 | 1920x1080 | YouTube, trang web, màn hình hội trường |

**Vùng an toàn khổ 9:16 (ước lượng, kiểm lại trên ứng dụng thật trước khi đăng vì các nền tảng hay đổi giao diện):** trên nền 1080x1920, giao diện nền tảng che khoảng 200 điểm ảnh trên cùng, khoảng 450 điểm ảnh dưới cùng (tên tài khoản, chú thích, nút mua) và khoảng 140 điểm ảnh bên phải (nút thích, bình luận, chia sẻ). Chữ, giá, lời kêu gọi, logo đặt trong khung còn lại, khoảng x 60-940, y 200-1470. Khi chấm, phủ một lớp mờ lên các vùng bị che để thấy chữ có bị đè không.

Chú thích lớn căn giữa vùng an toàn (x khoảng 500 ở khổ 1080) chứ không căn giữa khung (540); chú thích rộng quá 880 điểm ảnh thì rút chữ hoặc ngắt dòng (lần dựng thử đầu, chú thích 962 điểm ảnh bị lấn vào cột nút của nền tảng).

Không cắt bản 16:9 thành dọc. Mỗi khổ sắp lại chữ và giao diện từ cùng dòng thời gian (hàm bố cục).

## Tạo ảnh để xem

Chạy sau mỗi lần dựng (thay `out/final.mp4` bằng tệp thật):

```bash
# Ảnh ghép: 2 khung mỗi giây, 6 ảnh một hàng
ffmpeg -i out/final.mp4 -vf "fps=2,scale=270:-1,tile=6x5" -frames:v 1 out/contact.png

# Dải 12 khung liên tiếp quanh một động tác nhanh (ví dụ giây 4,2) để bắt chỗ giật, chồng chữ
ffmpeg -ss 4.1 -i out/final.mp4 -vf "scale=320:-1,tile=12x1" -frames:v 1 out/strip.png

# Xem ở cỡ điện thoại: bề ngang 360 điểm ảnh
ffmpeg -i out/final.mp4 -vf "fps=1,scale=360:-1,tile=5x3" -frames:v 1 out/phone.png

# Kiểm chỗ nối khi đăng dạng lặp: phát nối hai lần
ffmpeg -stream_loop 1 -i out/final.mp4 -c copy out/loop_check.mp4
```

Video dài hơn 15 giây thì tăng số hàng của `tile` cho đủ khung. Kiểm thêm: dựng một đoạn 5 giây hai lần, so mã băm hai tệp; khác nhau thì còn chỗ dùng số ngẫu nhiên hoặc hẹn giờ (vi phạm luật dựng).

## Câu lệnh tự phê bình

Dùng nguyên ý sau (viết lại cho video cụ thể):

```text
Mở out/contact.png, out/strip.png, out/phone.png và xem thật kỹ. Đóng vai đạo diễn chuyển động khó tính, không phải tác giả tự hào về sản phẩm của mình.

Chấm 8 tiêu chí trong cham-diem.md, thang 10, mỗi điểm một câu lý do.

Liệt kê 3 lỗi lớn nhất kèm giây. Tìm riêng các lỗi: chữ chồng nhau khi đổi trạng thái; vật trượt đều thay vì có lò xo; nhãn ở góc và viền khung; cảnh tiêu đề giữa nền chuyển màu; chữ bị mờ khi phóng; một nhịp không có gì xảy ra; giật ở chỗ nối khi lặp; chữ nằm trong vùng bị giao diện nền tảng che; sản phẩm hiện sai so với ảnh thật; số liệu không có trong kịch bản.

Sửa 3 lỗi đó, chỉ dựng lại đoạn bị ảnh hưởng, gửi ảnh ghép mới và điểm mới.
```

## Tám tiêu chí

| Tiêu chí | Câu hỏi khi chấm | 8 điểm trở lên khi |
|---|---|---|
| Mở | Hai giây đầu có làm người đang lướt dừng lại không? | Khung đầu đã có chuyển động lớn hoặc câu chữ đánh trúng nỗi lo; không mở bằng logo hay màn hình trống |
| Sản phẩm rõ | Xem đến giây 6, người lạ nói được sản phẩm là gì, dùng để làm gì không? | Sản phẩm thật xuất hiện trước giây 6, tên đọc được |
| Đọc được trên điện thoại | Ở ảnh 360 điểm ảnh, mọi chữ đọc được không? | Chữ chính cao từ khoảng 4% chiều cao khung trở lên, đủ tương phản, đứng yên đủ thời gian đọc |
| Chuyển động | Có lò xo, có khối lượng, không giật, không trôi? | Không có vật trượt đều; đổi trạng thái liền mạch; có làm mờ chuyển động ở bản cuối |
| Đa dạng | Cứ 2-4 giây có điều mới không? | Không có nhịp chết; không lặp một kiểu chuyển cảnh quá hai lần liền |
| Bố cục và nhận diện | Đúng màu, phông, logo; một điểm nhìn chính mỗi khung? | Một màu nhấn; logo đúng tệp; không có kiểu hình bị cấm |
| Âm thanh | Cắt cảnh khớp nhịp; tiếng động khớp hành động; tắt tiếng vẫn hiểu? | Mọi khoảnh khắc lớn rơi đúng nhịp mạnh; thông điệp chính có chữ trên hình |
| Lời kêu gọi | Người xem biết phải làm gì tiếp, đọc kịp, không bị che? | Lời kêu gọi cụ thể (động từ và nơi đến), đứng yên ít nhất 2,5 giây, trong vùng an toàn |

Ghi mỗi vòng vào `docs/review_log.md`:

```markdown
## Vòng <n> - <ngày giờ>
| Mở | Sản phẩm rõ | Đọc được | Chuyển động | Đa dạng | Nhận diện | Âm thanh | Kêu gọi |
|---|---|---|---|---|---|---|---|
| 7 | 9 | 6 | 8 | 8 | 9 | 7 | 6 |
Ba lỗi lớn nhất:
1. 2,4 giây - <mô tả> - sửa: <cụ thể>
2. ...
Đã sửa: <...>
```

Điểm do Claude tự chấm nên có thể lạc quan. Vì vậy sau vòng chấm vẫn phải có rà từng giây bằng trợ lý con và PM xem bản cuối.

## Mức lỗi khi rà từng giây

Dùng thang P0-P2 của `video-khoa-hoc`, cộng thêm các lỗi riêng của quảng cáo:

- **P0 - phải sửa**: số liệu, giá, lời hứa không có trong kịch bản đã duyệt hoặc không có nguồn; tên sản phẩm, giá, mã giảm giá sai chính tả hoặc sai số; sản phẩm hiện khác ảnh thật (màu hộp, nhãn, giao diện); tính năng chưa phát hành; từ "nhất", "số một" không có chứng minh; lời kêu gọi không đọc kịp hoặc bị giao diện nền tảng che; logo hãng khác hoặc ảnh người không có quyền dùng.
- **P1 - nên sửa**: sản phẩm xuất hiện sau giây 6; hai giây đầu tĩnh; chữ nhỏ ở cỡ điện thoại; tiếng động lệch hành động; khổ dọc chỉ là bản ngang cắt lại.
- **P2 - có thể bỏ qua**: chi tiết thẩm mỹ nhỏ.

Cách sửa phải cụ thể ("giữ khung giá thêm 0,6 giây", "đẩy lời kêu gọi lên y 1300"), không nhận góp ý chung chung kiểu "cho mượt hơn".
