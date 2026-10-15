---
name: video-ui-bien-hinh
description: Dùng khi PM muốn video chuyển động giao diện kiểu Dribbble, trong đó một khối hình biến liên tục qua nhiều trạng thái UI (nút, vòng tải, trình phát, thanh trượt, công tắc, tab, biểu đồ, bảng lệnh, thông báo), có con trỏ bấm kéo, khớp nhạc theo nhịp và lặp liền mạch; hoặc khi PM gõ /video-ui-bien-hinh, "UI morphing", "shape morph", "một khối biến hình".
---

# Video UI biến hình theo nhịp

Nội dung: Bước 1 Hỏi đầu vào; Bước 2 Bảng trạng thái; Bước 3 Hướng hình ảnh; Bước 4 Quy tắc dựng; Bước 5 Âm thanh; Bước 6 Xuất và kiểm tra; Bẫy đã gặp; Cách làm sai thường gặp.

Một khối hình duy nhất, không cắt cảnh: mọi trạng thái là cùng một phần tử đổi kích thước, bo góc, màu, còn nội dung bên trong đổi chỗ với một nhịp mờ ngắn. Con trỏ gây ra mọi thay đổi bằng cú bấm và cú kéo thật. Nhạc khoảng 120 BPM, 7 ô nhịp, nhịp nào cũng có việc xảy ra. Khung cuối là khung đầu.

Mã mẫu đi kèm, đã chạy thử, nằm ở `.claude/skills/video-ui-bien-hinh/`. Lệnh bên dưới viết tắt thư mục này là `$K` (chạy `K=.claude/skills/video-ui-bien-hinh` từ gốc kho trước):

- `spring.js`: lò xo dạng đóng.
- `beat.py`: đo nhịp, trộn tiếng động, chỉ cần numpy và ffmpeg.
- `render.py`: gọi HyperFrames dựng ở 240 khung/giây, ffmpeg tmix trộn 4 khung con thành 1 (mờ chuyển động); chế độ `--beats` chụp một ảnh mỗi phách bằng `snapshot`.
- `khung.html`: khung 2 ô nhịp (nút, vòng tải, dấu tích, nút) dạng dự án HyperFrames, đã chép sẵn `spring.js` vào trong; `seek(t)` được HyperFrames gọi qua `registerFrameSource`, bản cũ chưa có hàm này thì qua sự kiện `hf-seek` (cách làm chung ở `video-khoa-hoc/dung-hyperframes.md`). PM mở Studio thì dời, cắt được cả khối trên dòng thời gian; sửa chữ, trạng thái thì vẫn sửa bảng `KEY` trong mã.

Bắt đầu bằng cách tạo thư mục video trong dự án PM chỉ định, ví dụ `261005_DuAn_UIBienHinh/`, chạy `init` của HyperFrames theo `video-khoa-hoc/dung-hyperframes.md` (mục Chuẩn bị) rồi chép `$K/khung.html` thành `index.html` của thư mục đó. Video ra cạnh thư mục, tên `261005_DuAn_UIBienHinh.mp4`. Giữ một tệp HTML: không tách `spring.js` ra tệp riêng. Đổi độ dài vòng thì sửa `data-duration` của `#root` và `#stage` cho bằng `T`.

## Bước 1 - Hỏi đầu vào (bằng AskUserQuestion, trước mọi việc khác)

1. **8 đến 12 trạng thái** khối hình sẽ đi qua. Đưa sẵn chuỗi mặc định ở Bước 2 làm lựa chọn khuyến nghị.
2. **Màu**: đen trắng thuần, hay đen trắng cộng **một** màu nhấn (hỏi mã màu).
3. **Bài nhạc** khoảng 120 BPM, có bản quyền tự do cho mục đích thương mại (ví dụ Mixkit). PM gửi tệp hoặc đường dẫn. Không tự tổng hợp nhạc thay bài thật, trừ khi PM chọn vậy.
4. **Tiếng động UI** (bấm, bật công tắc, gõ phím, thông báo): PM gửi tệp, hay lấy từ kho hiệu ứng âm thanh miễn phí như Mixkit SFX. Ghi giấy phép của từng tệp.

## Bước 2 - Bảng trạng thái trên lưới nhịp (đưa PM duyệt TRƯỚC khi viết mã)

7 ô nhịp = 28 phách = 14 giây ở 120 BPM. Bảng gửi PM có 28 dòng, mỗi dòng một phách: phách số mấy, giây thứ mấy, con trỏ làm gì, khối thành gì, tiếng động nào. Không có phách nào trống; trạng thái dài thì chia thành nhiều việc nhỏ (bấm, kéo, rê chuột). Chuỗi mặc định, gọn theo ô nhịp:

