---
name: video-khoa-hoc
description: Làm video quảng cáo ngắn (khoảng 20 giây, khổ dọc 9:16 kèm bản 16:9) cho một khóa đào tạo ngắn hạn của TTC - Trường Đại học Thăng Long. Dùng khi PM gõ /video-khoa-hoc hoặc nhờ "làm video quảng cáo khóa ...", "video chiêu sinh", "clip giới thiệu khóa học". Nhận thông tin khóa (tên, đối tượng, khai giảng, lịch, địa điểm, học phí, cách đăng ký, 3 điểm nổi bật), soạn bản hướng dẫn dựng video, dừng cho PM duyệt, rồi dựng video bằng HyperFrames (HTML + GSAP, PM chỉnh được trong Studio), có lời đọc tiếng Việt bằng VieNeu-TTS. Không dùng cho video dài hay video quay người thật.
---

# Video quảng cáo khóa ngắn hạn TTC

Nội dung: Bước 0 Gom thông tin; Bước 0b Tra nhanh; Bộ màu; Dàn cảnh 20 giây; Âm thanh; Cách dựng; Thư mục; Các mốc; Vòng tự soát lỗi; Đo hiệu quả; Lỗi hay gặp; Gợi ý model.

Khung này lấy từ bản hướng dẫn đã duyệt cho khóa Tiếng Anh giao tiếp:
`tai-lieu/mau/260928_DaoTaoNganHan_BriefVideo_TiengAnhGiaoTiep.md`.
Mọi video tạo từ kỹ năng này dùng chung phong cách, chỉ thay thông tin khóa.

## Bước 0 - Gom thông tin (bắt buộc, không tự bịa)

Cần đủ các mục sau. **Bắt buộc phải có:** tên khóa, khai giảng và lịch học, địa điểm, cách đăng ký; thiếu một trong bốn thì hỏi, không điền thay. Học phí và hai mục cuối bảng (video mẫu, điều không muốn) được để trống. Thiếu mục nào thì hỏi PM **một lần** bằng hộp thoại (`AskUserQuestion`), gộp các câu vào cùng một hộp. Luôn có câu hỏi phong cách (PM dặn 3/10/2026), kể cả khi các mục khác đã đủ: đưa 3 phong cách hợp nội dung nhất từ "Danh mục phong cách có sẵn" trong kỹ năng `video-chuyen-dong`, mỗi lựa chọn ghi hợp với gì, phong cách khuyến nghị đứng đầu; PM có video mẫu thì thêm lựa chọn "Theo video mẫu". Kèm 1 mẫu gần nhất từ danh sách Skillry theo mục "Nguồn ý tưởng Skillry" của `video-chuyen-dong` (tối đa 4 lựa chọn). Màu và phông vẫn theo nhận diện ĐHTL ở mục dưới.

| Mục | Ví dụ |
|---|---|
| Tên khóa | Kỹ năng y tế cơ bản |
| Ý chính một câu | Tự tin sơ cứu đúng cách sau 4 buổi |
| Đối tượng | Sinh viên, người đi làm |
| Khai giảng, lịch học, địa điểm | 15/11/2026, tối thứ 3-5, Trường ĐH Thăng Long |
| Học phí hoặc ưu đãi | 2.500.000 đồng (có thể bỏ trống) |
| Cách đăng ký | Đường dẫn, mã QR hoặc số điện thoại |
| 3 điểm nổi bật | Học nhóm nhỏ, thực hành trên mô hình, có chứng chỉ |
| Câu mở đầu gây chú ý | "Gặp người ngất, bạn có biết làm gì?" |
| 3 tình huống quen thuộc | Ở nhà, nơi làm việc, trên đường |
| Video mẫu PM thích (không bắt buộc) | Đường dẫn 1-2 video; học nhịp, cách chuyển cảnh, không chép |
| Điều PM không muốn (không bắt buộc) | Không dùng màu đỏ làm nền, không có chữ chạy |
| Giọng đọc (mặc định Hải Đăng) | Đổi giọng hoặc tắt lời đọc nếu PM muốn |

