<!-- {"title": "在谷歌TPU上实现3倍加速：UCSD利用扩散式推测解码优化LLM推理", "url": "https://developers.googleblog.com/supercharging-llm-inference-on-google-tpus-achieving-3x-speedups-with-diffusion-style-speculative-decoding", "source": "Google Developers Blog（RSS）", "source_url": "", "publish_date": "2026-05-14", "score": null, "tags": "[\"论文\"]"} -->
# 在谷歌TPU上实现3倍加速：UCSD利用扩散式推测解码优化LLM推理

📢 来源：Google Developers Blog（RSS）

> 加州大学圣地亚哥分校的研究团队在谷歌TPU上成功部署了DFlash，一种基于块扩散的推测解码方法。该方法突破传统自回归草稿生成的序列性瓶颈，通过单次前向传播并行“绘制”整个候选令牌块，而非逐个预测。系统平均实现了3.13倍的推理加速，峰值性能接近EAGLE-3等现有方法的两倍。这一开源方案已集成至vLLM生态系统，通过利用“免费”的并行验证能力和针对复杂推理任务的高质量草稿预测，显著优化了TPU硬件的利用效率。

🏷️ [ · " · 论 · 文 · " · ]

<!-- 正文开始 -->

加州大学圣地亚哥分校的研究团队在谷歌TPU上成功部署了DFlash，一种基于块扩散的推测解码方法。该方法突破传统自回归草稿生成的序列性瓶颈，通过单次前向传播并行“绘制”整个候选令牌块，而非逐个预测。系统平均实现了3.13倍的推理加速，峰值性能接近EAGLE-3等现有方法的两倍。这一开源方案已集成至vLLM生态系统，通过利用“免费”的并行验证能力和针对复杂推理任务的高质量草稿预测，显著优化了TPU硬件的利用效率。

<!-- 正文结束 -->