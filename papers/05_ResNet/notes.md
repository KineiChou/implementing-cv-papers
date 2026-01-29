# Deep Residual Learning for Image Recognition (ResNet)

**Authors**: Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun
**Year**: 2015
**Link**: [https://arxiv.org/pdf/1512.03385.pdf](https://arxiv.org/pdf/1512.03385.pdf)

## Key Contributions
- Solved the vanishing gradient problem for very deep networks.
- Introduced **Residual Connections** (skip connections): $y = F(x) + x$.
- Trained networks with 152+ layers.

## Architecture Details
- **Residual Block**: Two 3x3 convs with a skip connection.
- **Bottleneck Block**: 1x1 -> 3x3 -> 1x1 (used in ResNet-50+).
- **Pooling**: Global Average Pooling at the end.

## Implementation Notes
- Standard backbone for many modern vision tasks.
- Batch Normalization is crucial.
