### Continuous Batching

**英文：** Continuous Batching

**解释：**

Continuous Batching（也叫 Iteration-Level Batching）是 vLLM 提出的推理优化技术。传统批处理需要等一批请求全部完成才能处理下一批，容易造成算力浪费；Continuous Batching 的做法是：当某个请求完成时，立即用新请求替换它，实现了请求级别的「动态组队」，将 GPU 利用率大幅提升。

**为什么重要：** Continuous Batching 是 vLLM 高吞吐量的另一关键因素，结合 PagedAttention，使 vLLM 吞吐量达到 HuggingFace 的 24 倍。
