# ImageNet Classification with Deep Convolutional Neural Networks (AlexNet)

**Authors**: Alex Krizhevsky, Ilya Sutskever, Geoffrey E. Hinton
**Year**: 2012
**Link**: [https://proceedings.neurips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf](https://proceedings.neurips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf)

## Key Contributions
- Won ILSVRC 2012 by a large margin.
- Popularized ReLU nonlinearity for faster training.
- Used Dropout to reduce overfitting.
- Efficient GPU implementation (split across 2 GPUs).

## Architecture Details
- **Input**: 224x224x3 images.
- **Layers**: 5 Convolutional layers, 3 Fully Connected layers.
- **Key Features**: ReLU, LRN (Local Response Normalization), Overlapping Pooling.

## Implementation Notes
- LRN is often replaced by Batch Normalization in modern variants.
