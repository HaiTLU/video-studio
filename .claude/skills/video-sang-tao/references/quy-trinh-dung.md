# Quy trình dựng chi tiết

Đường dẫn dưới đây tính từ `.claude/skills/video-sang-tao/` (viết tắt `$K`). Dự án video đặt ở `videos/<YYMMDD>_<DuAn>_<Ten>/`, tên tệp xuất `YYMMDD_<DuAn>_<NoiDung>.mp4`.

## Thiết lập dự án

```bash
export HYPERFRAMES_NO_TELEMETRY=1 DO_NOT_TRACK=1          # tắt gửi số liệu
D=videos/<YYMMDD>_<DuAn>_<Ten>; mkdir -p $D/assets/fonts
cd /tmp && HYPERFRAMES_SKIP_SKILLS=1 npx -y hyperframes@0.8.134 init tam --non-interactive --resolution landscape
cp /tmp/tam/{hyperframes.json,package.json,meta.json} $D/ ; sed -i 's/"proj"\|"tam"/"<ten-video>"/' $D/meta.json
cp $K/scripts/khung.html $D/index.html                    # rồi thay /*FONTS*/ và /*SPRING*/
cp $K/scripts/tao_nhac.py $D/
```

- `/*SPRING*/`: dán nguyên `scripts/spring.js`. `/*FONTS*/`: dán các khối `@font-face` của Be Vietnam Pro 700 và 900 (đổi tên họ phông thành `BVP`) và chép 6 tệp `BeVietnamPro-*.woff2` vào `$D/assets/fonts/`. Nguồn: `brand/fonts/web/` (OFL).
- Bỏ hai tệp `AGENTS.md`, `CLAUDE.md` mà `init` sinh ra.
- HyperFrames ghim bản 0.8.134 (chi tiết và cách nâng bản ở `.claude/skills/video-khoa-hoc/dung-hyperframes.md`).

## Viết cảnh

- Mỗi cảnh là một hàm vẽ nhận `t`; `drawTopLevel` gọi các hàm theo giây. Bảng mốc `PH` (giây theo phách) đặt đầu tệp, mọi cảnh đọc từ đó, nên dời một mốc là sửa một chỗ.
- **Chuyền vật nối giữa các cảnh bằng `track`.** Vị trí chấm là tổng lò xo của các lần đổi đích: `track([{t:0,v:x0},{t:3,v:x1,p:...},{t:5.5,v:x2,p:...}], t)`. Không đặt lại từ đầu mỗi cảnh, nếu không chấm giật ở chỗ nối.
- **Chuyển động cộng thêm** (ví dụ chấm chạy theo đường biểu đồ) tính riêng rồi cộng vào kết quả `track`; các key sau đó đặt đích bằng `đích mong muốn - phần cộng thêm cuối`.
- **Biểu đồ và chấm dùng cùng hàm**: `Y(tp) = step(tp, P.graph)`; đường vẽ lấy mẫu `Y`, chấm đặt tại `Y(tp)`. Lò xo có vọt rõ (`bounce` 0,5 vọt khoảng 16 phần trăm) để biểu đồ có "đỉnh".
- **Chữ rơi/xoay**: mỗi chữ cái có giờ riêng `t0 = tBat + 0.03*i`, `v = S(t,t0,{response:.3,bounce:0})`, vị trí `y + 420*v`, xoay `±0.6*v` rad, mờ dần trong 0,3 giây. Chữ ở lại và chữ đi có giờ khác nhau để không chồng.
- **Hình phủ kín khung**: đĩa bán kính từ `24` tới `1290` (> khoảng cách tới góc 1101); đổi nền sau khi đĩa đã phủ kín.
- **Các hình là trạng thái của một khối**: hình tròn, vuông bo góc, viên thuốc dùng cùng một hàm `pill(cx, cy, w, h, r, color, rot)`; chuyển trạng thái bằng cách nội suy `w, h, r, rot`.
- **Chữ theo vòng tròn**: tính trước góc mỗi chữ cái từ độ rộng chữ, cả vòng xoay `θ(t)`, mỗi chữ quay `a + π/2`. Mở ra ngoài bằng cách tăng bán kính và thu chữ thành chấm nhỏ.
- **Lưới chấm bán sắc**: lưới ô 40 px quanh tâm, cỡ chấm `0.78*ô*sm((Rw - d)/dải)` với `d` là khoảng cách tới tâm, `Rw` là bán kính sóng. Chấm cỡ 0,78 ô thì lấp kín (đường chéo ô là 0,707 ô). Chạy ngược sóng để quay về.
- **Khép vòng lặp**: khung cuối phải bằng khung đầu về mọi thứ (con trỏ, nhãn, nút). Đặt key cuối khớp key đầu; lò xo cuối bắt đầu sớm để phần đuôi còn dưới 0,1 px ở giây cuối (`response 0.24`, bắt đầu cách cuối từ 0,4 giây).