Quy tắc nội dung: chỉ dùng thông tin PM đưa. Không thêm lời hứa không có thật ("đảm bảo 100%", "giảng viên nước ngoài"...). Tên khóa, ngày, học phí phải khớp nguyên văn.

## Bước 0b - Tra nhanh trước khi viết (tùy chọn, học từ OpenMontage ngày 10/10/2026)

Chỉ làm khi khóa mới, chưa có câu mở đầu hay 3 tình huống chắc chắn, hoặc PM nhờ "tìm hướng cho hay". Khóa đã đủ thông tin thì bỏ qua. Giao một trợ lý con (`doc-tom-tat`, model `haiku`), trả về tối đa 300 từ gạch đầu dòng kèm đường dẫn nguồn:

- **Quảng cáo khóa tương tự đang chạy:** 3 mẫu khóa cùng chủ đề trên Facebook, TikTok, YouTube; ghi mẫu nào mở đầu giống nhau (để tránh) và điều chưa ai nói.
- **Câu hỏi và nỗi lo thật của người học:** 3-5 câu lấy từ diễn đàn, nhóm, bình luận (chép nguyên văn, kèm đường dẫn); dùng làm câu mở đầu và 3 tình huống ở Bước 0.
- **Số liệu:** chỉ dùng số có nguồn gốc rõ (tên tổ chức, năm); không có thì bỏ, không tự ước.

Luật: viết câu mở đầu bằng lời của mình trước, rồi mới đối chiếu với kết quả tra; 3 phương án ở mục Các mốc phải khác nhau về ý (câu mở đầu, góc nhìn), không chỉ khác màu hay nhịp. Kết quả tra đưa vào bản `BriefVideo` để PM duyệt cùng lúc, không thêm một lần dừng nào.

## Bộ màu và nhận diện

- **Bộ màu (PM chốt 29/9/2026): bộ nhận diện chính thức theo cẩm nang brand.thanglong.edu.vn**, giống ứng dụng Chuẩn hóa văn bản (`brand/MAU.md`):
  - Indigo `#000066` (màu chủ đạo, chữ tiêu đề, khối lớn); Indigo nhạt `#1a1a80`
  - Scarlet `#f32409` (điểm nhấn: nút kêu gọi, gạch chân, con số quan trọng); Scarlet đậm `#cf1d05`
  - Cultured `#f9f5f4` (nền sáng); Palatinate `#1d53e6` (màu phụ, dùng ít)
  - Chữ thường `#0a0e18`, chữ phụ `#5a6070`
  - Scarlet chỉ làm điểm nhấn, không làm nền lớn; chữ nhỏ không đặt trên nền Scarlet.
- **Phông chính thức, đã có sẵn trong kho, chép vào thư mục video, không dùng Google Fonts:**
  - Tiêu đề: Thang Long Sans (`brand/fonts/ThangLongSans-Regular.otf`, `-Medium.otf`, `-Bold.otf`)
  - Chữ thường: Manrope (`brand/fonts/Manrope-Variable.ttf`)
  - Kiểm tra dấu tiếng Việt hiển thị đúng ở khung đầu tiên trước khi dựng tiếp.
- Logo: tệp `brand/logo-tlu.png`, không tự vẽ lại logo.
- Nền sáng, gọn, trẻ trung. Không hình người thật; dùng hình khối, biểu tượng đơn giản, chữ động.
- Tránh kiểu mặc định "chữ giữa màn hình trên nền chuyển màu, mọi thứ mờ dần hiện ra".
- **Phong cách chuyển động:** đọc `phong-cach.md` trước khi phác dàn cảnh (tối giản, một cảnh một ý, hướng mắt bằng tương phản, chuyển cảnh nối từ cảnh trước, đổi nhịp nhanh - giữ).

## Dàn cảnh 20 giây

| Giây | Nội dung | Chữ trên màn hình |
|---|---|---|
| 0-2 | Câu mở đầu gây chú ý, chuyển động bật mạnh | Câu mở đầu |
| 2-6 | 3 tình huống quen thuộc, vẽ bằng hình khối | Tên 3 tình huống |
| 6-11 | 3 điểm nổi bật hiện lần lượt | 3 điểm nổi bật |
| 11-15 | Khai giảng, lịch học, địa điểm (và học phí nếu có) | Theo Bước 0 |
| 15-20 | Logo Trường, cách đăng ký; khung cuối đứng yên đủ lâu để đọc | "Đăng ký ngay: ..." |

