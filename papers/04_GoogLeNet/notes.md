# Going Deeper with Convolutions (GoogLeNet / Inception v1)

**Authors**: Christian Szegedy et al.
**Year**: 2014
**Link**: [https://arxiv.org/pdf/1409.4842.pdf](https://arxiv.org/pdf/1409.4842.pdf)

## Key Contributions
- Introduced the **Inception Module**: parallel convolutions of different sizes (1x1, 3x3, 5x5).
- Efficient parameter usage compared to AlexNet/VGG.
- Used Global Average Pooling (GAP) instead of heavy FC layers.
- Auxiliary classifiers for training deep networks.

## Architecture Details
- **Depth**: 22 layers.
- **Inception Module**: Concatenates outputs of different filters.
- **1x1 Convolutions**: Used for dimensionality reduction (bottleneck).

## Implementation Notes
- Complex architecture to implement from scratch.
- Auxiliary classifiers are only used during training.
