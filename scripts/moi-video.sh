#!/usr/bin/env bash
# Tạo thư mục video mới: bash scripts/moi-video.sh <DuAn> <TenVideo> [portrait|landscape|square]
set -euo pipefail
[ $# -ge 2 ] || { echo "Cách dùng: bash scripts/moi-video.sh <DuAn> <TenVideo> [portrait|landscape|square]"; exit 1; }
DUAN="$1"; TEN="$2"; KHO="${3:-portrait}"
GOC="$(cd "$(dirname "$0")/.." && pwd)"
DICH="$GOC/videos/$(date +%y%m%d)_${DUAN}_${TEN}"
[ -e "$DICH" ] && { echo "Đã có $DICH"; exit 1; }
export HYPERFRAMES_NO_TELEMETRY=1 DO_NOT_TRACK=1 HYPERFRAMES_SKIP_SKILLS=1
TAM="$(mktemp -d)"
( cd "$TAM" && npx -y hyperframes@0.8.134 init proj --non-interactive --resolution "$KHO" >/dev/null )
mkdir -p "$DICH/assets/fonts" "$DICH/out"
for f in index.html hyperframes.json package.json meta.json; do
  [ -f "$TAM/proj/$f" ] && cp "$TAM/proj/$f" "$DICH/"
done
cp "$GOC"/brand/fonts/*.otf "$GOC"/brand/fonts/*.ttf "$DICH/assets/fonts/"
cp "$GOC/brand/logo-tlu.png" "$DICH/assets/"
cat > "$DICH/TIEN-DO.md" <<MD
# Tiến độ: $TEN ($DUAN)

- Khổ: $KHO
- Kỹ năng dùng:
- Đã kiểm (lint, check, snapshot, ra-soat-video):
- Câu hỏi PM chưa trả lời:
- Bước tiếp:
MD
echo "Đã tạo $DICH"
