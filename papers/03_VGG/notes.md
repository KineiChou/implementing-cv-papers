# Very Deep Convolutional Networks for Large-Scale Image Recognition (VGG)

**Authors**: Karen Simonyan, Andrew Zisserman
**Year**: 2014
**Link**: [https://arxiv.org/pdf/1409.1556.pdf](https://arxiv.org/pdf/1409.1556.pdf)

## Key Contributions
- Standardized architecture using only 3x3 convolutions.
- Demonstrated that depth is key to performance.
- VGG-16 and VGG-19 are the most common variants.

## Architecture Details
- **Input**: 224x224 RGB.
- **Blocks**: Stack of conv layers followed by Max Pooling.
- **Filters**: Start at 64, double after each pooling (up to 512).

## Implementation Notes
- High parameter count due to fully connected layers (often replaced by GAP in modern adaptations).
