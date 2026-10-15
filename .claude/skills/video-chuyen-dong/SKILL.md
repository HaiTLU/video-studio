---
name: video-chuyen-dong
description: Làm video chuyển động ngắn bằng mã (giới thiệu AI Lab, Viện nghiên cứu, hội thảo, đơn vị, sự kiện) theo bản chỉ đạo, có video mẫu để học phong cách, nhạc và tiếng động khớp nhịp, tự chấm điểm nhiều vòng. Dùng khi PM gõ /video-chuyen-dong hoặc nhờ "làm video giới thiệu ...", "làm video theo mẫu này", "video khớp nhạc". Với video quảng cáo khóa ngắn hạn TTC thì dùng /video-khoa-hoc; video quảng cáo, bán hàng, ra mắt một sản phẩm (ứng dụng, hàng hóa, dịch vụ) thì dùng /video-quang-cao-san-pham trước để viết kịch bản. Kỹ năng này cũng là phần dựng hình (HyperFrames, khớp nhịp, chấm điểm) cho hai kỹ năng đó.
---

# Video chuyển động theo bản chỉ đạo

Nội dung: Quan hệ với video-khoa-hoc; Bước 1 Bản chỉ đạo; Bước 2 Tài liệu thật; Bước 3 Học từ video mẫu; Bước 4 Bảng nhịp (kỹ thuật bổ sung); Bước 5 Nhạc và tiếng động; Bước 6 Chấm điểm; Bước 7 Đo sau khi đăng; Danh mục phong cách; Video dài; Thư mục; Lỗi hay gặp; Gợi ý model.

Nguồn: video "Opus 5.5 Makes Insane Videos. Here's the Full Workflow" (Lukas Margerie, YouTube 747ZnEtsRbg) và bài viết trên X của tác giả Moves mà video dẫn. PM gửi bản ghi lời thoại ngày 30/9/2026. Phần cách dựng lấy từ bản ghi đó; các con số thời gian, chi phí, dịch vụ tài trợ trong video là lời tác giả, kỹ năng này không dùng làm căn cứ.

## Quan hệ với video-khoa-hoc

- **Cách dựng, bộ màu, phông, logo, thư mục lưu, rà từng giây P0-P2**: theo `.claude/skills/video-khoa-hoc/SKILL.md` và `phong-cach.md` của kỹ năng đó. Không chép lại ở đây.
- **Kỹ năng này thêm 5 việc**: bản chỉ đạo, học phong cách từ video mẫu, bảng nhịp trước khi viết mã, nhạc và tiếng động khớp nhịp, chấm điểm nhiều vòng.
- Dựng bằng HyperFrames theo `video-khoa-hoc/dung-hyperframes.md` (PM chốt 8/10/2026, thay cách cũ Playwright chụp, ffmpeg ghép). Không cài thêm khung dựng nào khác trừ khi PM yêu cầu.

## Ý chính

Lời dặn ngắn chỉ quyết định khoảng một phần mười kết quả. Phần còn lại nằm ở khung làm việc: quy tắc dựng hình, luật cấm đồ họa chung chung, âm thanh, và vòng phê bình. Mọi video làm bằng kỹ năng này đều đi qua đủ 6 bước dưới đây.

## Bước 1 - Bản chỉ đạo

Gom đủ 9 mục. Thiếu mục nào thì hỏi PM **một lần** bằng hộp thoại (`AskUserQuestion`), không viết câu hỏi thành chữ. Chỉ dùng thông tin PM đưa, không bịa.

| Mục | Ví dụ |
|---|---|
| Phim trong một câu | Giới thiệu AI Lab TLU x NIC cho đối tác trong 20 giây |
| Người xem và thông điệp | Lãnh đạo đối tác; "Thăng Long có phòng thí nghiệm AI thật" |
| Khổ và độ dài | 16:9, 20 giây (thêm 9:16 nếu đăng mạng xã hội) |
| Video hoặc ảnh mẫu | 1-2 tệp PM gửi (không bắt buộc) |
| Bộ nhận diện | Mặc định ĐHTL: màu, phông, logo theo `video-khoa-hoc` |
| Chữ trên màn hình | Do PM cung cấp, chép nguyên văn |
| Điều không muốn | Không chữ chạy, không nền đỏ (không bắt buộc) |
| Công cụ được dùng | Mặc định: HyperFrames (HTML, GSAP), PM chỉnh trong Studio |
| Sản phẩm giao | Tệp MP4, ảnh đại diện, bảng nhịp, mã nguồn |

