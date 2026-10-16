# Dựng video bằng HyperFrames

Cách dựng chung cho 5 kỹ năng video của kho (`video-khoa-hoc`, `video-chuyen-dong`, `video-quang-cao-san-pham`, `video-ui-bien-hinh`, `video-3d-theo-mau`). PM chốt ngày 8/10/2026: thay hẳn cách cũ (tự viết `seek(t)`, Playwright chụp, ffmpeg ghép) bằng HyperFrames của HeyGen (Apache 2.0) để PM mở Studio kéo chỉnh dòng thời gian, sửa chữ mà không cần nhờ Claude. Bản cũ của các kỹ năng lưu ở `04_Archives/Projects/KhoTaiLieu/261008_*`. Cùng ngày một phiên khác viết `dung-bang-hyperframes.md` (HyperFrames mặc định, cách cũ dự phòng, PR #535); PM chọn gộp vào tệp này và thay hẳn, bản đó lưu ở `04_Archives/Projects/KhoTaiLieu/261008_KhoTaiLieu_video-khoa-hoc_dung-bang-hyperframes_v1.md`.

Hợp đồng đầy đủ nằm ở các kỹ năng gốc đã chép vào kho; tệp này chỉ ghi phần kho dùng và các điểm đã chạy thử trong phiên web ngày 8/10/2026:

| Cần gì | Đọc kỹ năng gốc |
|---|---|
| Cấu trúc tệp, `data-*`, cảnh con, biến | `hyperframes-core` (SKILL.md và `references/`) |
| Lệnh `init`, `lint`, `check`, `snapshot`, `preview`, `render` | `hyperframes-cli` |
| Chuyển động, lò xo, chuyển cảnh, hiệu ứng chữ | `hyperframes-animation` |
| Bố cục dòng thời gian để PM chỉnh trong Studio | `hyperframes-studio` |
| Âm lượng, nhỏ dần, trộn tiếng | `hyperframes-audio` |
| Phóng to, máy quay, keyframe | `hyperframes-keyframes` |

Kỹ năng gốc `hyperframes` tự nhận là "cửa vào bắt buộc" cho mọi video. Trong kho này, việc của TTC và ĐHTL vẫn đi qua kỹ năng video của kho trước (bản hướng dẫn, duyệt từng mốc, bộ màu ĐHTL, rà từng giây); kỹ năng gốc chỉ dùng làm tài liệu tra cứu cho phần dựng.

## Chuẩn bị

- Cần Node.js 22 trở lên và ffmpeg (máy phiên web có sẵn). Ghim phiên bản: `npx -y hyperframes@0.8.134 <lệnh>` (ra 5/10/2026; theo bài học PM duyệt 8/10/2026 chỉ dùng bản đã ra ít nhất 3 ngày, không dùng `latest`). Đã thử trên bản này 8/10/2026: `init`, `lint`, `check`, `snapshot`, `render`, nhạc, khung `video-ui-bien-hinh`. Bộ kỹ năng gốc chép từ bản mới hơn (khoảng 0.8.141) nên vài lệnh, hàm trong đó có thể chưa có ở 0.8.134 (đã gặp: `registerFrameSource`); gặp lệnh báo không tồn tại thì làm theo cách của bản đang ghim. Nâng bản khi cần sửa lỗi hoặc cần tính năng mới: chọn bản đã ra ít nhất 3 ngày, thử dựng một video mẫu, sửa số ở đây, trong `video-ui-bien-hinh/render.py`, rồi chép lại bộ kỹ năng gốc cùng bản.
- Tắt gửi số liệu (mặc định công cụ gửi tên lệnh, thông tin máy về HeyGen, theo tài liệu không gửi nội dung video): đầu phiên chạy `export HYPERFRAMES_NO_TELEMETRY=1 DO_NOT_TRACK=1` và `npx -y hyperframes@0.8.134 telemetry disable`.
- Tạo dự án: `HYPERFRAMES_SKIP_SKILLS=1 npx -y hyperframes@0.8.134 init <ten> --non-interactive --resolution portrait` (`landscape` cho 16:9, `square` cho 1:1). Biến `HYPERFRAMES_SKIP_SKILLS=1` để lệnh không tải lại kỹ năng vào thư mục dự án, vì kho đã có. Chạy `init` trong thư mục scratchpad rồi chỉ chép `index.html`, `hyperframes.json`, `package.json`, `meta.json` sang thư mục video của dự án; bỏ hai tệp `AGENTS.md`, `CLAUDE.md` mà `init` sinh ra (lời dặn tiếng Anh của HeyGen, trùng với kỹ năng).
- Thư viện và phông chép vào `assets/` của dự án, không tải từ mạng lúc dựng: `curl -sL -o assets/gsap.min.js https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js`, rồi đổi đường dẫn trong `index.html`. Phông Google khai bằng thẻ `<link>` thì HyperFrames tự tải và nhúng lúc dựng (khi thử hiện dòng "Injected deterministic @font-face"), chữ có dấu hiện đúng; phông khác khai báo `@font-face` từ tệp trong `assets/` (xem mục Lỗi hay gặp của `video-khoa-hoc`).

## Viết video

Một video là một thư mục dự án, tệp chính `index.html`:

- Phần tử gốc có `data-composition-id="main"`, `data-width`, `data-height`, `data-duration` (giây), `data-fps` nếu cần 60.
- **Mỗi cảnh là một cảnh con** (`compositions/canh-01.html`... gắn vào gốc bằng `data-composition-src`), mỗi cảnh có `class="clip"`, `data-start`, `data-duration`, `data-track-index`. Studio hiện mỗi cảnh thành một dòng trên dòng thời gian, PM kéo dời, cắt ngắn được. Cách viết cảnh con: `hyperframes-core/references/sub-compositions.md`.
- **Chuyển động viết bằng GSAP** (mặc định): mỗi tệp đăng ký đúng một `gsap.timeline({ paused: true })` vào `window.__timelines["<id>"]`, id trùng `data-composition-id`. Chữ là phần tử HTML thật để PM sửa trong bảng thuộc tính của Studio.
- **Mã có sẵn dạng `seek(t)`** (lò xo tự viết, canvas, như `video-ui-bien-hinh`): không phải viết lại bằng GSAP. Bọc phần vẽ trong một phần tử `class="clip"` có `data-no-timeline`, thêm `data-no-timeline` cho phần tử gốc, rồi đăng ký:

  ```js
  if (window.__hyperframes && window.__hyperframes.registerFrameSource) {
    window.__hyperframes.registerFrameSource({
      element: document.getElementById("stage"),
      ready: document.fonts.ready,
      render: (t) => window.seek(t),
    });
  } else {
    window.addEventListener("hf-seek", (e) => window.seek(e.detail.time));
  }
  ```

  Bản đang ghim (0.8.134) chưa có `registerFrameSource` nên chạy nhánh `hf-seek`; nâng lên bản có hàm này thì tự chuyển, không phải sửa mã. Thiếu `data-no-timeline` thì mỗi lần dựng phải chờ 45 giây. Với khối `seek(t)`, PM chỉ dời, cắt được cả khối trong Studio, không sửa chữ bên trong được.
- Luật cố định giữ nguyên như cũ: cấm `Math.random()` không hạt giống, cấm `Date.now()`, `requestAnimationFrame`, hẹn giờ, chuyển tiếp CSS tự chạy, tải tệp từ mạng giữa chừng. Chi tiết: `hyperframes-core/references/determinism-rules.md`.
- Nhạc và tiếng động: nhạc vẫn tự tổng hợp bằng mã, xuất WAV vào `assets/`, đặt bằng `<audio class="clip" src="assets/nhac.wav" data-start="0" data-duration="20" data-track-index="9" data-volume="0.8">`. HyperFrames tự trộn vào MP4. Thẻ `<audio>` phải có `id` (thiếu thì video ra không có tiếng) và không thêm `crossorigin`. Thẻ `<video>` (clip quay, clip AI) cũng dùng được, HyperFrames tự tua theo khung. Tiếng động theo `events.json` thì mỗi tiếng một thẻ `<audio>` riêng ở đúng giây. Lời đọc VieNeu cũng vậy: mỗi câu một thẻ `<audio>` trên dòng riêng, đặt đúng chỗ trong lưới nhịp; hạ nhạc khi có giọng bằng tự động hóa âm lượng (`hyperframes-audio`) thay cho lọc ffmpeg.
- Thông tin hay đổi (ngày khai giảng, học phí, đường dẫn đăng ký) khai báo thành biến của video (`hyperframes-core/references/variables-and-media.md`); đổi khóa khác chỉ sửa biến rồi dựng lại, nhiều khóa một lúc thì dùng `render --batch`.

## Kiểm và dựng

| Việc | Lệnh |
|---|---|
| Kiểm nhanh khi đang viết | `npx -y hyperframes@0.8.134 lint` |
| Kiểm đầy đủ trước khi dựng (lỗi chạy, chữ tràn, độ tương phản WCAG) | `npx -y hyperframes@0.8.134 check` |
| Ảnh ở các mốc giây (thay cho kiểm tra tự động cũ) | `npx -y hyperframes@0.8.134 snapshot --at 0,2,6,11,15,19.5` |
| Bản nháp xem nhanh | `npx -y hyperframes@0.8.134 render --quality draft --output nhap.mp4` |
| Bản giao | `npx -y hyperframes@0.8.134 render --quality delivery --fps 60 --output <Ten>_9x16.mp4` |

- `check` phải qua (0 lỗi) mới dựng. Cảnh báo `nested_structure_needs_subcomposition` nghĩa là còn khối lồng chưa tách thành cảnh con; với khối dạng `seek(t)` thì chấp nhận được.
- **Mờ chuyển động** (thay cho cách gọi `seek` nhiều lần của bản cũ): dựng ở `--fps 240`, rồi trộn 4 khung thành 1:
  `ffmpeg -i raw240.mp4 -vf "tmix=frames=4:weights=1 1 1 1,select='eq(mod(n\,4)\,3)',setpts=N/(60*TB)" -r 60 -c:v libx264 -crf 18 -pix_fmt yuv420p -c:a copy ra60.mp4`. Đã thử 8/10/2026: 4 giây khổ 1440 mất khoảng 80 giây trên máy phiên. Bản nháp bỏ qua bước này.
- Chuẩn hóa âm lượng -14 LUFS sau khi dựng: `ffmpeg -i in.mp4 -c:v copy -af loudnorm=I=-14:TP=-1.5:LRA=11 out.mp4`.
- Kiểm tệp ra: `ffprobe -v error -show_entries format=duration:stream=width,height,r_frame_rate -of compact <tệp>`; thời lượng phải bằng `data-duration`.
- Bản 16:9 hay 1:1: tạo dự án thứ hai cạnh dự án 9:16 (`<ten>_16x9/`), chép `assets/` cần dùng, sắp lại bố cục từng cảnh. Không ép khổ bằng `--resolution` của lệnh `render`: bố cục viết theo khổ gốc nên chữ dễ tràn hoặc bị cắt.

## PM chỉnh trong Studio

- Trên Mac của PM: `cd <thư mục dự án> && npx -y hyperframes@0.8.134 preview`. Studio mở ở `http://localhost:3002`; PM kéo cảnh trên dòng thời gian, sửa chữ, màu trong bảng thuộc tính; Studio ghi thẳng vào tệp HTML. PM chỉnh xong thì báo Claude, Claude chạy `check` rồi dựng lại.
- Trong phiên web, Studio chạy trong máy phiên nên PM không mở được; Claude chỉ dùng `preview --background` để tự xem khi cần.
- Gói `@hyperframes/studio` (trang PM gửi) là bộ khối React để tự viết trình chỉnh video, kho không cài.

## Không dùng

- Dựng trên mây của HeyGen, AWS Lambda, Google Cloud Run (`cloud`, `lambda`, `cloudrun`): gửi dữ liệu ra ngoài, có thể tốn phí. Chỉ dựng trên máy.
- `snapshot --describe` (gửi ảnh cho Gemini), giọng đọc `tts` của HyperFrames, nhạc và tiếng động tải qua `media-use resolve` (cần tài khoản HeyGen). Lời đọc dùng VieNeu-TTS chạy trên máy (`video-khoa-hoc`, mục Âm thanh), nhạc tự tổng hợp.
- `npx hyperframes open` (ứng dụng máy tính của HeyGen) khi PM chưa yêu cầu.

## Lỗi hay gặp

- `missing_timeline_registry`, mỗi lần dựng chờ 45 giây: mã `seek(t)` thiếu `data-no-timeline` ở phần tử gốc hoặc phần tử bọc.
- `lint` đọc cả thẻ `<audio>` nằm trong chú thích HTML và báo thiếu tệp: không để thẻ mẫu trong chú thích.
- Chép bộ kỹ năng gốc vào kho: `.gitignore` chặn `lib/`, `*.mp3`, `*.txt`, phải `git add -f`.
