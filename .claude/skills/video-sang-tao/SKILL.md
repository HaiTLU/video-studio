---
name: video-sang-tao
description: Làm phim chuyển động 2D ngắn bằng mã (motion design, 10-30 giây, 16:9 hoặc 9:16, lặp liền) theo cách "hỏi, gợi ý ý tưởng, viết bản chỉ đạo 6 khối, duyệt bảng nhịp và 4 ảnh tĩnh, rồi mới dựng". Mỗi lần gợi ý một vật nối và một thể loại khác lần trước, học thêm công thức từ video mẫu PM gửi, ghi sổ ý tưởng và bài học để lần sau hay hơn. Dùng khi PM gõ /video-sang-tao, nói "làm video mới", "cho tôi ý tưởng video", "làm phim motion", "video chuyển động kiểu này", gửi prompt dài mô tả phim (có khối inputs, direction, structure, build), hoặc gửi video mẫu bảo "học cách làm này". Video quảng cáo một khóa cụ thể của TTC thì đi /video-khoa-hoc trước; kỹ năng này dành cho phim giới thiệu, thương hiệu, ý tưởng mới.
---

# Video sáng tạo: hỏi, gợi ý, dựng, học

Kỹ năng này tự đủ: có sẵn mã dựng, mã nhạc, mã chụp ảnh tĩnh, sổ ý tưởng và kho công thức. Không phải đọc thêm kỹ năng video khác để dựng, trừ khi PM cần việc của khóa TTC (xem Định tuyến).

## Vì sao làm theo cách này

Hai thứ làm video mẫu đẹp: một **vật nối** đi xuyên mọi cảnh (một chấm, một đường kẻ, một chữ cái...) nên phim thành một mạch; và **luật dựng chặt** (mọi hình tính từ thời gian, lò xo thay đường cong cứng, cấm đồ họa sáo). Lỗi tốn công nhất là dựng xong mới biết sai hướng, nên có cổng duyệt rẻ trước khi dựng. Lỗi làm phim nhàm là mỗi video một khuôn, nên mỗi lần phải đổi vật nối và thể loại.

## Bước 0 - Đọc sổ trước khi hỏi (không hỏi PM điều tra được)

1. `so-y-tuong.md`: ý tưởng đã dùng, điều PM khen hoặc sửa. Không đề xuất lại vật nối đã dùng trong 3 video gần nhất.
2. `cong-thuc/`: công thức đã học (mỗi tệp một video hoặc một phong cách). Chọn 1-2 cái hợp để trộn.
3. `references/ngan-hang-y-tuong.md`: vật nối, thể loại, bảng ghép và luật cấm.

## Bước 1 - Hỏi bằng hộp thoại, vòng 1 chốt hướng

Theo CLAUDE.md mục 2, mọi câu hỏi PM đều dùng `AskUserQuestion`, 2-4 lựa chọn, khuyến nghị đứng đầu. Vòng 1 hỏi tối đa 4 câu:

1. **Phim nói về gì và cho ai xem** (AI Lab, Viện, TTC chung, sự kiện, đề tài khác). Nội dung thật lấy từ kho, không bịa số liệu.
2. **Ý tưởng**: đưa 3-4 ý, mỗi ý ghi `vật nối + thể loại + một câu mô tả cảnh mở và cảnh cuối`. Quy tắc: ít nhất một ý lạ (ghép vật nối với thể loại ít ai nghĩ tới, lấy từ bảng ghép); ý khuyến nghị là ý hợp nhận diện và nội dung nhất, không phải ý lạ nhất. Có công thức trong `cong-thuc/` hợp thì nêu tên.
3. **Khổ và độ dài**: mặc định 16:9, 15 giây; hỏi thêm 9:16 khi đăng mạng xã hội.
4. **Video mẫu**: PM có gửi không. Có thì chuyển sang `references/hoc-tu-video-mau.md` trước khi hỏi tiếp.

Vòng 2 (sau khi PM chọn ý) chốt chi tiết: sáu thông tin của khối `inputs` (nhãn nút hoặc chữ mở đầu, một từ chủ đạo, một con số có nguồn hoặc "không số", chữ thẻ cuối, một màu nhấn, nhạc). Thiếu số liệu thật thì đổi cảnh số liệu thành chữ định tính, đừng điền số giả.

## Bước 2 - Viết bản chỉ đạo 6 khối

Viết vào `<thư mục dự án>/bang-nhip.md` rồi dựng bảng nhịp:

| Khối | Nội dung |
|---|---|
| `inputs` | 6 thông tin PM đã chốt |
| `direction` | Bầu không khí 3-4 câu, một màu nhấn, nền, phông, vật nối, danh sách cấm |
| `structure` | Từng cảnh theo giây: phần tử nào biến thành phần tử nào; cảnh cuối nối về cảnh đầu |
| `build` | Luật kỹ thuật (xem Bước 4) |
| `gotchas` | Lỗi riêng của phim này, lấy từ `cong-thuc/` và `bai-hoc` trong sổ |
| `start` | Hỏi inputs, rồi đưa bảng nhịp + 4 ảnh tĩnh |