Mỗi 3-4 giây có một chuyển động mới. Chữ đủ to để đọc trên điện thoại, tối đa 8 từ mỗi dòng.

Bảng dàn cảnh trong bản hướng dẫn có thêm cột **Lời đọc**, viết theo `../video-quang-cao-san-pham/giong-doc-linh-vat.md` (mục Viết lời đọc): 20 giây chứa khoảng 45-55 âm tiết; lời đọc nói thêm ý, không đọc lại y chữ trên màn hình; tên khóa, ngày, học phí đọc đúng nguyên văn Bước 0. PM duyệt lời đọc cùng bản hướng dẫn ở mốc 1.

Trong bản hướng dẫn, mỗi cảnh ghi đủ 5 mục: người xem cần hiểu gì; hình ảnh (bố cục, vật chính); chuyển động (vào, đứng, ra); âm thanh gắn với hành động nào; cách nối sang cảnh sau.

## Âm thanh

Nhạc nền **tự tổng hợp bằng mã** (không dùng nhạc có bản quyền), chuyển cảnh khớp nhịp. Nhịp chọn theo tâm trạng khóa (bảng trong `phong-cach.md`), mặc định 115-120 nhịp/phút.

**Lời đọc bật mặc định (PM chốt 8/10/2026, thay quy tắc cũ "không dùng giọng đọc AI"):** dùng VieNeu-TTS, giọng mặc định **Hải Đăng** (nam, Bắc), tạo bằng `../video-quang-cao-san-pham/scripts/loi_doc_vieneu.py` (cách cài ghi đầu tệp; chạy trên máy, miễn phí, không gửi chữ ra ngoài). Đặt từng câu vào lưới nhịp, hạ nhạc 8-10 dB khi có giọng, phụ đề lấy từ lời đọc; các bước ghép theo mục "Ghép giọng vào phim" của tệp `giong-doc-linh-vat.md`. Video vẫn phải hiểu được khi tắt tiếng. Không nhái giọng người thật khi chưa có đồng ý bằng văn bản.

## Cách dựng

