# Ví dụ: SonicRec (nhóm ứng dụng)

Ví dụ điền để học cách dùng kỹ năng, chưa phải kịch bản đã duyệt. Thông tin lấy từ bộ nhớ dự án (5/10/2026): `memory/projects/SonicRec_Remotion.md` và ghi chú giá, nhận diện SonicRec. Marketing SonicRec làm ở kho `HaiTLU/sonicrec-congty` (`marcom/`); làm thật thì chép kịch bản sang đó.

## Đầu vào

- Sản phẩm: SonicRec (sonicrec.app), nhóm ứng dụng; chạy trên Mac, bản Windows đang thử.
- Người mua: người ghi biên bản họp ở trường học, công ty nhỏ.
- Vấn đề bằng lời của họ: "Họp xong lại mất cả buổi gõ biên bản."
- Lời hứa: Họp xong là có biên bản Word.
- Mục tiêu: ra mắt. Nơi đăng: Reels, TikTok, Zalo. Khổ: 9:16 trước, sau đó 16:9. Độ dài: 20 giây.
- Bằng chứng: **chưa có số đo có nguồn** (cần PM đo: một buổi họp dài bao lâu, ra biên bản mất bao lâu, đo trên máy nào, ngày nào). Trong lúc chờ, nhịp bằng chứng dùng cảnh trang Word đầy đủ hiện ra.
- Lời kêu gọi: "Dùng thử miễn phí 30 ngày" và sonicrec.app.
- Giá (không bắt buộc): 50.000 đồng/tháng (PM quyết 4/10/2026).
- Nhận diện: nền xanh than `#02152a`, xanh ngọc `#06e3d8`, đỏ `#fe301c`, trắng; chữ "Rec" luôn đỏ khi "Sonic" trắng; gọi người xem là "bạn".
- Phương án mở đầu (giả định để minh họa): mở bằng vấn đề.
- Phong cách (giả định): một khối đổi hình xuyên suốt, nền tối.

## Tài liệu

| Tệp | Nguồn | Ghi chú |
|---|---|---|
| assets/ui-cho-ghi.png | Dựng lại bằng HTML dữ liệu mẫu (`marcom/remotion/ui/` ở sonicrec-congty) | Không dùng đoạn quay có tên thiết bị, tên người |
| assets/ui-dang-ghi.png | Như trên, theo đoạn quay 12.56.48 | Chấm đỏ ĐANG GHI ÂM, đồng hồ, sóng, nút Đánh dấu |
| assets/word-bien-ban.png | Dựng lại trang Word bằng chữ mẫu | Không lấy trang thật có đầu văn bản Trường |
| assets/logo.svg | `marcom/logo/bo-logo/` | Logo tam giác chuẩn |

## Danh sách trạng thái (120 nhịp/phút, 10 ô nhịp)

| Ô nhịp.nhịp | Giây | Trạng thái trên hình | Chữ | Chuyển động | Âm thanh |
|---|---|---|---|---|---|
| 1.1 | 0,0 | Nền xanh than, chồng giấy trắng rơi xuống chất cao giữa khung | "Họp 1 tiếng." | Giấy rơi lò xo nặng, mỗi tờ một nhịp con | Thịch nhẹ mỗi tờ |
| 1.3 | 1,0 | Chồng giấy cao gấp đôi, đồng hồ góc chồng giấy quay nhanh | "Gõ biên bản 3 tiếng." | Chữ thay chữ sau lớp mờ ngắn | Tiếng tích tắc nhanh |
| 2.1 | 2,0 | Chồng giấy co lại thành một khối bo góc màu xanh ngọc | | Khối đổi hình, máy quay phóng nhẹ | Lướt |
| 2.3 | 3,0 | Khối thành cửa sổ SonicRec chờ ghi (ảnh ui-cho-ghi) | "Sonic**Rec**" (Rec đỏ) | Cửa sổ lắp từng mảnh: khung, thanh bên, nút Ghi | Bấm nhẹ mỗi mảnh |
| 3.1 | 4,0 | Con trỏ đi từ dưới phải tới nút Ghi, bấm | | Con trỏ cong, chậm dần trước khi bấm | Bấm |
| 3.3 | 5,0 | Nút Ghi co thành chấm đỏ, đồng hồ chạy, sóng âm hiện (ảnh ui-dang-ghi) | "Bấm ghi. Cứ họp." | Khối đổi hình; sóng chạy theo nhạc | Nhịp trống vào |
| 4.1-5.4 | 6,0-9,9 | Máy quay phóng vào nút Đánh dấu chỗ quan trọng; con trỏ bấm hai lần, mỗi lần một cờ nhỏ cắm vào dải sóng | "Đánh dấu chỗ quan trọng" | Cờ bật lò xo cứng | Ting mỗi cờ, đúng nhịp |
| 6.1-6.4 | 10,0-11,9 | Con trỏ bấm "Dừng và soạn biên bản"; thanh tiến trình chạy | "Dừng. Soạn biên bản." | Nút đổi thành thanh tiến trình (cùng khối) | Lướt dài |
| 7.1-8.2 | 12,0-14,9 | Thanh tiến trình nở thành trang Word đầy chữ, cuộn nhẹ qua mục Việc cần làm (ảnh word-bien-ban) | "Biên bản Word, có danh sách việc." | Khối nở thành trang, máy quay lùi | Thịch ở nhịp mạnh ô 7 |
| 8.3-9.1 | 15,0-16,0 | Nhịp bằng chứng: chờ số đo của PM; tạm thời trang Word phóng to tên mục, dấu tích đỏ hiện cạnh | "Họp xong là có biên bản." | Dấu tích lò xo cứng | Ting |
| 9.1-10.4 | 16,0-20,0 | Trang Word co lại thành logo tam giác; dưới logo là tên, lời kêu gọi, đường dẫn; đứng yên từ 17,0 | "Dùng thử miễn phí 30 ngày" / "sonicrec.app" | Logo lò xo nặng, không nảy; chữ vào sau logo | Hợp âm kết |

## Kiểm thời gian đọc (mẫu)

| Dòng chữ | Ký tự | Cần (giây) | Có (giây) | Đạt |
|---|---|---|---|---|
| Họp 1 tiếng. | 12 | 2,3 | 1,0 | Không: gộp với dòng sau thành một câu hai vế, giữ 2,4 giây |
| Đánh dấu chỗ quan trọng | 23 | 3,0 | 4,0 | Đạt |
| Dùng thử miễn phí 30 ngày | 25 | 3,2 | 3,0 | Không: bắt đầu đứng yên từ 16,6 |

Bảng kiểm phát hiện hai dòng không đạt ngay trên giấy, trước khi viết mã. Cũng vì vậy "Họp 1 tiếng" và "3 tiếng" là số giả định để minh họa: làm thật phải có số đo của PM, không có thì đổi câu mở thành câu không có số ("Họp xong lại ngồi gõ biên bản?").

## Kiểm theo khung

- Sản phẩm thật xuất hiện ở giây 3: đạt (trước giây 6).
- Ba điều làm được (ghi, đánh dấu, ra Word) đều có trong bản đang phát hành v2.11: đạt.
- Không nêu Windows là đã có (chỉ "đang thử"): đạt vì không đưa vào chữ.
- Nhịp bằng chứng chưa có nguồn: ghi rõ, chờ PM.