**Luôn hỏi phong cách (PM dặn 3/10/2026).** Mỗi lần dựng video, kể cả khi PM đã gửi video mẫu, đưa một câu trong hộp thoại để PM chọn phong cách từ mục "Danh mục phong cách có sẵn" bên dưới: chọn 3 phong cách hợp nội dung nhất (mỗi lựa chọn ghi phong cách đó hợp với gì), phong cách khuyến nghị đứng đầu; PM có video mẫu thì thêm lựa chọn "Theo video mẫu". Không tự chọn thay PM.

**Gợi ý mẫu đẹp, đúng ý (PM dặn 3/10, nâng cấp 10/10/2026).** Trước hộp hỏi phong cách, tìm các mẫu gần nhất với nội dung cần dựng trong thư viện đã lưu sẵn `tai-lieu/thu-vien-prompt-skillry.md` (279 prompt đầy đủ trên 513 video Opus 5.5, nguồn `yihui-dev/awesome-opus5-5-videos`), không cần tải lại: `python3 -I .claude/skills/video-chuyen-dong/scripts/tim_mau_skillry.py "<từ khóa tiếng Anh>" ... [--nhom motion|explainer|3d|interactive] --top 5`. Từ khóa lấy từ nội dung video (vd course, launch, data, timeline, logo, typography); chạy 2 lượt với bộ từ khóa khác nhau nếu lượt đầu ít kết quả. Từ 5 kết quả chọn **3 mẫu hợp nhất**, ưu tiên: đúng loại video (khóa học, sản phẩm, giải thích), đúng độ dài và nhịp cần, mẫu dùng HyperFrames hoặc svg, gsap (khớp cách dựng của kho), prompt đủ ý để học. Trong tin nhắn trước hộp, mỗi mẫu một dòng: tác giả, video làm gì, vì sao hợp (một câu), đường dẫn `skillry_url` để PM bấm xem. Trong hộp: 2 phong cách từ danh mục bên dưới + 1 lựa chọn "Theo mẫu Skillry <tác giả>" (mẫu gần nhất) + "Theo video mẫu" nếu PM có, tối đa 4 lựa chọn. PM chọn mẫu thì đọc câu lệnh để học cách làm (bố cục, chuyển cảnh, nhịp, kỹ thuật); câu lệnh và video thuộc người tạo, không chép nguyên văn, màu và phông vẫn theo nhận diện ĐHTL hoặc sản phẩm. Thư viện cũ quá 1 tháng thì tải lại `data/videos.json` từ kho nguồn để cập nhật.

## Bước 2 - Tài liệu thật của thương hiệu

