// Lò xo dạng đóng: mọi giá trị là hàm thuần của t (giây). Không trạng thái, không timer.
// Chép nguyên tệp vào thẻ <script> của tệp HTML (không dùng module: file:// chặn import).

// Tham số kiểu Apple: response = chu kỳ dao động (giây), bounce = 0 (không vọt) .. 0.25 (vọt khoảng 2%, mức tối đa cho phép).
const SPRING = {
  snap:  { response: 0.30, bounce: 0.00 },  // con trỏ, nội dung nhỏ
  base:  { response: 0.42, bounce: 0.22 },  // khối hình đổi kích thước, bo góc
  lazy:  { response: 0.60, bounce: 0.10 },  // cạnh đuôi của chỉ báo tab, camera
};

// Độ lệch còn lại so với đích tại thời điểm t, bắt đầu từ lệch x0, vận tốc v0.
function springOffset(x0, v0, t, { response, bounce }) {
  if (t <= 0) return x0;
  const w = (2 * Math.PI) / response;
  const z = Math.min(1, Math.max(0, 1 - bounce));
  if (z >= 1) return (x0 + (v0 + w * x0) * t) * Math.exp(-w * t);   // tắt dần tới hạn
  const wd = w * Math.sqrt(1 - z * z);
  return Math.exp(-z * w * t) * (x0 * Math.cos(wd * t) + ((v0 + z * w * x0) / wd) * Math.sin(wd * t));
}

// Phản hồi bước: 0 -> 1.
const step = (t, p) => (t <= 0 ? 0 : 1 - springOffset(1, 0, t, p));

// Một giá trị đổi đích nhiều lần = tổng các lò xo, mỗi lần đổi một lò xo.
// keys: [{ t, v, p? }] sắp theo t; key đầu là giá trị lúc bắt đầu. p riêng từng key ghi đè p chung.
// loop = T: cộng đuôi lò xo của vòng trước, để giá trị tại T khớp giá trị tại 0 (cả vận tốc).
//           Bắt buộc: key cuối có v bằng key đầu.
function track(keys, t, p = SPRING.base, loop = 0) {
  let v = keys[0].v;
  for (let i = 1; i < keys.length; i++) {
    const d = keys[i].v - keys[i - 1].v, q = keys[i].p || p;
    v += d * step(t - keys[i].t, q);
    if (loop) v -= d * springOffset(1, 0, t - keys[i].t + loop, q);
  }
  return v;
}

// Kéo trực tiếp: trong lúc giữ chuột, giá trị lấy từ vị trí con trỏ; nhả ra thì lò xo về đích
// từ đúng chỗ đang đứng (kèm vận tốc lúc nhả, đo bằng sai phân).
// hold: { t0, t1 } khoảng giữ; fromCursor(t) -> giá trị khi đang giữ; rest: đích sau khi nhả.
function dragged(t, base, hold, fromCursor, rest, p = SPRING.base) {
  if (t < hold.t0) return base;
  if (t <= hold.t1) return fromCursor(t);
  const h = 1 / 240, x1 = fromCursor(hold.t1);
  const v1 = (x1 - fromCursor(hold.t1 - h)) / h;
  return rest + springOffset(x1 - rest, v1, t - hold.t1, p);
}

// Kéo quá giới hạn thì giãn có lực cản (kiểu iOS): càng kéo càng nặng, không bao giờ vượt quá max + dim.
function rubber(x, min, max, dim, c = 0.55) {
  const over = (d) => (c * d * dim) / (dim + c * d);
  if (x > max) return max + over(x - max);
  if (x < min) return min - over(min - x);
  return x;
}

// Hai cạnh của chỉ báo (tab, núm công tắc) đi trên hai lò xo khác nhau:
// cạnh dẫn nhanh, cạnh đuôi chậm, nên chỉ báo dài ra khi chạy rồi co lại khi tới.
// stops: [{ t, l, r }] vị trí cạnh trái/phải theo thời gian.
function liquidEdges(stops, t, fast = SPRING.snap, slow = SPRING.lazy, loop = 0) {
  const L = [], R = [];
  stops.forEach((s, i) => {
    const right = i > 0 && s.l > stops[i - 1].l;          // đang chạy sang phải
    L.push({ t: s.t, v: s.l, p: right ? slow : fast });
    R.push({ t: s.t, v: s.r, p: right ? fast : slow });
  });
  return { l: track(L, t, fast, loop), r: track(R, t, fast, loop) };
}

// Nội dung đổi trong khối đang biến hình: mỗi lớp có giờ vào và giờ ra riêng, mờ nhòe ngắn,
// lớp cũ ra xong lớp mới mới vào hẳn (gối nhau tối đa `overlap` giây) để chữ không chồng lên nhau.
function swap(t, tIn, tOut, dur = 0.12, overlap = 0.04) {
  const a = Math.min(1, Math.max(0, (t - (tIn + overlap)) / dur));
  const b = Math.min(1, Math.max(0, (t - tOut) / dur));
  const o = a * (1 - b);
  return { opacity: o, blur: (1 - o) * 6, y: (1 - a) * 6 - b * 6 };
}
