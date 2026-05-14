<!-- {"title": "Stochastic KV Routing: 实现自适应深度方向的缓存共享", "url": "https://machinelearning.apple.com/research/stochastic-kv-routing", "source": "Apple Machine Learning Research（RSS）", "source_url": "", "publish_date": "2026-05-14", "score": null, "tags": "[\"论文\"]"} -->
# Stochastic KV Routing: 实现自适应深度方向的缓存共享

📢 来源：Apple Machine Learning Research（RSS）

🏷️ [ · " · 论 · 文 · " · ]

<!-- 正文开始 -->

为降低大语言模型推理时KV缓存的高昂内存开销，研究提出了一种沿模型深度维度优化的新方法。该方法通过随机KV路由，在Transformer模型的各层之间动态共享KV缓存，而非每层保留完整独立缓存。实验表明，在保持模型质量基本不变的前提下，该方法能将KV缓存的内存占用减少高达50%，为降低大模型服务成本提供了与现有时间轴压缩、淘汰技术正交的新优化路径。

<!-- 正文结束 -->