| Ô | Phách 1 | Phách 2 | Phách 3 | Phách 4 |
|---|---|---|---|---|
| 1 | Nút, con trỏ tới | Bấm, thành vòng tải | Vòng tải quay | Dấu tích |
| 2 | Thành dynamic island | Mở thành trình phát | Bấm play, biến thành pause | Nắm thanh tiến trình |
| 3 | Tua (kéo) | Nhả, lò xo về | Trình phát thu thành thanh âm lượng | Kéo âm lượng lên |
| 4 | Kéo quá mức tối đa, thanh giãn | Nhả, co về | Thành công tắc | Công tắc bật đúng phách |
| 5 | Núm thành chỉ báo tab | Bấm tab 2 (chỉ báo chảy) | Bấm tab 3 | Tab mở thành biểu đồ |
| 6 | Biểu đồ tự vẽ | Rê chuột, hiện chú thích | Chú thích chạy sang điểm kế | Thu lại thành ⌘K |
| 7 | Gõ chữ để lọc | Danh sách lọc lại | Enter, thành thông báo | Thông báo thành nút (= khung đầu) |

Sau khi PM duyệt bảng, chạy `beat.py` để có lưới phách thật của bài nhạc rồi mới gán giây.

## Bước 3 - Hướng hình ảnh

- Nền xám ấm nhạt (khoảng `#ECEAE6`), khối đen `#0A0A0A` và trắng, một phông giao diện là Geist (dự phòng Helvetica Neue).
- Lò xo ở mọi chuyển động, vọt tối đa khoảng 2% (`SPRING.base`). Camera phóng sao cho mỗi trạng thái lấp đầy khung, nhỏ thì phóng to, lớn thì lùi ra.
- Icon cùng một độ dày nét, khớp nét con trỏ.
- **Cấm**: easing nảy, hạt bung, phát sáng, gradient trên khung giao diện, icon lệch nét, khoảng chết, mọi thứ trông như template.

## Bước 4 - Quy tắc dựng

1. **Một tệp `index.html` vuông 1440x1440.** `window.seek(t)` tính mọi kiểu dáng từ `t`; HyperFrames gọi nó mỗi khung, không tự chạy. Không CSS transition, không animation, không timer, không `requestAnimationFrame`, không biến nhớ giữa các khung. Gọi seek theo thứ tự bất kỳ phải ra cùng một hình.
2. **Lò xo dạng đóng.** Một giá trị đổi đích nhiều lần = tổng các lò xo, mỗi lần đổi một lò xo: `track(keys, t, p, T)`.
3. **Vòng lặp không cần chờ lò xo đứng yên.** Truyền `loop = T` cho `track`: hàm cộng thêm đuôi lò xo của vòng trước, nên khung T khớp khung 0 cả vị trí lẫn vận tốc. Key cuối phải bằng key đầu, kể cả vị trí con trỏ. Key về đầu đặt được ngay ở phách cuối (13,5 giây), không lùi sớm hơn để chờ; phách cuối là một việc thật (thông báo thành nút). Cú kéo (giữ chuột) thì phải nhả trước phách cuối, vì `dragged` không nối qua mép vòng.
4. **Hai cạnh, hai lò xo.** Chỉ báo tab và núm công tắc dùng `liquidEdges`: cạnh dẫn đi lò xo nhanh, cạnh đuôi đi lò xo chậm, nên chỉ báo dài ra khi chạy rồi co lại khi tới.
5. **Kéo trực tiếp.** Trong lúc giữ chuột, giá trị tính từ vị trí con trỏ (`dragged`). Nhả ra thì lò xo về đích từ đúng chỗ đang đứng, mang theo vận tốc lúc nhả. Kéo quá giới hạn thì dùng `rubber`.
6. **Nội dung đổi chỗ có giờ vào và giờ ra riêng** (`swap`): lớp cũ mờ ra, lớp mới vào sau đó tối đa vài chục mili giây, mờ 6px, không bao giờ hai dòng chữ cùng đọc được một lúc.
7. **Con trỏ** nằm ở không gian màn hình (không bị camera phóng), toạ độ = tâm + toạ độ cảnh x camera; cỡ khoảng 56px trên khung 1440. Con trỏ tới nơi trước phách, cú bấm rơi đúng phách.

## Bước 5 - Âm thanh

```bash
python3 $K/beat.py nhac.mp3 --bpm 120 --bars 7 -o beats.json
python3 $K/beat.py nhac.mp3 --mix su_kien.json --beats-json beats.json -o nhac_cat.wav
```

- `beat.py` cho BPM đo được, điểm cắt rơi đúng phách mạnh, và 28 mốc phách tính từ điểm cắt. Nếu BPM đo lệch quá 1 so với BPM đoán thì nghe lại; bài có intro thì dùng `--start-bar`.
- `su_kien.json` lấy từ bảng phách: mỗi cú bấm, cú bật, phím gõ là một dòng `{"t": giây, "file": tệp, "gain": 0.7}`.
- `--mix` cắt nhạc đúng điểm phách mạnh, fade 10 ms hai đầu, đặt từng tiếng động sao cho **đỉnh** của nó rơi đúng `t`, đuôi tràn qua cuối vòng thì cuộn về đầu. Xem độ lệch đỉnh của một tệp: `beat.py --peak tep.wav`.

