# Ngân hàng ý tưởng

Dùng ở Bước 1 để đề xuất ý. Một ý = một **vật nối** + một **thể loại** + một câu mô tả cảnh mở và cảnh cuối. Mỗi video chọn khác lần trước (xem `../so-y-tuong.md`). Thêm mục mới vào đây khi nghĩ ra, đừng xóa mục cũ.

## Vật nối (thứ đi xuyên mọi cảnh)

| Vật nối | Hợp với | Cách biến đổi qua các cảnh |
|---|---|---|
| Chấm (đã dùng: TTC "Chấm đỏ") | Mọi nội dung | Núm nút, dấu chấm câu, đầu đường biểu đồ, đĩa phủ khung, chấm tâm |
| Đường kẻ | Lộ trình, quy trình, kế hoạch | Gạch chân, trục biểu đồ, đường chân trời, sợi dây, nét bút |
| Chữ cái | Thương hiệu, tên đơn vị | Một chữ cái rơi, thành ô vuông, thành nhân vật, thành logo |
| Ô vuông (ô trang tính) | Số liệu, báo cáo, quản lý dự án | Ô Excel nhảy giá trị, thành thẻ, thành khối nền |
| Con trỏ | Phần mềm, kỹ năng số, AI | Con trỏ vẽ, chọn, kéo mọi thứ; cảnh nào cũng do con trỏ gây ra |
| Sóng âm | Bài giảng, hội thảo, âm nhạc | Sóng thành đường biểu đồ, thành nét chữ |
| Thẻ bài | Danh mục khóa, nhân sự, đối tác | Thẻ lật, xếp chồng, xòe quạt, thành lưới |
| Kim đồng hồ | Hạn, lịch khai giảng, tiến độ | Kim quét thành vòng cung, thành biểu đồ tròn, thành chữ số |
| Mũi tên | Tăng trưởng, hành trình | Mũi tên gãy khúc thành đường đi, thành chữ "→" trong thẻ cuối |
| Nét vẽ tay (dựng bằng đường cong) | Sáng tạo, thiết kế | Nét phác thành khung, thành bố cục, thành thẻ cuối |

## Thể loại (cách kể)

| Thể loại | Đặc điểm | Dựng bằng |
|---|---|---|
| UI biến hình | Một khối đổi qua nút, thanh trượt, công tắc, biểu đồ (xem `/video-ui-bien-hinh`) | Canvas, lò xo |
| Biểu đồ động | Số liệu thành hình, chấm chạy theo đường lò xo | Canvas, cùng hàm lò xo cho chấm và đường |
| Chữ động | Chữ cái tự xếp, xoay vòng, tan thành chấm | Canvas, từng chữ cái riêng |
| Phẳng 3D (isometric) | Khối đẻ ra từ lưới, xoay một trục | Canvas, phép chiếu tự tính |
| Bản đồ hành trình | Đường đi qua các điểm mốc | Canvas, đường cong lò xo |
| Sổ tay phác thảo | Nét bút, ô, ghi chú tự hiện | Đường cong, nét đứt |
| Trang tính sống | Lưới ô, ô nhảy số, ô phình thành thẻ | Canvas, lưới |
| Bảng tin / tờ lịch | Trang lật, thẻ ngày | Canvas |
| Lưới chấm bán sắc | Chấm đổi cỡ theo khoảng cách | Canvas, vòng lặp lưới |

## Bảng ghép để ra ý lạ

Chọn một vật nối ở hàng và một thể loại ở cột; ô chứa gợi ý cảnh. Ô trống: tự nghĩ.

| | UI biến hình | Biểu đồ động | Chữ động | Sổ tay phác thảo | Trang tính sống |
|---|---|---|---|---|---|
| Chấm | (làm rồi: Chấm đỏ) | Chấm là điểm dữ liệu chạy theo lò xo | Chấm là dấu chấm câu bay giữa các từ | Chấm là đầu bút | Chấm là ô được chọn |
| Đường kẻ | Đường kẻ thành thanh trượt | Đường kẻ là trục rồi thành đường tăng | Gạch chân quét qua từng từ | Đường kẻ là nét phác đầu tiên | Đường kẻ là viền ô lan thành lưới |
| Chữ cái | Chữ cái thành nút | Chữ cái là nhãn bay ra khỏi cột | Một chữ cái "K" sinh ra cả từ | Chữ cái tập viết rồi lên nét | Chữ cái ở góc ô, ô phình ra |
| Con trỏ | Con trỏ làm mọi thứ (kiểu video giao diện) | Con trỏ kéo cột lên | Con trỏ gõ từng chữ | Con trỏ vẽ khung | Con trỏ kéo công thức |
| Kim đồng hồ | Kim thành thanh tiến trình | Kim quét thành biểu đồ tròn | Kim chỉ từng chữ số ngày khai giảng | Kim là nét gạch đếm | Kim đi qua từng ô ngày |

Ý lạ tốt thường là ô mà vật nối làm một việc *khác công dụng quen* của nó (đường kẻ là nhân vật chính, chữ cái là nhịp).

## Luật cấm chung (đưa vào khối direction)

Không video kho, không chuyển sắc (gradient), không phát sáng, không hạt tung tóe, không chuyển cảnh ngẫu nhiên, không chuyển động không gắn với một phần tử đang có trên màn hình, không easing nảy quá (lò xo vọt tối đa khoảng 2 phần trăm ở UI; biểu đồ được vọt rõ hơn). Một màu nhấn duy nhất.

## Cách viết ý gợi ý cho PM

Mỗi ý ghi trên một dòng: **Tên ngắn.** Vật nối + thể loại. Cảnh mở: ... Cảnh cuối: ... Hợp với: ... (nội dung nào của TTC, AI Lab, Viện). Không hứa điều chưa dựng được trong một lượt.