## Nhạc và tiếng động

`python3 tao_nhac.py assets/nhac.wav`: kick mỗi phách, hat ở nửa phách, clap ở phách chẵn, bass nhẹ, kèm tiếng động theo sự kiện (bấm, nhảy, hạ cánh, đĩa phủ khung...). Sửa danh sách sự kiện theo bảng nhịp. Gắn thẻ `<audio id="nhac" class="clip" src="assets/nhac.wav" data-start="0" data-duration="<T>" data-track-index="1" data-volume="0.9">` (phải có `id`, không thêm `crossorigin`). Nghe thử là việc của PM: ghi rõ chưa kiểm nếu chưa ai nghe.

## Kiểm và xuất

```bash
node $K/scripts/chup_anh_tinh.js $D $D/kiem 1.15 4.2 9.6 12.8     # ảnh tĩnh từ cùng mã seek
cd $D && npx -y hyperframes@0.8.134 check                          # 0 lỗi; cảnh báo nested_structure_needs_subcomposition chấp nhận được
npx -y hyperframes@0.8.134 snapshot --no-end --at 12.6 --output /tmp/snap   # kiểm khung qua chính HyperFrames (bắt lỗi đo phông)
python3 $K/scripts/render.py $D --duration <T> --out $D/<ten>.mp4          # nền, khoảng 6 phút cho 15 giây
bash $K/scripts/gan_the_mau.sh $D/<ten>.mp4
ffprobe -v error -show_entries format=duration:stream=nb_frames -of compact $D/<ten>.mp4
```

SSIM khung đầu và cuối: lấy khung 0 và khung cuối bằng `select=eq(n\,N)` rồi `ffmpeg -i cuoi.png -i dau.png -lavfi ssim -f null -`.

## Lỗi đã gặp

| Lỗi | Nguyên nhân và cách tránh |
|---|---|
| Chữ lớn dính nhau trong video nhưng đẹp ở ảnh chụp | `measureText` chạy trước khi phông tải, bị nhớ số đo của phông dự phòng. Chỉ nhớ số đo khi `document.fonts.check` đúng (đã có trong `khung.html`); kiểm bằng `hyperframes snapshot` |
| Màu nhấn trong video sẫm hơn bảng màu | MP4 không có thẻ màu. Chạy `gan_the_mau.sh` |
| `.mp4` không lên Git | `.gitignore` chặn `*.mp4`; giao PM bằng SendUserFile, kho giữ mã, bảng nhịp, ảnh tĩnh, mã nhạc; `nhac.wav` cũng bị chặn nên giữ `tao_nhac.py` |
| Khung cuối khác khung đầu vài điểm ảnh | Đuôi lò xo chưa tắt: bắt đầu lò xo cuối sớm hơn hoặc dùng `response` nhỏ |
| Vệt trắng ở góc khi đĩa phủ khung | Bán kính cuối chưa quá góc: tăng thêm 5 phần trăm |
| Khoảng trống nền thuần trước khi hình vào | Cho hình vào sớm hơn 0,15 giây, kể cả cỡ nhỏ |
| Chấm đè lên chữ trên đường đi | Cho chấm đi vòng dưới dòng chữ hoặc chờ chữ vào xong |
| Thẻ cuối đủ chữ quá muộn, người xem không kịp đọc | Dòng cuối vào sớm 0,3 giây; giữ thẻ tối thiểu 1,3 giây |
| Thẻ `<audio>` thiếu `id` | Video ra không tiếng |
