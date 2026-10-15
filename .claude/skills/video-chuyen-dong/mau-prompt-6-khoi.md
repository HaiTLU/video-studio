# Mẫu bản chỉ đạo 6 khối

Học từ một prompt phim chuyển động 2D dài 15 giây PM gửi ngày 8/10/2026 (chấm cam đi xuyên các cảnh: nút bật, chữ, biểu đồ lò xo, hình khối, chữ xoay vòng, thẻ cuối, rồi quay lại khung đầu để lặp liền). Nội dung của prompt gốc là quảng bá một model AI, không dùng lại; chỉ lấy khung viết.

Mẫu này là cách trình bày Bản chỉ đạo (Bước 1) cho video có một chi tiết xuyên suốt. Không thay các bước khác: bảng nhịp, nhạc, chấm điểm vẫn chạy như cũ.

## Sáu khối

| Khối | Viết gì | Vì sao |
|---|---|---|
| `inputs` | Đúng 6 thông tin cần hỏi PM trước khi làm: nhãn nút đầu video, một từ chủ đạo, một con số phần trăm cho biểu đồ, chữ thẻ cuối, một màu nhấn, nhạc có nhịp rõ | Hỏi một lần, đủ; không bịa. Hỏi bằng hộp thoại theo CLAUDE.md mục 2 |
| `direction` | Bầu không khí và phong cách trong 3-4 câu; một màu nhấn duy nhất; một chi tiết nối mọi cảnh; danh sách cấm (không video kho, không chuyển sắc, không phát sáng, không hạt tung tóe, không chuyển cảnh ngẫu nhiên, không chuyển động không gắn với phần tử đang có trên màn hình) | Chi tiết xuyên suốt cho phim một mạch; danh sách cấm cắt hẳn kiểu đồ họa chung chung |
| `structure` | Độ dài; mỗi cảnh một đoạn: bắt đầu bằng gì, phần tử nào biến thành phần tử nào, kết thúc ra sao. Cảnh cuối nối về cảnh đầu | Mỗi nhịp lớn có một thay đổi hình nhìn thấy, không có đoạn chết |
| `build` | Luật kỹ thuật đánh số: một tệp HTML, đúng khổ và số khung/giây, mọi hình tính từ thời gian trong `seek(t)`; lò xo dạng đóng; biểu đồ vẽ từ chính hàm lò xo đang đẩy chấm; chữ cái tách riêng khi cần biến hình; các hình (tròn, vuông, viên thuốc) là các trạng thái của cùng một khối; mốc nhịp đo từ nhạc | Dựng lại bao nhiêu lần cũng ra cùng một hình (xem `video-ui-bien-hinh` và `dung-hyperframes.md`) |
| `gotchas` | Các lỗi đã biết của riêng video này: biểu đồ và chấm phải cùng một chuyển động; chữ vào và chữ ra tính giờ riêng để không chồng; hình phủ kín khung phải lớn quá cả bốn góc; khung cuối khớp khung đầu để lặp không giật | Báo trước lỗi hay gặp, đỡ làm lại |
| `start` | Lệnh mở đầu: hỏi `inputs`, rồi đưa bảng nhịp và 4 ảnh tĩnh để duyệt, chưa dựng bản đủ | Cổng duyệt rẻ nhất: sai hướng thì sửa ở ảnh tĩnh, không phải ở video đã dựng |

## Cổng duyệt: bảng nhịp + 4 ảnh tĩnh

Trước khi dựng bản đầy đủ:

1. Lập bảng nhịp theo Bước 4.
2. Dựng 4 ảnh tĩnh từ cùng mã `seek(t)` (một ảnh mỗi cảnh chủ chốt: cảnh mở, cảnh biểu đồ hoặc số liệu, cảnh chữ động, thẻ cuối). Chụp bằng cách gọi `seek` tại 4 mốc nhịp, không vẽ riêng.
3. Gửi PM xem; hỏi "đạt hay phải sửa" bằng hộp thoại. Chỉ dựng bản đủ khi PM đạt.
4. Dựng xong, đối chiếu khung đầu và khung cuối (độ lệch bằng 0 ở mọi phần tử) rồi mới chấm điểm Bước 6.

## Cách dùng cho video TTC

Chi tiết xuyên suốt gợi ý: một chấm màu nhấn của TTC (theo nhận diện ĐHTL, xem `video-khoa-hoc/phong-cach.md`) bắt đầu ở nút "Đăng ký" rồi theo từng cảnh: tên khóa, biểu đồ kết quả, hình khối, thẻ cuối kèm cách đăng ký. Số liệu trên màn hình (phần trăm, số học viên) chỉ dùng số PM cung cấp có nguồn.

## Bài học chạy thử đầu tiên (video TTC "Chấm đỏ", 8/10/2026)

- **Đo chữ bằng canvas phải chờ phông tải xong.** HyperFrames có thể gọi `seek(t)` trước khi phông tải; nếu nhớ số đo của phông dự phòng thì chữ lớn dính nhau trong video nhưng vẫn đẹp ở ảnh chụp bằng Playwright. Cách làm: chỉ nhớ số đo khi `document.fonts.check(...)` đúng. Kiểm bằng `hyperframes snapshot --at <giây>` chứ không chỉ ảnh Playwright.
- **Gắn thẻ màu bt709 sau khi dựng** (`ffmpeg -c copy -bsf:v h264_metadata=matrix_coefficients=1:colour_primaries=1:transfer_characteristics=1`), nếu không màu nhấn có thể hiện sẫm hơn ở vài trình phát.
- **Tệp `.mp4` bị `.gitignore`.** Video giao cho PM qua SendUserFile; trong kho chỉ giữ mã, bảng nhịp, ảnh tĩnh, mã tạo nhạc.
- **Dựng 15 giây ở 240 khung/giây mất khoảng 6 phút** trên máy phiên; chỉ dựng bản đủ sau khi PM duyệt 4 ảnh tĩnh, mỗi lần sửa nhỏ vẫn tốn một lượt dựng.
- **Prompt có chi tiết gắn vào một chữ cái (chấm trên chữ "i") thì phải đổi cho hợp tiếng Việt** (ở đây chấm đỏ thành dấu chấm cuối câu), và nói rõ khác biệt trong bảng nhịp.