- Dựng bằng **HyperFrames** (PM chốt 8/10/2026, thay hẳn cách cũ tự viết `seek(t)` rồi Playwright chụp, ffmpeg ghép). Cách làm, lệnh và các điểm đã chạy thử: `dung-hyperframes.md` trong thư mục kỹ năng này; năm kỹ năng video của kho cùng trỏ về tệp đó. Không dùng dịch vụ trả phí, không cần khóa API, chỉ dựng trên máy.
- Mỗi cảnh là một cảnh con trên dòng thời gian, chữ là phần tử HTML thật, để PM mở Studio dời cảnh, sửa chữ. Thông tin hay đổi (ngày khai giảng, học phí, đường dẫn đăng ký) khai báo thành biến.
- Chuyển động viết bằng GSAP trên dòng thời gian dừng sẵn; lò xo dùng ease có công thức, không dùng nảy kiểu hoạt hình.
- **Luật cứng khi viết mã** (để khung nào cũng vẽ lại y hệt): cấm `Math.random()` (cần ngẫu nhiên thì dùng hàm có hạt giống cố định); cấm chuyển tiếp và hoạt ảnh CSS tự chạy, hẹn giờ, `requestAnimationFrame`; cấm ảnh, phông, thư viện tải từ ngoài lúc dựng (chép vào `assets/`). Nhạc đặt bằng thẻ `<audio>` theo đúng cách của HyperFrames.
- **Kiểm tra tự động trước khi dựng hàng loạt:** `check` phải qua, rồi `snapshot --at 0,2,6,11,15,19.5` và xem từng ảnh: chữ cần có đang hiện đúng (đối chiếu Bước 0). Sai thì sửa rồi mới dựng.
- **Thời gian đọc chữ** (học từ `core/render/readcheck.mjs` của lemo-opuscar): mỗi dòng chữ phải ở yên trên màn hình ít nhất (số ký tự chia 15) cộng 1,5 giây, tối thiểu 1,5 giây. Kiểm tra theo công thức này cho từng câu trong bảng nhịp.
- **Âm lượng:** chuẩn hóa về -14 LUFS sau khi dựng (`ffmpeg -i in.mp4 -c:v copy -af loudnorm=I=-14:TP=-1.5:LRA=11 out.mp4`) để đăng mạng xã hội không bị nền tảng tự hạ hay nâng tiếng.
- **Dò đoạn im lặng** (học từ kỹ năng `remotion-markup` của Remotion, bản 4.0.532, 4/10/2026): đo ngưỡng bằng `ffmpeg -i nhac.wav -af loudnorm=print_format=json -f null /dev/null`, lấy `input_thresh`, rồi chạy `ffmpeg -i nhac.wav -af "silencedetect=noise=<input_thresh>dB:d=0.5" -f null /dev/null` để liệt kê các đoạn lặng; dùng khi kiểm nhạc tự tổng hợp hoặc cắt bản ghi họp.
- Bản nháp `render --quality draft`; bản giao `render --quality delivery --fps 60`, H.264 yuv420p để phát được trên điện thoại.
- **Kiểm tệp trước khi đăng** (học từ `reel-export` của charlie947/motion-graphics-skills, MIT, 10/10/2026): `ffprobe -v error -show_entries stream=codec_type,codec_name,width,height,pix_fmt,color_range,color_space -of compact video.mp4`. Đạt khi video `h264`, `yuv420p`, `color_range=tv`, `bt709` và có một luồng âm thanh `aac` (video không tiếng thì thêm âm thanh im lặng bằng `-f lavfi -i anullsrc=r=48000:cl=stereo`). Thêm `-movflags +faststart` để phát được ngay khi chưa tải xong. Nguồn là bản quay HEVC từ điện thoại hoặc dải màu `pc` thì xuất lại H.264 dải `tv`, kể cả sau khi chỉnh sửa. Dán một khung giữa video xem ở cỡ điện thoại. Bản dọc 1080x1920: chữ và logo nằm trong vùng an toàn, đối chiếu số ở `video-quang-cao-san-pham/cham-diem.md`.
- **Ảnh bìa động GIF lặp** (cho bản tin, bài đăng khóa; học từ `loop-cover` cùng kho): chỉ một phần tử động, 180 khung 20 khung/giây (9 giây); xoay vòng sao cho khung 1 là hình hoàn chỉnh (email và bản xem trước liên kết chỉ hiện khung 1). Ghép: `ffmpeg -y -framerate 20 -i f%03d.png -filter_complex "split[x][y];[x]palettegen=max_colors=128:stats_mode=full[p];[y][p]paletteuse=dither=none" -loop 0 bia.gif`. Đo đường nối bằng độ lệch giữa khung cuối và khung đầu (đo bằng đoạn mã nhỏ trên ảnh xám thu nhỏ; kho gốc đạt 0 đến 0,3), không nhìn mắt; tệp nên dưới khoảng 2,3 MB. Độ lệch xa nhất so với khung đầu (kho gốc 0,7 đến 2,8) gần 0 nghĩa là chẳng có gì chuyển động.
- Làm theo video mẫu, khớp nhạc bằng `beats.json` hoặc chấm điểm nhiều vòng: xem kỹ năng `video-chuyen-dong`.
- Bản 16:9 là dự án thứ hai cùng nội dung, sắp lại bố cục, không cắt xén.

## Thư mục và tên tệp

`videos/<YYMMDD>_DaoTaoNganHan_<TenKhoaKhongDau>/`

- `YYMMDD_DaoTaoNganHan_BriefVideo_<TenKhoa>.md` - bản hướng dẫn đã điền
- `<TenKhoa>_9x16.mp4`, `<TenKhoa>_16x9.mp4`
- Ảnh đại diện (poster) và một ảnh ghép tất cả cảnh
- Thư mục dự án HyperFrames (mã nguồn) kèm `README.md` ghi cách đổi biến ngày khai giảng, học phí, cách mở Studio và lệnh dựng lại

