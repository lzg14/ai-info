# Google 发布 Imagen：文本到图像生成的新竞争者

## 摘要

2022 年 5 月，Google Research 发布 Imagen——一个基于大规模 [Transformer](../../../glossary/terms/transformer.md) 的文本到图像扩散模型。Imagen 在 COCO 基准测试中取得了 7.27 的 FID 分数（越低越好），刷新了当时该任务的 SOTA，被认为是 DALL-E 2 的最强竞争者。

## 技术特点

**MM-DiT 架构：** Imagen 使用新型 Mixed-Model DIT 架构，结合了 Transformer 和扩散模型的优势，在保持高质量生成的同时支持高分辨率输出。

**超分辨率级联：** 采用多级扩散模型级联架构，从 64×64 → 256×256 → 1024×1024，逐步提升图像分辨率和质量。

**大型语言模型文本编码器：** Imagen 首次使用 T5 大型语言模型（11B 参数）作为文本编码器，比 CLIP 的视觉语言预训练更善于理解复杂文本描述。

## 与 DALL-E 2 的对比

| 指标 | Imagen | DALL-E 2 |
|------|--------|----------|
| 基准 FID | 7.27 | ~10 |
| 文本理解 | T5 XXL | CLIP |
| 开源 | 否 | 否 |
| 公开访问 | 否 | 仅限邀请 |

## 点评

 Imagen 证明了「文本编码器越大，图像生成质量越好」——这是将大语言模型能力迁移到视觉生成领域的成功实践。








## 相关文章
- [OpenAI GPT-1 Paper Release](../../2018/06/2018-06-11-openai-gpt-1-release.md)
- [Google BERT Model Release](../../2018/10/2018-10-11-google-bert-release.md)
- [OpenAI Releases GPT-2 1.5B Language Model](../../2019/02/2019-02-14-gpt2-release.md)
- [无标题](../../2019/11/2019-11-06-facebook-xlm-r-multilingual.md)
- [OpenAI Releases Full GPT-2 1.5B Model](../../2019/11/2019-11-06-gpt2-full-release.md)

tags: [图像生成, 开源, Transformer, Google, 机器人, BERT, GPT, OpenAI]