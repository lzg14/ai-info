# ELECTRA: 判别式预训练文本编码器

斯坦福大学与Google Brain团队联合提出了一种名为ELECTRA的新型预训练语言模型，该模型创新性地将文本编码器训练为判别器而非生成器。传统的[BERT](../../../glossary/terms/bert.md)等模型采用掩码语言建模（MLM）方法，通过替换部分token后训练模型重建原始token，虽然效果良好但计算成本高昂。ELECTRA则引入对抗式训练机制，使用生成器替换序列中的token，再训练判别器识别哪些token被替换过。这种预训练任务被称为替换token检测（RTD），能够更高效地学习上下文表示。研究团队在GLUE、SQuAD等基准测试上验证了模型性能，实验表明ELECTRA在相同算力下显著优于BERT和XLNet等模型，为自然语言处理预训练开辟了新的技术路径。








## 相关文章
- [OpenAI GPT-1 Paper Release](../../2018/06/2018-06-11-openai-gpt-1-release.md)
- [Google BERT Model Release](../../2018/10/2018-10-11-google-bert-release.md)
- [OpenAI Releases GPT-2 1.5B Language Model](../../2019/02/2019-02-14-gpt2-release.md)
- [无标题](../../2019/11/2019-11-06-facebook-xlm-r-multilingual.md)
- [OpenAI Releases Full GPT-2 1.5B Model](../../2019/11/2019-11-06-gpt2-full-release.md)

tags: [BERT, Google, 上下文, 开源, Transformer, GPT, OpenAI]