Tệp video nặng: kiểm tra `.gitignore` trước khi commit; video trên 20MB thì không đưa lên kho, chỉ giữ mã nguồn và ảnh xem trước.

## Các mốc (không bỏ qua mốc nào)

1. Điền bản hướng dẫn từ Bước 0, lưu tệp `BriefVideo`, **dừng cho PM duyệt**.
2. **Phác 3 phương án dàn cảnh khác nhau rõ rệt** (khác cách mở đầu, nhịp chuyển cảnh, cách trình bày 3 điểm nổi bật), ghép thành **một ảnh** (mỗi phương án một hàng, 5 ô nhỏ cho 5 cảnh, dưới mỗi hàng một dòng mô tả), **dừng cho PM chọn một**. Cả 3 đều theo đúng bộ màu, dàn cảnh 20 giây và thông tin ở Bước 0.
3. Vẽ 5 khung hình tĩnh đầy đủ cho phương án đã chọn, **dừng cho PM duyệt**.
4. Dựng bản nháp đầy đủ, tạo lời đọc, ghép nhạc và giọng, xuất video. Sinh kèm **ảnh ghép từng cảnh đã dựng** (mỗi cảnh một hàng vài khung), tự xem kỹ từng cảnh trước khi ghép bản cuối; cảnh lỗi thì dựng lại riêng cảnh đó.
5. Rà từng giây (mục dưới), sửa, dựng bản cuối.

## Vòng tự soát lỗi

**Rà từng giây bằng một trợ lý con riêng** (phần tạo ra nhiều khác biệt nhất giữa video tốt và video thường):

- Giao cho **một** trợ lý con (model `sonnet`), chỉ được xem, **không được sửa**. Đưa cho nó: đường dẫn tệp video nháp, tệp `BriefVideo` và thông tin Bước 0.
- Trợ lý con tách video thành ảnh mỗi giây (`ffmpeg -i video.mp4 -vf fps=1 giay_%02d.png`), thêm các khung ngay trước và sau mỗi lần chuyển cảnh, xem lần lượt từng ảnh, rồi trả về danh sách lỗi theo mức:
  - **P0 - phải sửa:** sai hoặc thiếu thông tin so với Bước 0 (tên khóa, ngày, học phí, cách đăng ký); sai hoặc mất dấu tiếng Việt; chữ bị che, tràn khung, không đọc kịp; logo sai hoặc méo; khung cuối không đứng yên đủ lâu; nhạc lệch nhịp rõ; lời đọc sai tên khóa, ngày, học phí hoặc đọc sai dấu, câu bị cắt, nhạc lấn giọng.
  - **P1 - nên sửa:** chuyển cảnh giật; chữ quá nhỏ trên điện thoại; màu lệch bộ nhận diện; một cảnh quá dày chữ.
  - **P2 - có thể bỏ qua:** chi tiết thẩm mỹ nhỏ.
- Mỗi lỗi ghi: giây, mức, mô tả ngắn, cách sửa đề xuất. Cách sửa phải cụ thể (vd "giữ khung ngày khai giảng thêm 0,8 giây", "tăng chữ học phí lên 64px"); không chấp nhận góp ý chung chung như "cho mượt hơn", "cho sang hơn".
- Phiên chính **sửa hết P0**, sửa P1 nếu nhanh, rồi dựng lại và cho trợ lý con rà lại. Chỉ xuất bản cuối khi **không còn P0**. **Tối đa 3 vòng**; hết 3 vòng vẫn còn P0 thì dừng, báo PM danh sách lỗi còn lại.
- Báo PM kèm danh sách P1, P2 chưa sửa (nếu có).

Trước khi báo xong: đối chiếu từng chữ trên màn hình và lời đọc (`vo_do-dai.json`) với Bước 0 (tên khóa, ngày, học phí, cách đăng ký). Trợ lý con chỉ xem ảnh nên không nghe được giọng: phiên chính tự kiểm độ dài từng câu so với chỗ trống trong lưới nhịp và nhờ PM nghe bản nháp. Nhắc PM video phải qua bộ phận truyền thông hoặc Marcom duyệt trước khi đăng.

## Đo hiệu quả sau khi đăng (PM duyệt 3/10/2026)

