---
name: tu-cam-ca-du-lieu-mau
description: "Từ PM cấm (vd \"chốt\") áp cả cho chữ mẫu trong giao diện, video, thành phần thiết kế; grep trước khi đưa lên"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 1a24ae4a-db62-4096-9990-e00f4bdc9000
  modified: 2026-10-05T16:50:33.926Z
---

Từ PM cấm (hiện có "chốt", xem [[khong-dung-tu-chot]]) áp cho MỌI chữ Claude viết ra, kể cả dữ liệu mẫu trong giao diện dựng lại, lời chép mẫu, khung Trợ lý, video, bản xem trước thành phần.

**Why:** 5/10/2026 dựng hệ thống thiết kế SonicRec, chữ mẫu "Chốt lịch nghiệm thu..." lọt vào 6 tệp và đã đưa lên Claude Design, phải sửa, dựng và tải lại.

**How to apply:** trước khi tải lên hay gộp, grep từ cấm trong mọi thư mục nguồn (src, docs, previews, templates), không chỉ tệp MD. Thay bằng "thống nhất", "quyết".
