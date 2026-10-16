---
name: feedback-luon-chay-humanizer
description: "Luôn chạy kỹ năng humanizer cho mọi chữ dài viết ra, kể cả ở kho SR; nếu Skill báo không có thì đọc SKILL.md và tieng-viet.md rồi rà tay"
metadata:
  node_type: memory
  type: feedback
  originSessionId: c895fc2f-b2aa-40ec-a917-ef076262121b
  modified: 2026-10-04T09:47:35.044Z
---

PM dặn 4/10/2026: "luôn chạy humanizer skill khi viết". Lần đó tôi bỏ qua bước này cho trang kế hoạch tuần đầu của SR vì công cụ Skill báo "Unknown skill: humanizer" (kỹ năng nằm ở `.claude/skills/humanizer/` của kho Trường, không có trong kho sonicrec-congty), rồi chỉ rà tay.

**Why:** CLAUDE.md quy tắc 9 đã yêu cầu; PM nhắc lại vì tôi để lọt.
**How to apply:** trước khi giao chữ dài (báo cáo, thư, trang HTML, tệp MD), gọi Skill `humanizer`; nếu không có thì đọc `SKILL.md` và `tieng-viet.md` ở `<kho Trường>/.claude/skills/humanizer/` (đường dẫn worktree cũng có) và rà theo đó, rồi nói rõ đã làm. Không đổi câu khuôn, số liệu, tên riêng. Liên quan [[sr-hai-phong-moi-hoc-hang-ngay]].
