# DeepMind WaveNet：原始音频生成的革命

2016年9月，DeepMind发表WaveNet论文，提出一种能够生成原始音频波形的深度神经网络，在语音合成（TTS）和音乐生成任务上实现了质的飞跃。

## 技术创新

WaveNet使用空洞卷积（Dilated Causal Convolutions）构建自回归模型，逐样本生成音频波形。这种方法生成的音频质量远超当时的拼接合成和参数合成方法，人类听众评分显示WaveNet生成的语音与真实人类语音几乎无法区分。

## 应用

Google将WaveNet技术应用于Google Assistant的语音合成，使语音助手的自然度大幅提升。同时DeepMind也展示了WaveNet生成古典钢琴曲的能力，证明了生成模型在音乐创作上的潜力。

## 后续

WaveNet之后，Tacotron、FastSpeech、[Transformer](../../../glossary/terms/transformer.md)-TTS等模型相继出现，端到端语音合成成为主流。WaveNet开创的深度生成模型方法后来也影响了音频、音乐生成领域。








## 相关文章
- [微软研究院语音识别深度学习取得重大突破](../../2012/06/2012-06-20-microsoft-speech-recognition-deep-learning.md)
- [微软亚洲研究院ResNet：深度残差网络刷新视觉识别纪录](../../2013/03/2013-03-01-微软亚洲研究院ResNet-深度残差网络刷新视觉识别纪录.md)
- [Google DeepDream：神经网络可视化打开视觉黑箱](../../2013/06/2013-06-01-Google-DeepDream-神经网络可视化打开视觉黑箱.md)
- [Bengio团队提出循环神经网络语言模型](../../2013/10/2013-10-18-bengio-rnn.md)
- [NIPS 2013：深度学习从学术边缘走向主流](../../2013/10/2013-12-01-NIPS-2013-深度学习从学术边缘走向主流.md)

tags: [论文, Transformer, Google, 语音, 语音合成, 神经网络, 机器学习, 微软]
