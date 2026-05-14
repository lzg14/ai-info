<!-- {"title": "OpenAI Codex 官方迁移指南：一键迁移 Agent 资产", "url": "https://x.com/shao__meng/status/2051840291834052863", "source": "X：邵猛 (@shao__meng)", "source_url": "", "publish_date": "2026-05-14", "score": null, "tags": "[\"技巧\"]"} -->
# OpenAI Codex 官方迁移指南：一键迁移 Agent 资产

📢 来源：X：邵猛 (@shao__meng)

> OpenAI 为 Codex 发布官方迁移方案，支持从其他 AI Coding Agents 一键导入指令、配置、技能、近30天会话等资产。迁移采用“自动迁移+残留兜底”设计：通过用户级和项目级双层扫描，执行检测、迁移、回检的四步循环；自动处理可识别配置后，对剩余部分使用 `migrate-to-codex` skill 手动处理。需注意 Slash commands 被归入 Skills 体系，且会话历史仅限30天。迁移完成后，必须人工复核工具权限、MCP服务器认证、Hooks行为差异等五类内容，因平台间语义或实现差异可能影响功能。

🏷️ [ · " · 技 · 巧 · " · ]

<!-- 正文开始 -->

OpenAI 为 Codex 发布官方迁移方案，支持从其他 AI Coding Agents 一键导入指令、配置、技能、近30天会话等资产。迁移采用“自动迁移+残留兜底”设计：通过用户级和项目级双层扫描，执行检测、迁移、回检的四步循环；自动处理可识别配置后，对剩余部分使用 `migrate-to-codex` skill 手动处理。需注意 Slash commands 被归入 Skills 体系，且会话历史仅限30天。迁移完成后，必须人工复核工具权限、MCP服务器认证、Hooks行为差异等五类内容，因平台间语义或实现差异可能影响功能。

<!-- 正文结束 -->