Mục đích: biết kiểu video nào hiệu quả để video sau làm tốt hơn, không chỉ dừng ở bước giao tệp.

1. **Khi PM báo video đã đăng** (nền tảng, ngày đăng, đường dẫn): ghi một dòng vào bảng chung `videos/TheoDoi_HieuQuaVideo.md` (tạo tệp ở lần đầu). Rồi hẹn nhắc PM sau 7 ngày và 30 ngày (công cụ `send_later` nếu có; không có thì ghi việc treo vào bộ nhớ dự án).
2. **Khi đến hạn:** nhờ PM dán số liệu xem trên trang quản lý của nền tảng. Claude không tự đăng nhập tài khoản mạng xã hội của Trường. Các cột:

| Video | Khóa / dự án | Nền tảng | Ngày đăng | Mốc (7 hay 30 ngày) | Lượt xem | Thời gian xem trung bình (giây) | Tỷ lệ xem hết (%) | Lượt chia sẻ | Lượt bấm vào đường dẫn | Số đăng ký (nếu đo được) | Ghi chú |
|---|---|---|---|---|---|---|---|---|---|---|---|

3. **Rút bài học khi có từ 3 video trở lên:** so cách mở đầu, độ dài, khổ, phong cách với tỷ lệ xem hết và số đăng ký. Ghi 2-3 bài học ngắn vào cuối bảng và dùng cho bản chỉ đạo video sau. Số video còn ít thì ghi rõ là "chưa đủ để kết luận", không suy diễn.
4. Số đăng ký lấy từ Google Form hoặc phần mềm TTC: chỉ ghi số tổng, không ghi thông tin cá nhân người học.

## Lỗi hay gặp

Ghi từ lần làm thật; gặp lỗi mới thì thêm vào đây.

- **Trình duyệt trong phiên web không mở được trang ngoài:** Playwright báo `ERR_CERT_AUTHORITY_INVALID` khi đi qua máy chủ trung gian của phiên. Dựng video thì chỉ mở trang cục bộ (`file://` hoặc máy chủ trên máy); tài nguyên ngoài thì tải về bằng `curl` trước.
- **ffmpeg đi kèm Playwright là bản rút gọn**, không đọc được tệp MP4 ("Invalid data found"). Dùng `pip install imageio-ffmpeg` rồi lấy đường dẫn bằng `python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())"`, hoặc `apt-get install ffmpeg`.
- **Video mẫu YouTube** đòi đăng nhập xác nhận không phải người máy: không tải được, nhờ PM gửi tệp hoặc dán lời thoại. Reel Facebook công khai thì đọc được thẻ `og:video` trong mã trang để tải.
- **Chụp khổ hẹp** bằng `chromium --screenshot --window-size` bị cắt dưới khoảng 500px; dùng `playwright-cli resize`.
- **Lệnh dừng tiến trình:** không gộp `pkill -f` hay `pgrep -f` vào cùng một dòng lệnh có chứa đúng chuỗi đó, vì nó tự diệt chính vỏ lệnh (mã thoát 144).
- **Phông có hai tệp con (vietnamese, latin):** khai báo mỗi tệp một `@font-face` riêng kèm `unicode-range`; gộp hai tệp vào một `src` thì trình duyệt chỉ dùng tệp đầu, chữ không dấu rơi về phông mặc định (gặp ở video SonicRec 2/10/2026).
- **VieNeu báo "External data path escapes model directory"** khi dùng onnxruntime 1.30: cài `onnxruntime==1.22.1` (gặp 8/10/2026).
- **Máy chủ thử cũ còn giữ cổng** sau một lần chạy hỏng: kiểm tra và dừng nó trước khi mở lại.

## Gợi ý model

Chạy từ Sonnet 5.5 trở lên, không dùng Haiku: thử 5/10/2026 cho thấy Haiku tự bịa tên khóa, ý chính và điểm nổi bật dù Bước 0 cấm. Opus 5.5 - mức high (dựng video nhiều bước, cần tự soát kỹ). Trợ lý con rà từng giây dùng `sonnet`. Chỉ soạn bản hướng dẫn (mốc 1) thì Sonnet 5.5 - mức high là đủ.