- Dùng ảnh chụp màn hình thật của sản phẩm hoặc trang web (chụp bằng `playwright-cli`), logo thật từ tệp có sẵn. Không tự vẽ lại logo, không bịa giao diện ứng dụng.
- Sản phẩm của bên khác (đối tác, NIC): chỉ dùng tài liệu công khai hoặc do họ đưa; ghi nguồn trong bản chỉ đạo.
- Hình trang trí và biểu tượng cho video sản phẩm (SonicRec), không dùng cho video ĐHTL vì nhận diện Trường chỉ dùng Indigo và Scarlet (PM chọn 3/10/2026, nguồn: reel Aminul Islam):
  - Coolshapes (`coolshap.es`, mã `github.com/realvjy/coolshapes-react`, giấy phép MIT): hơn 100 hình khối trừu tượng dạng SVG, đổi màu được theo màu sản phẩm.
  - Iconsax (`iconsax.io`): khoảng 6.000 biểu tượng miễn phí, dùng thương mại được, không bắt ghi nguồn (docs.iconsax.io/license-and-terms/license). Dùng bản miễn phí, không dùng bản trả phí.
  - Moving Icons (`movingicons.dev`, mã `github.com/jis3r/icons`, giấy phép MIT, thêm 4/10/2026): hơn 500 biểu tượng Lucide có chuyển động, viết cho Svelte. Video ở đây dựng bằng HyperFrames nên không cài gói Svelte; lấy đường SVG và học cách chuyển động, rồi viết lại bằng GSAP trên dòng thời gian để khớp nhịp. Chép mã thì giữ dòng ghi bản quyền MIT trong bản chỉ đạo.
  - LottieFiles (`lottiefiles.com`, giấy phép Lottie Simple, thêm 4/10/2026, nguồn dự phòng khi Moving Icons không có hình cần dùng): hoạt ảnh định dạng Lottie (tệp JSON). Được dùng thương mại và sửa, không bắt ghi nguồn; cấm bán lại hay đăng lại nguyên tệp như một tệp riêng. Mỗi hoạt ảnh có thể có giấy phép riêng ghi trên trang, đọc trước khi tải. HyperFrames phát và tua Lottie sẵn (`hyperframes-animation/adapters/`), không tự viết `goToAndStop`. Không dùng 3 trang còn lại trong reel: lordicon.com (bản miễn phí cấm sửa, bắt ghi nguồn), useanimations.com (CC-BY, bắt ghi nguồn), lottieflow.com (chỉ cho Webflow).
  - Ghi tên bộ đã dùng vào bản chỉ đạo; không dùng hình thay cho logo hay ảnh chụp giao diện thật.

## Bước 3 - Học phong cách từ video mẫu

Chỉ làm khi PM có video mẫu. Video mẫu phải do PM gửi tệp hoặc đường dẫn tải được; đường dẫn bị chặn (như YouTube đòi đăng nhập) thì nhờ PM gửi tệp.

1. Tách khung hình mỗi 0,5 giây: `ffmpeg -i mau.mp4 -vf fps=2 mau_%03d.png`, xem từng ảnh.
2. Viết `phong-cach-<ten>.md` gồm: bảng màu, kiểu chữ, độ dài từng cảnh, kiểu chuyển cảnh, chuyển động máy quay, kết cấu (hạt nhiễu), cách chữ vào và ra.
3. Chỉ học **cách làm** (nhịp, bố cục, chuyển cảnh). **Không** lấy nội dung, logo, nhân vật, câu chữ hay hình của video mẫu. Bản chỉ đạo ghi rõ điều này.
4. Video mẫu của người khác mà PM định đăng lại theo phong cách gần giống: nhắc PM cân nhắc bản quyền và nhờ bộ phận truyền thông duyệt.

## Bước 4 - Bảng nhịp trước khi viết mã

Lập bảng từng đoạn thời gian, **dừng cho PM duyệt** rồi mới viết mã. Video có một chi tiết xuyên suốt (một chấm hay một khối đi qua mọi cảnh) thì viết bản chỉ đạo theo mẫu 6 khối ở `mau-prompt-6-khoi.md` và đưa thêm 4 ảnh tĩnh (một ảnh mỗi cảnh chủ chốt) cùng bảng nhịp trước khi dựng bản đủ (PM duyệt 8/10/2026):

| Giây | Trạng thái (ở đâu, đang làm gì) | Chữ | Chuyển động | Âm thanh |
|---|---|---|---|---|

- Câu lệnh giao cho Claude mô tả **kết quả nhìn thấy** và nêu phong cách ngay câu đầu, chứ không chỉ định kỹ thuật.
- Kèm danh sách thành phần dùng lại (nút, thanh tiến trình, dấu tích, biểu đồ, thẻ) để hình đồng nhất.
- Với video giới thiệu ứng dụng: mỗi trạng thái nên là cùng một phần tử đổi kích thước, bo góc, màu, còn nội dung bên trong đổi qua một lớp mờ ngắn. Tránh cắt cảnh liên tục.
- Cảnh nào quan trọng ghi rõ thời gian giữ yên (xem `phong-cach.md` của `video-khoa-hoc`).
- Video khớp nhạc: tính sẵn mốc cắt theo nhịp bằng `node .claude/skills/video-chuyen-dong/scripts/beatgrid.mjs --bpm 120 --fps 30 --length 24 --chapters "Mở đầu:8, Nội dung:24, Flurry:8, Kết:rest"`. Độ dài mỗi đoạn tính bằng nhịp; đoạn tên bắt đầu bằng `Flurry` thì liệt kê mốc cắt mỗi nhịp rồi mỗi nửa nhịp. Dán bảng in ra vào bảng nhịp; trong GSAP, giây = khung / fps. Bố cục mẫu cho 15 giây ở khoảng 129 BPM: khoảng 75% phần phát triển, 13% cắt nhanh, 12% chốt lại. Nguồn và giấy phép MIT: `scripts/NGUON.md` (PM duyệt 10/10/2026).

