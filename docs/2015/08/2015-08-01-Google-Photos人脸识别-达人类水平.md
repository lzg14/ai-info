# Google Photos人脸识别：达人类水平

2015年，Google在YouTube视频人脸识别基准（MEGAFACE）上取得了突破性成绩，其FaceNet系统将人脸识别的准确率推向新高度。同时Google Photos的自动人脸聚类和搜索功能也达到实用水平。

## FaceNet的突破

FaceNet使用三元组损失（Triplet Loss）直接学习人脸的128维嵌入向量，在LFW基准上达到99.63%的准确率，创造了纪录。三元组损失的核心是让同一人的人脸向量距离尽可能小，不同人尽可能大。

## Google Photos功能

Google Photos的自动人脸分组功能使用了这一技术：AI会自动识别照片中的人物，将同一个人物的照片聚合成相册，用户可以为人脸命名，方便搜索。

## 隐私影响

这一技术的普及也带来了隐私担忧：Google可以识别任意照片中的人物，甚至可以在用户不知情的情况下建立人脸数据库。人脸识别技术的隐私问题成为社会热点。








## 相关文章
- [Batch Normalization：2015年革命的前奏](../../2014/12/2014-12-01-Batch-Normalization-2015年革命的前奏.md)
- [Facebook DeepFace：97.35%人脸识别精度，超越人类水平](../../2014/12/2014-12-01-Facebook-DeepFace-97.35percent人脸识别精度-超越人类水平.md)
- [DeepFace：人脸识别97.35%，首次超越人类](../../2014/08/2014-03-01-DeepFace-人脸识别97.35percent-首次超越人类.md)
- [Batch Normalization论文发表，深度学习训练稳定性突破](../03/2015-03-10-batch-normalization-paper.md)
- [Google Photos：基于深度学习的智能相册](../05/2015-05-01-Google-Photos-基于深度学习的智能相册.md)

tags: [Google, 人脸识别, 深度学习, 神经网络, DeepFace, 论文]