## Bước 6 - Xuất và kiểm tra

Chép `nhac_cat.wav` vào thư mục dự án và đặt thẻ nhạc vào chỗ chú thích "Nhạc" trong `index.html`: `<audio id="nhac" class="clip" src="nhac_cat.wav" data-start="0" data-duration="14" data-track-index="1"></audio>` (`data-duration` bằng `T`). Không để thẻ `<audio>` trong chú thích HTML: `lint` vẫn đọc và báo lỗi thiếu tệp.

```bash
python3 $K/render.py <thư mục dự án> --duration 14 --beats beats.json --out kiem/   # một ảnh mỗi phách
python3 $K/render.py <thư mục dự án> --duration 14 --out video.mp4
```


1. **Chụp một ảnh mỗi phách trước** (`--beats`), xem `kiem/bang_phach.png`. Sửa mọi chỗ lệch lưới, chật, khó đọc, lớp lệch tâm, khối trống chữ. Lặp lại tới khi sạch rồi mới xuất cả video.
2. Xuất cả video: `render.py` chạy `check` (phải qua), HyperFrames dựng 240 khung/giây, ffmpeg `tmix` trộn mỗi nhóm 4 khung rồi giữ đúng khung thứ 4, ra 60 fps; nhạc chép nguyên từ bản HyperFrames. Thử 8/10/2026 với bản 0.8.134 và 0.8.140: vòng 4 giây mất khoảng 80-90 giây trên máy phiên web, ảnh hai bản giống hệt nhau.
3. Kiểm vòng lặp: `--beats` cũng chụp `dau.png` (t = 0) và `cuoi.png` (t ngay trước T). So hai ảnh bằng `ffmpeg -i kiem/cuoi.png -i kiem/dau.png -lavfi ssim -f null -`, phải từ 0,999 trở lên. Video chỉ chứa khung 0 đến 839 (t < 14), khung 840 chính là khung 0 của vòng sau nên không xuất. Đếm khung: đúng 840.
4. Gửi PM video, kèm bảng phách đã duyệt.

## Bẫy đã gặp

| Bẫy | Cách tránh |
|---|---|
| `will-change` trên thứ camera phóng làm chữ mờ | Không dùng `will-change` ở đâu cả |
| Xếp các lớp nội dung chồng nhau bằng grid: lớp rộng nhất (chữ của nút) kéo lệch tâm vòng tải, dấu tích | Mỗi lớp `position:absolute; left:50%; top:50%; translate:-50% -50%`, để `transform` trống cho hoạt ảnh |
| Chữ mới vào trễ sau phách, ảnh chụp ở phách ra khối trống | Lớp mới vào ngay trước phách khoảng 40 ms |
| Khung cuối khác khung đầu (con trỏ lệch, vận tốc khác) làm vòng lặp giật | `track(..., T)` và key cuối bằng key đầu cho mọi thuộc tính, kể cả con trỏ |
| `import` module từ `file://` bị Chromium chặn | `spring.js` là script thường, chép vào `<script>` |
| Thiếu `data-no-timeline` ở `#root` hoặc `#stage`: mỗi lần dựng chờ 45 giây tìm dòng thời gian GSAP | Giữ nguyên hai thuộc tính này như trong `khung.html` |
| `lint` cảnh báo `nested_structure_needs_subcomposition` cho `#stage` | Chấp nhận được với khung `seek(t)`; không phải lỗi |
| `tmix` + `framestep` lấy lệch: mỗi khung mờ trễ 3/4 khung, khung 0 không mờ nên chỗ nối vòng giật | `render.py` dùng `select` giữ khung có `n mod 4 = 3`. Kiểm: tự trộn 4 khung con của một khung đang chạy nhanh, so SSIM với khung video, phải từ 0,999 trở lên |
| Chromium không chạy trong hộp cát macOS ("trust settings"), gặp với bản Playwright cũ | Chạy `render.py` ngoài hộp cát |
| Đỉnh onset trễ nửa cửa sổ FFT | `beat.py` đã bù `(hop + n/2)/SR`; tự viết lại thì nhớ bù |

## Những cách làm sai thường gặp khi không có kỹ năng này

- Tự tổng hợp nhạc thay vì hỏi bài thật, nên không có bước đo nhịp.
- Chia đều 4 phách cho mỗi trạng thái, ra 24 giây, phần lớn các phách không có gì xảy ra.
- Viết mã ngay, không có bảng phách cho PM duyệt.
- Không làm mờ chuyển động: mỗi khung chỉ chụp một lần.
- Để lò xo đứng yên hơn 1 giây trước khi hết vòng để lặp cho khớp, tức cố ý tạo khoảng chết.
- Dùng CSS transition hay GSAP tự chạy theo đồng hồ: tua thời gian thì không ra cùng một hình. (GSAP dừng sẵn trên dòng thời gian của HyperFrames thì tua được, nhưng lò xo dạng đóng ở đây cho vòng lặp liền nên giữ `seek(t)`.)