### Kỹ thuật chuyển động bổ sung (PM duyệt 3/10/2026)

Học từ danh sách `github.com/yihui-dev/awesome-opus5-5-videos` (475 video làm bằng Opus 5.5 kèm câu lệnh; danh sách giấy phép MIT, câu lệnh và video thuộc người tạo nên chỉ học cách làm). Áp dụng khi viết mã ở Bước 5:

- **Mờ chuyển động:** khi xuất bản cuối, dựng ở 240 khung/giây rồi trộn 4 khung thành 1 (lệnh trong `video-khoa-hoc/dung-hyperframes.md`). Bản nháp xem nhanh thì bỏ qua cho đỡ tốn thời gian.
- **Chữ không chồng nhau:** nội dung bên trong chỉ vào sau khi khối chứa đã bắt đầu đổi hình, và rời đi trước lần đổi hình kế tiếp.
- **Không chuyển thẳng từ nền tối sang màu nhấn:** thay vào đó cho một phần tử mang màu nhấn đi từ trạng thái trước sang trạng thái sau.
- **Đổi đích nhiều lần thì cộng lò xo:** một giá trị đổi đích nhiều lần thì cộng một lò xo cho mỗi lần đổi, không đặt lại từ đầu (tránh giật). Thanh chỉ thẻ (tab) cho hai cạnh chạy hai lò xo khác nhau để nó giãn ra khi di chuyển.
- **Khung cuối bằng khung đầu** khi video cần phát lặp trên mạng xã hội; nếu có khung cuối đứng yên để đọc (ví dụ cách đăng ký) thì không áp dụng.

### Ba điểm bổ sung (PM duyệt 4/10/2026, nguồn: infographic @0xMovez về MOTION.md, brief.md, style_guide.md)

- **Tệp thông số chuyển động `motion.md` trong thư mục video.** Ghi một lần, mọi lần dựng lại và mọi video sau cùng nhãn hiệu đều đọc lại thay vì đoán: kích thước khung và số khung hình mỗi giây; bảng màu; mỗi loại lò xo một dòng (độ cứng, độ giảm chấn; ví dụ khối đổi hình, con trỏ, chữ); nhịp mỗi phút và các mốc nhịp; luật chung (trạng thái đổi rơi đúng nhịp, cấm nảy, cấm phát sáng). Phần chữ giải thích vì sao chọn các số đó viết ngay dưới bảng số. Bản chỉ đạo (Bước 1) trỏ tới tệp này. Sửa số ở đây rồi dựng lại, không sửa rải rác trong mã HTML. Chỉnh nhỏ về thời điểm hay chữ thì PM có thể tự làm trong Studio; Claude đọc lại tệp trước khi sửa tiếp để không ghi đè chỉnh sửa của PM.
- **Nhiễu cố định.** Mọi hạt nhiễu, hạt phim, vị trí ngẫu nhiên dùng bộ sinh số có hạt giống ghi trong `motion.md`, không dùng `Math.random`. Dựng lại bao nhiêu lần cũng ra đúng cùng một khung, nên so hai bản được và sửa lỗi không làm hình khác đi chỗ khác.
- **Nhật ký chấm điểm `review_log.md`.** Sau mỗi vòng chấm ở Bước 6 ghi 3 lỗi lớn nhất, việc đã sửa và điểm mới. Vòng sau đọc lại nhật ký để không lặp lỗi cũ; hết 3 vòng thì gửi nhật ký cho PM cùng danh sách lỗi còn lại.
- **Mức suy nghĩ theo việc (nguồn: khóa học 12 bước của Moves, 27/9/2026).** Video mới hoặc 3 giây đầu quyết định (giới thiệu sản phẩm) dùng mức high; sửa nhỏ và dựng lại dùng mức medium. Ghi một dòng `Gợi ý:` đầu việc theo quy tắc 7 của CLAUDE.md.
- **Một phiên cho một nhãn hiệu.** Làm video thứ hai cho cùng nhãn hiệu thì dùng lại phiên (hoặc đọc lại `motion.md` và thư mục video trước): bộ dựng hình, nhạc và xuất tệp đã có nên nhanh hơn nhiều.
- **Khóa API không dán vào câu lệnh hay bản chỉ đạo.** Để trong biến môi trường (PM tự lưu), bản chỉ đạo chỉ ghi tên biến.

