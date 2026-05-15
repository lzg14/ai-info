<!-- {"title": "加速设备端AI：Arm与Google AI Edge的优化实践", "url": "https://developers.googleblog.com/accelerating-on-device-ai-a-look-at-arm-and-google-ai-edge-optimization", "source": "Google Developers Blog（RSS）", "source_url": "", "publish_date": "2026-05-14", "score": null, "tags": "[\"技巧\"]"} -->
# 加速设备端AI：Arm与Google AI Edge的优化实践

📅 2026-05-14
📢 来源：Google Developers Blog（RSS）

> Arm第二代可扩展矩阵扩展（SME2）与Google AI Edge软件栈集成，将CPU转变为强大的矩阵计算加速器，从而实现高性能的设备端生成式AI。本文以Stability AI的"stable-audio-open-small"模型为例，阐述了利用LiteRT、XNNPACK和KleidiAI构建的"转换、优化、部署"自动化硬件加速流程。该方案在基于Arm架构的移动设备和笔记本电脑上，成功实现了音频生成速度提升2倍以上、内存使用减少4倍的显著效果，同时确保了高音频质量。这一集成方案为在资源受限的边缘设备上高效运行复杂AI模型提供了有效路径。

🏷️ [ · " · 技 · 巧 · " · ]

<!-- 正文开始 -->

Arm第二代可扩展矩阵扩展（SME2）与Google AI Edge软件栈集成，将CPU转变为强大的矩阵计算加速器，从而实现高性能的设备端生成式AI。本文以Stability AI的"stable-audio-open-small"模型为例，阐述了利用LiteRT、XNNPACK和KleidiAI构建的"转换、优化、部署"自动化硬件加速流程。该方案在基于Arm架构的移动设备和笔记本电脑上，成功实现了音频生成速度提升2倍以上、内存使用减少4倍的显著效果，同时确保了高音频质量。这一集成方案为在资源受限的边缘设备上高效运行复杂AI模型提供了有效路径。

<!-- 正文结束 -->