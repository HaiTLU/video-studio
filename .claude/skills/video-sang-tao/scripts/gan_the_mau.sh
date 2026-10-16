#!/bin/bash
# Gắn thẻ màu bt709 cho MP4 vừa dựng, không mã hóa lại: bash gan_the_mau.sh video.mp4
# Lý do: tệp HyperFrames dựng ra không có thẻ màu, vài trình phát hiện màu nhấn sẫm hơn thật.
set -e
f="$1"; tmp="$(mktemp --suffix=.mp4)"
ffmpeg -y -v error -i "$f" -c copy -bsf:v h264_metadata=matrix_coefficients=1:colour_primaries=1:transfer_characteristics=1:video_full_range_flag=0 -movflags +faststart "$tmp"
mv "$tmp" "$f"
ffprobe -v error -select_streams v:0 -show_entries stream=color_space,nb_frames -of compact "$f"
