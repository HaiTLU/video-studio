# Giọng đọc và linh vật

Tùy chọn, mặc định tắt. Chỉ làm khi PM chọn có trong hộp hỏi ở Bước 1. Bài nguồn (mục 04) kể một bản quảng cáo có nhân vật nói, giọng làm bằng dịch vụ ElevenLabs; tác giả bản đó nay bán "giọng đọc cộng linh vật" như một dịch vụ.

## Giọng đọc

**Hỏi PM trong một hộp:**

1. Nguồn giọng:
   - **VieNeu-TTS (khuyến nghị, PM duyệt chất lượng 8/10/2026):** mã nguồn mở Apache 2.0 (`github.com/pnnbao97/VieNeu-TTS`), chạy trên CPU ở máy Mac hoặc phiên web, không gửi chữ ra ngoài; 25 giọng có sẵn (Bắc, Trung, Nam; nam, nữ), đọc được câu xen tiếng Anh. Giọng mặc định của TTC là **Hải Đăng** (nam, Bắc, tự nhiên). Tạo giọng bằng `scripts/loi_doc_vieneu.py` (cách cài và lỗi onnxruntime ghi đầu tệp). Đo 8/10/2026: Hải Đăng đọc khoảng 3,7 âm tiết mỗi giây, máy 4 nhân mất gần bằng độ dài câu để tạo.
   - Giọng có sẵn trên máy Mac: miễn phí, chạy trên máy. Kiểm có giọng tiếng Việt bằng `say -v '?' | grep -i vi_VN`; chất giọng máy, nghe rõ là giọng tổng hợp.
   - Dịch vụ giọng AI (ElevenLabs hoặc tương tự): giọng tự nhiên hơn, tốn phí theo số ký tự, có điều khoản dùng thương mại riêng. PM tự tạo tài khoản và lưu khóa vào biến môi trường (ví dụ `ELEVENLABS_API_KEY` trong tệp `.env` không đưa lên git); Claude không đăng ký thay, không dán khóa vào câu lệnh hay ảnh chụp.
   - PM tự thu giọng: tốt nhất về độ tin; Claude chỉ cắt, chuẩn hóa âm lượng, khớp nhịp.
2. Giọng nam hay nữ, miền nào, tốc độ.
3. Lời đọc: PM viết, hay Claude viết rồi PM duyệt.

**Không nhân bản giọng người thật** (kể cả giọng PM, giảng viên, khách) khi chưa có đồng ý rõ ràng bằng văn bản của chính người đó. VieNeu nhái được giọng từ mẫu 3-5 giây, nên luật này áp dụng cả cho VieNeu.

Không dùng VibeVoice (Microsoft) và các bản sao lưu của nó: không đọc được tiếng Việt, chỉ dành cho nghiên cứu, kho gốc đã bị gỡ vì bị dùng làm giọng giả (PM xem 8/10/2026).

Phương án dự phòng, chưa dùng (PM chốt 10/10/2026): **VoiceStudio** (`github.com/debpalash/VoiceStudio`, AGPL-3.0, chạy trên máy). Chỉ cân nhắc khi cần nhân bản giọng hoặc lồng tiếng sang ngôn ngữ khác, hai việc VieNeu không làm. Tiếng Việt có trong danh sách 646 ngôn ngữ của mô hình OmniVoice (k2-fsa, Apache 2.0, `docs/languages.md` dòng 607), chưa nghe thử chất lượng. Cần GPU từ 6 GB VRAM (CPU chạy được nhưng chậm), phiên web không chạy được. Mỗi mô hình có giấy phép riêng, kiểm trước khi dùng thương mại; luật không nhân bản giọng người thật ở trên vẫn áp dụng.

**Viết lời đọc**

- Lời đọc đi cùng kịch bản, thêm một cột "Lời đọc" trong danh sách trạng thái. Tốc độ tiếng Việt khoảng 3-3,7 âm tiết mỗi giây (3,7 là số đo trên giọng Hải Đăng của VieNeu; giọng khác thì đo lại bằng `vo_do-dai.json`); 20 giây chứa được khoảng 45-55 âm tiết nếu chừa chỗ thở.
- Lời đọc không lặp đúng chữ trên màn hình; chữ trên màn hình là ý chính, lời đọc nói thêm cảm xúc hoặc cách dùng.
- Câu ngắn, động từ trước. Không dùng từ "nhất", "số một" khi không có chứng minh (luật như phần chữ).
- Video vẫn phải hiểu được khi tắt tiếng: luôn có phụ đề hoặc chữ chính trên hình.

**Ghép giọng vào phim**

1. Tạo tệp giọng từng câu riêng (`vo_01.wav`, `vo_02.wav`...), đo độ dài từng câu.
2. Đặt câu vào lưới nhịp: câu bắt đầu ở nhịp, kết thúc trước khoảnh khắc lớn tiếp theo. Câu dài hơn chỗ trống thì sửa lời, không tăng tốc giọng quá 10%.
3. Hạ nhạc nền khi có giọng (giảm khoảng 8-10 dB quanh mỗi câu), rồi chuẩn hóa cả bản về -14 LUFS.
4. Phụ đề lấy từ chính lời đọc, hiện theo câu.

## Linh vật (nhân vật đại diện)

**Hỏi PM:** đã có linh vật chưa (có bản vẽ thì dùng bản vẽ đó); muốn kiểu gì (hình khối đơn giản, nét vẽ tay, 3D); linh vật có nói không.

**Bảng nhân vật** (`docs/nhan-vat.md`, viết trước khi dựng, mọi cảnh đọc lại):

| Mục | Ghi gì |
|---|---|
| Tỷ lệ | Cao bao nhiêu đầu; đầu, thân, tay so với nhau |
| Bảng màu | Mã hex lấy từ bản vẽ gốc; một màu nhận dạng không đổi |
| Phần nhận dạng không đổi | Ví dụ tai nghe, chấm đỏ, hình sóng âm trên ngực; còn nguyên dù đổi phong cách |
| Nét mặt | Danh sách 4-6 nét: bình thường, vui, ngạc nhiên, nghĩ, nói (miệng mở 3 mức) |
| Dáng | Đứng, chỉ tay, vẫy, cầm sản phẩm |
| Lò xo | Nảy thấy rõ (nhóm "vui"), khác lò xo của giao diện |
| Cấm | Giống nhân vật có bản quyền; giống người thật |

**Dựng**

- Vẽ bằng mã (SVG hoặc canvas) thành các bộ phận rời có khớp (đầu, thân, tay, mắt, miệng) để chuyển động bằng lò xo; vẫn là hàm của thời gian `t`.
- Miệng khớp giọng: đo độ lớn âm của tệp giọng theo từng khung (ví dụ 60 lần mỗi giây), lưu `mouth.json`; độ mở miệng lấy từ đó, chia 3 mức. Không cần khớp từng âm.
- Mắt chớp theo bộ sinh số có hạt giống cố định, mỗi 2-4 giây một lần.
- Linh vật tương tác với sản phẩm thật (cầm hộp, chỉ vào nút), không thay thế sản phẩm.
- Có thể học cách dựng nhân vật nét vẽ tay ở plugin `claude-animation-skill` (buildwithhanif, bài nguồn mục 02); chưa kiểm giấy phép nên chỉ học cách làm, không chép mã khi chưa đọc giấy phép.
