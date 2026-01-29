# Gradient-Based Learning Applied to Document Recognition (LeNet-5)

**Authors**: Yann LeCun, Léon Bottou, Yoshua Bengio, and Patrick Haffner
**Year**: 1998
**Link**: [http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf](http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf)

## Key Contributions
- Introduced LeNet-5, a pioneering CNN architecture.
- Demonstrated the effectiveness of gradient-based learning for document recognition.
- Showed that CNNs are robust to geometric distortions.

## Architecture Details
- **Input**: 32x32 pixel images.
- **Layers**: C1 (Conv), S2 (Subsampling), C3 (Conv), S4 (Subsampling), C5 (Conv), F6 (Fully Connected), Output (RBF).
- **Activation**: Tanh / Sigmoid (modern implementations use ReLU).

## Implementation Notes
- Original used average pooling; modern often uses max pooling.
