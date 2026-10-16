# Học công thức từ video mẫu PM gửi

Mục tiêu: biến một video đẹp thành một "công thức" (nhịp, cảnh, chuyển cảnh, màu, chữ, lò xo) lưu ở `cong-thuc/`, để trộn vào ý tưởng mới. Không chép video: video và câu lệnh của người khác thuộc người tạo, chỉ học cách làm, thay chữ, hình, thương hiệu, không mạo danh.

## Các bước

1. Gọi kỹ năng `watch` trên tệp hoặc đường dẫn (chạy trên máy, không gửi video ra ngoài). Nếu bị chặn (YouTube đòi đăng nhập...) thì nói rõ, tìm bản tóm tắt cùng tiêu đề, ghi "chưa xác nhận trùng video".
2. Tách khung 0,25 giây một ảnh (hoặc 0,1 giây ở chỗ chuyển cảnh): `ffmpeg -i v.mp4 -vf fps=4 khung_%03d.png`, ghép lưới để xem.
3. Ghi vào bảng của `cong-thuc/_mau.md`: độ dài, nhịp ước lượng (đếm cú nhấn trong 10 giây rồi nhân 6), số cảnh, vật nối, 3 màu chủ đạo (lấy bằng `ffmpeg ... -vf palettegen` hoặc đọc điểm ảnh), phông và cỡ chữ, loại chuyển cảnh, loại chuyển động (lò xo hay đều), điểm nhấn nhìn thấy rõ nhất.
4. Rút ra 3 điều "làm cho video này đẹp" và 1 điều "tôi sẽ làm khác" cho Trường.
5. Lưu `cong-thuc/<ten-ngan>.md`, ghi nguồn (đường dẫn, tác giả nếu biết, ngày xem, giấy phép nếu có) và ghi một dòng vào `../so-y-tuong.md`.
6. Hỏi PM bằng hộp: áp dụng ngay vào video sắp làm, hay chỉ lưu.

## Nếu PM chỉ gửi câu lệnh (prompt) chứ không có video

Đọc như một bản chỉ đạo: tách thành 6 khối (inputs, direction, structure, build, gotchas, start), ghi chỗ nào hay (vật nối, danh sách cấm, cổng duyệt), chỗ nào không hợp tiếng Việt hoặc nhận diện Trường, rồi lưu thành công thức như trên.