### Bổ sung từ motion-graphics-skills (PM duyệt 10/10/2026)

Nguồn: `github.com/charlie947/motion-graphics-skills` (Charlie Hills, MIT, commit 4cd156a ngày 30/9/2026, 13 kỹ năng; đọc 10/10/2026, chỉ lấy ý, không cài gói, không chép mã). Không lấy: phong cách nhái giao diện Apple, 3D nặng, so sánh nhiều mô hình AI, giấy rách và hạt phim (lệch nhận diện Trường).

- **Thang 4 trạng thái trong bản chỉ đạo:** bắt đầu, đổi, giữ, quay về; khung cuối trùng khung đầu khi video phát lặp. Với đoạn lặp tham khảo tỷ lệ khoảng 2 giây đổi, 4 giây giữ, 1,5 giây quay về.
- **Phần giữ không đứng chết:** trong lúc giữ luôn có một chi tiết nhỏ còn sống (thanh tiến trình, con trỏ nhấp nháy); để lại một "bóng mờ" của trạng thái đầu cho mắt theo kịp; vào cảnh so le theo nhịp chứ không cùng lúc. Riêng khung cuối đăng ký đứng yên để đọc thì không áp dụng.
- **Dưới lời đọc:** đoạn chuyển động chủ động chỉ khoảng 1,4 giây rồi giữ; vòng chuyển động 8 giây là quá chậm cho một cảnh reel.
- **Số liệu thật ghi nguồn, số mẫu dán nhãn "Ví dụ" trên mọi khung** (số tuyển sinh, kết quả khóa, học phí). Không để số mẫu trông như số thật.
- **Mốc kiểm "giây 4":** người lạ xem đến giây 4 phải biết đây là khóa gì, cho ai. Cùng với mốc hiểu được khi tắt tiếng đã có.
- **Dựng thử 10 giây đầu** (2-3 kiểu) rồi mới dựng phần còn lại, nhất là video trên 20 giây, cho đỡ tốn token.
- **Nếu dùng canvas:** tạo context với `willReadFrequently: true` (Chrome đổi cách vẽ sau nhiều lần đọc điểm ảnh làm cùng một khung ra khác nhau); nạp phông tường minh trước khi vẽ khung 0 (khung 0 hay vẽ bằng phông dự phòng, nguy cơ với phông của Trường); kiểm khung 0 và khung cuối giống nhau từng điểm ảnh khi video lặp.
- **Sửa một lỗi mỗi lần:** câu mẫu khi chỉnh bản nháp là "chỉ sửa đúng một chỗ này, giữ nguyên chuyển động, thời gian và vòng lặp".

## Bước 5 - Nhạc và tiếng động khớp nhịp

