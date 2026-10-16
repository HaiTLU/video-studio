# Sổ từ cấm

Danh sách duy nhất các từ và kiểu viết PM đã cấm. Hook `.claude/hooks/chan-tu-cam.py` đọc bảng dưới mỗi lần Claude ghi tệp:

- Mức `chặn`: hook không cho ghi, Claude phải sửa rồi ghi lại.
- Mức `nhắc`: tệp vẫn được ghi, hook nhắc Claude xem lại (dùng cho từ có nghĩa thường hợp lệ, ví dụ "mạch máu").
- Loại tệp `chữ`: .md, .txt, .html, .js, .jsx, .ts, .tsx, .py, .json, .csv, .xml. Loại `office`: chỉ .py và .xml (mã dựng tệp Word).

Hook chỉ xét chữ mới thêm vào: chữ cũ có sẵn trong tệp không bị chặn, chỉ sửa khi PM nhờ. Trong tệp .md và .txt, chữ trong dấu ngoặc kép hoặc dấu ` ` được bỏ qua (trích nguyên văn). Dòng có chữ `nguyen-van` cũng được bỏ qua, dùng khi phải ghi đúng lời người khác trong mã dựng biên bản.

**PM nhắc thêm một từ thì thêm một dòng vào bảng** (cột Mẫu là biểu thức chính quy Python, không phân biệt hoa thường), rồi tăng số lần trong `memory/context/so-loi-lap.md`. Hook không cần sửa.

Từ cấm áp cho mọi chữ Claude viết ra, kể cả trả lời trong chat. Chat không chặn được vì PM đã đọc rồi mới kiểm; hook `.claude/hooks/nhac-tu-cam-chat.py` dò câu trả lời vừa xong (cả mức chặn và nhắc) và nhắc Claude ở lượt sau. Hook này có thể sót đoạn chữ đứng ngay trước hộp hỏi PM, vì transcript không lưu đoạn đó dưới dạng chữ; Claude vẫn tự rà.

## Bảng

| Mẫu | Mức | Tệp | Thay bằng | PM nhắc |
|---|---|---|---|---|
| (?<!then )(?<!mấu )(?<!chủ )chốt(?! chặn) | chặn | chữ | quyết, đồng ý, chọn, duyệt, xác nhận, thống nhất | 13/9, 4/10, lọt 5/10 |
| (?<![-\w])neo(?![-\w]) | chặn | chữ | gắn vào, căn cứ, mốc, dựa vào | 11/9 (hai lần) |
| nút thắt | chặn | chữ | việc khó nhất, chỗ khó nhất | 10/9 |
| trụ đỡ | chặn | chữ | nguồn thu chính, chiếm phần lớn | 10/9 |
| đòn bẩy | chặn | chữ | giúp tăng, làm tăng | 10/9 |
| điểm sáng | nhắc | chữ | có kết quả tốt hơn (giữ khi nói ánh sáng) | 10/9 |
| mũi nhọn | nhắc | chữ | mảng chính, mảng lớn nhất (giữ "công nghệ mũi nhọn" trong văn bản chính sách) | 10/9 |
| bệ phóng(?! sự nghiệp)\|cú hích | chặn | chữ | điều kiện cần, làm cho ... tăng (giữ tên khóa "Bệ phóng sự nghiệp") | 10/9 |
| bứt phá | chặn | chữ | tăng nhanh | 10/9 |
| chuyển mình | chặn | chữ | thay đổi | 10/9 |
| khơi thông | chặn | chữ | mở, gỡ | 10/9 |
| chạm (mốc\|chỉ tiêu\|tới con số) | chặn | chữ | đạt mốc, đạt chỉ tiêu, đạt được con số | 10/9 |
| văn bản đẹp | chặn | chữ | có đủ giấy tờ nhưng... (nói thẳng nghĩa) | 10/9 |
| (đợt\|cuộc) hỏi(?! ý) | chặn | chữ | khảo sát, phỏng vấn, lần khảo sát | 12/9 |
| gánh điểm\|cứu điểm\|về đích\|xoay trục | chặn | chữ | bài để đủ điểm, được đăng, chuyển sang | 13/9 |
| điểm cần nhấn | chặn | chữ | cần lưu ý | nhãn slide |
| điểm nhấn | nhắc | chữ | cần lưu ý (giữ khi nói màu, bố cục thiết kế) | nhãn slide |
| lan tỏa | nhắc | chữ | mở rộng ra, ảnh hưởng tới | 10/9 |
| xương sống | nhắc | chữ | mảng chính (giữ khi nói về giải phẫu) | 10/9 |
| phép thử | nhắc | chữ | cách kiểm chứng (giữ khi là thuật ngữ thống kê) | 10/9 |
| đóng vai trò quan trọng | nhắc | chữ | ảnh hưởng tới, quyết định | 10/9 |
| (?<!\w)mạch(?!\w\| máu\| điện\| nước) | nhắc | chữ | nhóm, phần, lập luận | 13/9 |
| đường đi | nhắc | chữ | cách làm chính | 13/9 |
| đóng khung | nhắc | chữ | viết theo hướng | 13/9 |
| trả nợ | nhắc | chữ | làm đúng việc bài kia chỉ ra (giữ khi nói tiền) | 13/9 |
| dứt khoát | nhắc | chữ | bỏ từ này | 12/9 |
| ^#{1,6}\s*(hai\|ba\|bốn\|năm\|sáu\|bảy\|tám\|chín\|mười\|[2-9]\|1[0-9])\s+(câu hỏi\|nguyên tắc\|bước\|việc\|điều\|điểm\|nội dung\|yêu cầu\|nhóm\|mức\|quyền\|trách nhiệm\|lý do\|cách\|bài học\|lỗi) | nhắc | chữ | bỏ con số khỏi tiêu đề: "Nguyên tắc sử dụng AI" | 22/9 |
| <w:w\s\|OxmlElement\(['"]w:w['"]\) | chặn | office | nới cột, giảm cỡ chữ, ngắt dòng; không co giãn ký tự | 31/7 |
