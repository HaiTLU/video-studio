# Nguồn các kỹ năng trong kho

Chép từ kho `thanglong_kb` ngày 15/10/2026. Nguồn chi tiết ở `NGUON.md` hoặc `LICENSE` trong từng thư mục kỹ năng.

| Kỹ năng | Nguồn | Giấy phép |
|---|---|---|
| `video-khoa-hoc`, `video-chuyen-dong`, `video-3d-theo-mau`, `video-quang-cao-san-pham`, `video-sang-tao`, `video-ui-bien-hinh`, `remotion` | Viết trong kho `thanglong_kb` (học ý từ nhiều kho mở, ghi trong từng tệp) | của PM |
| `hyperframes`, `hyperframes-*` (8), `general-video`, `faceless-explainer`, `product-launch-video`, `pr-to-video`, `motion-graphics`, `music-to-video`, `slideshow`, `talking-head-recut`, `embedded-captions`, `media-use`, `remotion-to-hyperframes` | github.com/heygen-com/hyperframes | Apache 2.0 |
| `gsap-*` (8) | github.com/greensock/gsap-skills | MIT |
| `motion-design` | github.com/LottieFiles/motion-design-skill | MIT |
| `sound-layer` | github.com/Bodila51/opus-sound-layer | MIT |
| `watch` | github.com/bradautomates/claude-video | MIT |
| `motion` | github.com/motiondivision/ai-kit | MIT |
| `humanizer` | github.com/blader/humanizer (thêm `tieng-viet.md`) | MIT |
| `object-separation` | github.com/Barty-Bart/motion-graphics | MIT |

## Đối chiếu 15 repo trong bài "15 repo GitHub cho Claude Motion Studio" (Cesglobal AI, 15/10/2026)

Tên trong ảnh không có chủ sở hữu, nên kho dưới đây là kho khớp nhất tìm được; số sao đọc từ trang GitHub ngày 15/10/2026.

| Tên trong ảnh | Kho tìm được | Kết luận |
|---|---|---|
| product-launch-motion | AbubakrChan/product-launch-motion (MIT) | Không thêm: trùng `product-launch-video`, `video-chuyen-dong` |
| motion-graphics-skills | charlie947/motion-graphics-skills (MIT) | Không thêm: đã lấy ý ngày 10/10/2026 |
| claude-motion-design | howseen-ai/claude-motion-design (MIT) | Không thêm: cùng cách với `video-chuyen-dong` |
| hyperframes-student-kit | nateherkai/hyperframes-student-kit | Không thêm: phần lõi là HyperFrames, giấy phép chưa rõ |
| motion-graphics | heygen-com/hyperframes `skills/motion-graphics`; Barty-Bart/motion-graphics (MIT) | Bản HeyGen đã có; lấy thêm `object-separation` của Barty-Bart; `sound-effects` trùng `sound-layer` |
| animate | chưa xác định (impeccable hoặc delphi-ai/animate-skill) | Không thêm |
| claude-motion | whaleyxbt/claude-motion (MIT) | Không thêm: dựa trên Remotion, cần khóa ElevenLabs |
| claude-remotion-skill | haidrrrry/claude-remotion-skill (MIT) | Không thêm: trùng `remotion` |
| motion | motiondivision/motion (MIT) | Thư viện npm, cài trong từng dự án khi cần |
| motion-dev-animations-skill | 199-biotechnologies/motion-dev-animations-skill (MIT) | Không thêm: trùng `gsap-*`, PM đã bỏ 12/10/2026 |
| hyperframes | heygen-com/hyperframes (Apache 2.0) | Đã có |
| remotion | remotion-dev/remotion | Thư viện; công ty trên 3 người có thể phải mua giấy phép, cần hỏi trước khi dùng |
| remotion skills | remotion-dev/skills | Không thêm: giấy phép chưa rõ |
| gsap-skills | greensock/gsap-skills (MIT) | Đã có |
| motion-design-skill | LottieFiles/motion-design-skill (MIT) | Đã có |

## Đối chiếu 20 repo theo từng lớp (16/10/2026)

Chưa mở trang GitHub để kiểm giấy phép và số sao của danh sách này. Kết luận dựa trên vai trò từng thư viện và những gì kho đã có. Trước khi thêm Satori hoặc Remotion thì kiểm giấy phép.

| Lớp | Repo | Kết luận |
|---|---|---|
| Kỹ năng | remotion-dev/skills | Chưa chép: kho không có tệp giấy phép, chờ PM quyết có chép hay không |
| Kỹ năng | motiondivision/ai-kit | Đã chép thành kỹ năng `motion` ngày 16/10/2026 theo yêu cầu PM (MIT); chỉ dùng cho web, ứng dụng |
| Kỹ năng | greensock/gsap-skills | Đã có (8 kỹ năng `gsap-*`) |
| Thiết kế | svg/svgo (MIT) | Công cụ ngoài, xem `tai-lieu/CONG-CU-NGOAI.md` |
| Thiết kế | vercel/satori (MPL-2.0) | Công cụ ngoài, xem `tai-lieu/CONG-CU-NGOAI.md` |
| Chuyển động | greensock/GSAP | Đã có, là thư viện chính của HyperFrames |
| Chuyển động | juliangarnier/anime | Không cần: HyperFrames đã hỗ trợ sẵn |
| Chuyển động | motiondivision/motion | Thư viện npm, cài trong từng dự án web khi cần |
| Chuyển động | rive-app/rive-wasm | Không cần: hợp giao diện tương tác, không hợp dựng ra MP4 |
| Chuyển động | LottieFiles/dotlottie-web | Không cần: HyperFrames đã hỗ trợ Lottie |
| Video | remotion-dev/remotion | Chưa dùng; công ty trên 3 người có thể phải mua giấy phép, hỏi PM trước |
| Video | motion-canvas/motion-canvas | Không cần: trùng HyperFrames |
| 3D | mrdoob/three.js | Dùng qua HyperFrames cho `video-3d-theo-mau` |
| 3D | pmndrs/react-three-fiber, drei, react-three-rapier, react-postprocessing | Không cần: chỉ có ích khi dựng bằng React (đi theo Remotion) |
| Âm thanh | goldfire/howler.js | Không cần: phát âm thanh trên web; trộn âm đã có `hyperframes-audio`, `sound-layer` |
| Xuất bản | Vanilagy/mediabunny | Không cần: FFmpeg đã làm được |
| Xuất bản | FFmpeg/FFmpeg | Đã có trên máy |