Bảng nhịp có cột: giây, phách, cảnh, vật nối ở đâu và làm gì, chữ, chuyển động. Phách theo nhịp nhạc (120 nhịp/phút = 0,5 giây). Mỗi phách lớn có một thay đổi nhìn thấy; chỗ chữ cần đọc được giữ yên tối thiểu 1,3 giây.

## Bước 3 - Cổng duyệt: bảng nhịp + 4 ảnh tĩnh

Dựng ngay `index.html` từ `scripts/khung.html`, viết đủ các cảnh, rồi chụp 4 ảnh tĩnh từ chính mã đó (một ảnh mỗi cảnh chủ chốt) bằng `scripts/chup_anh_tinh.js`. Gửi PM cùng bảng nhịp, hỏi bằng hộp: đạt, sửa ít, hoặc làm lại hướng. Chỉ dựng bản đủ khi PM đạt. Ảnh tĩnh phải đúng, vì cùng một mã sẽ ra video.

Báo trước mọi chỗ khác với prompt hay ý PM (ví dụ chi tiết gắn vào chữ "i" không hợp tiếng Việt thì đổi và nói rõ).

## Bước 4 - Dựng (luật cứng và lý do)

Chi tiết đầy đủ ở `references/quy-trinh-dung.md`. Tóm tắt:

- Một tệp `index.html`, canvas 1920x1080, 60 khung/giây. `seek(t)` tính mọi hình; cấm CSS transition, timer, `requestAnimationFrame`, `Math.random` không hạt giống. Lý do: tua tới giây nào cũng ra đúng một hình, nên dựng lại và chụp ảnh tĩnh luôn khớp.
- Lò xo dạng đóng trong `scripts/spring.js`; một giá trị đổi đích nhiều lần dùng `track` (cộng lò xo). Biểu đồ và chấm dùng cùng một hàm lò xo, nếu không chuyển động nhìn giả.
- Chữ có giờ vào và giờ ra riêng, không chồng nhau. Hình phủ kín khung phải lớn quá cả bốn góc. Khung cuối bằng khung đầu.
- Nhạc và tiếng động tự tạo bằng `scripts/tao_nhac.py` (sửa danh sách sự kiện theo bảng nhịp); không dính bản quyền.
- Dựng bằng `scripts/render.py` (HyperFrames, 240 khung/giây trộn thành 60), rồi `scripts/gan_the_mau.sh`.

## Bước 5 - Kiểm bằng số rồi mới báo xong

- Đủ số khung (giây x 60) và đúng độ dài (`ffprobe`).
- SSIM khung đầu so với khung cuối từ 0,999.
- `hyperframes check` 0 lỗi.
- Rà từng giây bằng trợ lý con `ra-soat-video` (model `sonnet`), sửa mọi P0 và P1. Tự đối chiếu lỗi trợ lý nêu với mã trước khi sửa.
- Xem lại vài khung có chữ sau khi sửa, và đọc dấu tiếng Việt từng chữ.
- Nói rõ điều chưa kiểm (thường là nhạc chưa nghe).

## Bước 6 - Học (luôn làm, không hỏi duyệt trước)

1. Ghi một dòng vào `so-y-tuong.md`: ngày, tên video, vật nối, thể loại, điều PM khen, điều PM sửa, một mẹo.
2. Có bài học kỹ thuật mới thì thêm vào `references/quy-trinh-dung.md` mục Lỗi đã gặp; có kỹ thuật chuyển động mới thì tạo `cong-thuc/<ten>.md` theo `cong-thuc/_mau.md`.
3. Hỏi PM bằng hộp: video này nên giữ làm "mẫu" (công thức dùng lại) hay chỉ ghi sổ.
4. Cuối phiên báo PM một dòng: đã ghi gì. PM xóa được.

## Định tuyến

| Việc | Đi đâu |
|---|---|
| Phim giới thiệu, thương hiệu, ý tưởng mới, học từ video mẫu | Kỹ năng này |
| Video quảng cáo một khóa TTC cụ thể (có học phí, ngày khai giảng, cách đăng ký) | `/video-khoa-hoc` trước, lấy phần dựng ở đây nếu cần |
| Video ra mắt ứng dụng, hàng hóa, dịch vụ cần kịch bản bán hàng | `/video-quang-cao-san-pham` |
| Video giao diện một khối biến hình theo nhạc 120 nhịp | Làm được ở đây (vật nối là khối); mẫu riêng ở `/video-ui-bien-hinh` |
| Có người thật nói trước máy quay | Không thuộc kỹ năng này |

Nhận diện ĐHTL (Scarlet #f32409, Indigo #000066, nền Cultured #f9f5f4, phông Be Vietnam Pro) là mặc định cho mọi video của Trường; chỉ đổi khi PM yêu cầu. Phông chép từ `brand/fonts/web/` (giấy phép OFL).

## Gợi ý model

Phiên lập ý tưởng và bản chỉ đạo: Sonnet 5.5 - high. Video quan trọng gửi BGH hoặc đối tác: opusplan + cố vấn Opus 5.5 - high. Rà từng giây dùng `sonnet`.