1. Chọn nhịp theo tâm trạng (bảng trong `video-khoa-hoc/phong-cach.md`). Tổng hợp nhạc bằng mã, không dùng nhạc có bản quyền.
2. Đo bản nhạc và xuất `beats.json` gồm: nhịp/phút, thời điểm các nhịp, nhịp mạnh, các điểm nhấn.
3. **Chỉnh lại thời gian hoạt ảnh theo `beats.json`** (chữ hiện, chuyển cảnh, nhấn logo rơi đúng nhịp), không đặt thời gian tay rồi mới chọn nhạc. Gom các mốc nhịp vào một chỗ (một tệp `nhip.js` trong `assets/` đọc từ `beats.json`, ví dụ hàm `nhip(k)` trả về giây của nhịp thứ k); mọi cảnh đặt `data-start` và vị trí trên dòng thời gian GSAP qua các hàm này, không tự ghi số giây riêng. Lệnh `npx hyperframes beats` của HyperFrames cũng đo được nhịp (xem `hyperframes-cli`).
4. Tiếng động giao diện (bấm khi con trỏ nhấn, lướt khi khối đổi hình, thịch khi hiện logo) dùng bản ghi thật theo kỹ năng `sound-layer` (PM duyệt 11/10/2026), không tổng hợp bằng mã; nhạc nền vẫn tự tổng hợp như trên. Chỉ đặt tiếng ở nơi làm rõ hành động; nhỏ, không át nhạc. **Lấy thời điểm tiếng từ chính hình:** tệp HTML xuất danh sách sự kiện (`events.json`: giây, loại tiếng, độ mạnh), một đoạn mã đọc danh sách đó và sinh mỗi tiếng một thẻ `<audio>` đúng giây trong `index.html`. Sửa hình thì tiếng tự khớp theo, không phải canh lại tay. Dùng bộ sinh số ngẫu nhiên có hạt cố định để mỗi lần trộn ra cùng một kết quả.
5. **Giọng đọc mặc định không dùng.** PM muốn có lời thì hỏi PM trước. Dùng dịch vụ giọng AI có thể tốn phí và có điều khoản riêng. Nhân bản giọng một người thật (kể cả giọng PM) cần người đó đồng ý rõ ràng.

## Bước 6 - Chấm điểm nhiều vòng

Trước khi chấm: chạy kiểm tra tự động và xem ảnh ghép từng cảnh theo `video-khoa-hoc` (mục Cách dựng và mốc 4). Sau khi dựng bản đầy đủ, xem liền một mạch rồi tự chấm 6 tiêu chí, thang 10, mỗi điểm kèm một câu lý do:

1. Bố cục và điểm nhìn chính
2. Chữ (đọc được, đồng nhất, đúng nguyên văn)
3. Chuyển động (mềm, nối từ cảnh trước)
4. Nhịp (nhanh - giữ, khớp nhạc)
5. Màu và nhận diện ĐHTL
6. Âm thanh

- Sửa tiêu chí dưới 8, dựng lại, chấm lại. **Tối đa 3 vòng**; hết 3 vòng vẫn dưới 8 thì báo PM danh sách còn lại.
- Điểm này do Claude tự chấm nên có thể lạc quan. Sau vòng chấm vẫn phải chạy **rà từng giây P0-P2 bằng trợ lý con** theo `video-khoa-hoc` và để PM xem bản cuối. Lỗi P0 luôn sửa hết.
- Khi PM muốn dùng lại nhiều lần, đóng gói bản chỉ đạo thành kỹ năng riêng: tên gọi, các câu hỏi thông tin cần hỏi, luật cứng, và giữ tệp `phong-cach-<ten>.md` cùng bảng thành phần trong thư mục dự án để video sau đồng nhất.

## Bước 7 - Đo sau khi đăng

Sau khi PM đăng video, làm theo mục "Đo hiệu quả sau khi đăng" của `video-khoa-hoc`: ghi vào bảng chung, hẹn nhắc 7 và 30 ngày, nhờ PM dán số liệu, rút bài học khi có từ 3 video. Bài học đã rút thì đọc lại trước khi viết bản chỉ đạo video mới (Bước 1).

## Danh mục phong cách có sẵn (lemo-opuscar)

Nguồn: kho `github.com/lemomo-ai/lemo-opuscar` (giấy phép MIT, LemoLab 2026; phông, nhạc, giọng trong các bản demo có giấy phép riêng ghi ở `CREDITS`). 43 phong cách phim dựng bằng mã, mỗi phong cách có `STYLE.md` mô tả cách làm, đọc ngày 3/10/2026. Mỗi lần dựng video đều đưa các phong cách dưới đây làm lựa chọn ở Bước 1 (hộp thoại); PM chọn phong cách nào thì đọc `styles/<tên>/STYLE.md` thay cho Bước 3.

