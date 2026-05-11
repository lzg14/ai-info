<!--
{
  "title": "Geoffrey Hinton Proposes Capsule Networks",
  "date": "2013-07-31",
  "source": "Association for the Advancement of Artificial Intelligence",
  "source_url": "https://www.aaai.org/Magazine/Monograph/Deep-Learning.pdf",
  "score": "精选"
}
-->

# Geoffrey Hinton Proposes Capsule Networks

📅 2013-07-31 | 📎 Association for the Advancement of Artificial Intelligence | ⭐ 精选

<!-- 正文开始 -->
In July 2013, Geoffrey Hinton, the British-Canadian cognitive psychologist and computer scientist who would later share the Turing Award with Yoshua Bengio and Yann LeCun for their contributions to deep learning, began circulating ideas that would eventually evolve into capsule networks, a fundamentally new architecture for neural networks designed to address fundamental limitations in the way conventional deep learning systems represent spatial hierarchies and visual understanding. Hinton had been thinking about the problem for decades, motivated by his understanding of how the human visual system efficiently represents objects and their properties through structured hierarchies of neural modules that capture not just what objects exist in a scene but how they relate to each other spatially. The core insight behind capsule networks was that traditional neural networks used scalar activations to represent the presence of features, whereas using small vectors or matrices to represent the instantiation parameters of features including position, orientation, scale, and deformation would allow networks to capture much richer information about object geometry and pose. This approach addressed a significant weakness of conventional computer vision systems, which often failed catastrophically when images were viewed from novel angles or perspectives different from those in their training data, a problem known as the "viewport assumption" that humans somehow manage to avoid. Hinton presented these ideas at various workshops and conferences throughout 2013, generating considerable excitement among researchers who recognized the potential to overcome persistent limitations in visual reasoning capabilities. The concept of capsules would not be fully formalized in a published paper until 2017, but the early formulations circulated in 2013 planted seeds that inspired a generation of researchers to explore more structured representations in neural networks rather than relying purely on distributed representations that seemed to require unrealistic amounts of training data to generalize robustly.
<!-- 正文结束 -->
