# Luật kỹ thuật (bản 4.0.x)

Nguồn: remotion.dev/docs (the-fundamentals, composition, sequence, interpolate, spring, transitions, media, fonts, captions, cli/render), kiểm 5/10/2026. Chỗ nào ghi "chưa kiểm" là suy luận.

## Mô hình
- Video là hàm của số khung hình: `useCurrentFrame()`, `useVideoConfig()`.
- `Composition`: `id` chỉ chữ không dấu, số, gạch ngang; `defaultProps` phải chuyển được sang JSON; `schema` là `z.object()`; chiều rộng, cao là số nguyên chẵn (chưa kiểm cho h264).
- `calculateMetadata` chạy một lần trước khi dựng, trả `durationInFrames`, `fps`, `width`, `height`, `props`. Dùng nó để nạp JSON hoặc CSV và đặt thời lượng. Truyền `abortSignal` vào `fetch`.
- `Sequence` dịch khung của con theo `from`; `premountFor` nạp trước để khỏi nháy.

## Chuyển động
- `interpolate`: luôn `extrapolateLeft` và `extrapolateRight` là `'clamp'`.
- `spring`: `damping` cao bớt nảy, `overshootClamping: true` chặn vọt, `durationInFrames` kéo đường cong đúng độ dài.
- Cấm CSS transition, CSS animation, `Math.random`, `Date.now`. Ngẫu nhiên chỉ `random('hạt-giống')`. Khung hình dựng song song, không thứ tự.
- `TransitionSeries`: tổng thời lượng bằng tổng cảnh trừ tổng chuyển cảnh. Chuyển cảnh không dài hơn cảnh kề, hai chuyển cảnh không đứng sát nhau.

## Phông và tiếng Việt
- `@remotion/google-fonts/BeVietnamPro` và `NotoSerif` đều có tập con `vietnamese` (đọc từ mã nguồn gói). Gọi `loadFont('normal', {weights: [...], subsets: ['vietnamese','latin']})`, đừng gọi không đối số (nạp mọi thứ, dễ quá hạn).
- Phải `await waitUntilDone()` trước khi đo chữ bằng `fitText` hay `measureText`.
- Phông riêng: `@remotion/fonts` `loadFont` với `staticFile()`.
- Chữ nhiều dấu cao hơn chữ Latin cùng cỡ: đặt `lineHeight` dư và giới hạn cỡ tối đa (chưa kiểm bằng thử).

## Phương tiện
- Video và âm thanh mới dùng `@remotion/media`; `OffthreadVideo` còn dùng cho codec không hỗ trợ. Ảnh dùng `<Img>`. Tệp trong `public/` qua `staticFile()`, đặt tên không dấu.
- Tải bất đồng bộ: `delayRender` rồi `continueRender`.

## Phụ đề
- `@remotion/captions`, `createTikTokStyleCaptions` cho kiểu từng từ; mỗi trang một `Sequence`, `white-space: pre`.
- Whisper: `language: 'vi'`, bắt buộc mô hình đa ngôn ngữ (tên không có `.en`; mặc định `base.en` sai cho tiếng Việt). Đầu vào WAV 16 kHz 16 bit. Độ chính xác từng cỡ mô hình chưa thử.
- Giọng đọc tiếng Việt: Remotion không kèm; chưa kiểm dịch vụ nào.

## Biểu đồ và số liệu
- Cột, số đếm: `interpolate` và `spring`. Đường: `@remotion/paths` (`evolvePath`, `getLength`). Hình: `@remotion/shapes`. Âm thanh: `visualizeAudio`. D3 không chính thức; chỉ dùng để tính, tự vẽ bằng SVG.

## Dựng
- `npx remotion render <entry> <id> out.mp4 --codec h264 --crf 18 --props data.json`; ảnh: `npx remotion still`. `npx remotion benchmark` chọn số luồng.
- Hàng loạt: `bundle()` một lần (đừng gói lại mỗi video), mỗi dòng `selectComposition({serveUrl, id, inputProps})` rồi `renderMedia` hoặc `renderStill` với cùng `inputProps`. Nhiều ảnh: dùng chung `puppeteerInstance` từ `openBrowser()`.
- Lambda: ví dụ trong tài liệu, video 1 phút khoảng 0,02 USD, chưa tính S3; Cloud Run đang ở mức Alpha, tránh dùng.

## Bẫy
Không kẹp `interpolate`; dùng CSS animation; quên `delayRender`; quên trừ chuyển cảnh khi đặt thời lượng; id có dấu hay khoảng trắng; nạp mọi tập con phông; thẻ `<img>` hay `<video>` thô; props không chuyển được JSON; v4.0.530 đổi cách tính `durationInFrames` với `playbackRate` nên ghim đúng số phiên bản trong `package.json`.