| Phong cách | Hợp với | Nhịp gốc |
|---|---|---|
| `swiss-motion` | Tiêu đề khóa học, hội thảo: chữ và lưới sạch, rất rõ chữ | 120 |
| `dark-keynote` | AI Lab, sản phẩm công nghệ: nền tối, giao diện | 120 |
| `dataviz` | Số liệu tuyển sinh, kết quả khóa học | 90 |
| `whiteboard` | Giảng giải một khái niệm, ra dáng bài giảng | 120 |
| `blueprint` | Sơ đồ quy trình, kỹ thuật | 108 |
| `iso-infographic` | Lộ trình học, quy trình nhiều bước | khoảng 100 |
| `hologram-hud` | AI, quét, thông số (mẫu gốc là phim ra mắt sản phẩm) | 120 |

- Chỉ học cách làm (bố cục, chuyển cảnh, nhịp). Màu và phông luôn đổi sang nhận diện ĐHTL (hoặc của sản phẩm, ví dụ SonicRec), phông có dấu tiếng Việt; phông trong kho đó chỉ có chữ Latin.
- Không chép nguyên mã hay bản demo của họ vào video của Trường khi chưa xem `CREDITS`.

## Video dài hơn 30 giây

Học từ 2 repo PDoomVideo (video ca nhạc 2,5 phút) và Battle-of-Austerlitz-Film (phim 5 phút), đọc 2/10/2026. Cả hai không có giấy phép nên chỉ học cách làm, không chép mã.

- **Bảng phân cảnh trước, mã sau.** Ngoài bảng nhịp, viết `bang-phan-canh.md`: mỗi cảnh ghi màu chủ đạo, kiểu chuyển cảnh, và việc gì xảy ra trên hình. Cảnh nào cũng phải có hành động, không để hình đứng không có lý do (trừ đoạn giữ yên để đọc chữ).
- **Chia việc cho trợ lý con** (tối đa 3 theo CLAUDE.md): phiên chính viết `huong-dan-canh.md` gồm bảng màu, các hàm nhịp, thành phần dùng lại, luật cứng và cách tự kiểm tra. Mỗi trợ lý con làm một nhóm cảnh trong tệp riêng; tệp dùng chung (hàm nhịp, màu, phông) chỉ được đọc, không được sửa. Mỗi trợ lý con tự xem ảnh ghép tại khung đầu, khung cuối và quanh các nhịp nhấn của cảnh mình trước khi nộp.
- **Mỗi trợ lý con một cảnh con.** Mỗi nhóm cảnh là một tệp trong `compositions/` của dự án HyperFrames; trợ lý con chạy `snapshot` cho cảnh của mình trước khi nộp. Phiên chính gắn các cảnh vào `index.html`, chạy `check` rồi dựng một lần (HyperFrames tự chia nhiều tiến trình).
- Khung hình vẫn là hàm của thời gian, không giữ trạng thái giữa các khung, nên cảnh nào cũng xem lại được ở bất kỳ giây nào.

## Thư mục và tên tệp

`videos/<YYMMDD>_<DuAn>_<TenVideo>/`, tệp đặt tên `YYMMDD_<DuAn>_<NoiDung>.ext`. Video trên 20MB không đưa lên kho, chỉ giữ mã nguồn, bảng nhịp, `beats.json`, ảnh xem trước.

## Lỗi hay gặp

Phần dựng bằng mã dùng chung danh sách "Lỗi hay gặp" trong `video-khoa-hoc/SKILL.md` và mục "Lỗi hay gặp" trong `video-khoa-hoc/dung-hyperframes.md`. Gặp lỗi riêng của kỹ năng này thì ghi thêm ở đây.

## Gợi ý model

Opus 5.5 - mức high (nhiều bước, cần tự soát). Bản chỉ đạo và bảng nhịp riêng thì Sonnet 5.5 - high là đủ. Trợ lý con rà từng giây dùng `sonnet`.
