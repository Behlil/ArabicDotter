# ArabicDotter
 Build an NLP model for converting dotless Arabic text to dotted text

## Dotless  characters
| Character | Decimal Code |
|-----------|--------------|
|    ٮ      |     1646     |
|    ح      |     1581     |
|    د      |     1583     |
|    ر      |     1585     |
|    س      |     1587     |
|    ص      |     1589     |
|    ط      |     1591     |
|    ع      |     1593     |
|    ٯ      |     1647     |
|    ڡ      |     1697     |
|    ں      |     1722     |
|    ى      |     1609     |
|    ه      |     1607     |

---------------------------


## Model Architecture

### Overview
The model is designed to convert dotless Arabic text to its dotted version. It utilizes a recurrent neural network (RNN) architecture to learn the mapping between dotless and dotted Arabic characters.

### Architecture
1. **Embedding Layer**
   - Input dimension: 10,000 (vocab_size)
   - Output dimension: 256
   - The embedding layer converts input characters into dense vectors.

2. **Bidirectional LSTM Layers**
   - Two Bidirectional LSTM layers, each with 256 units.
   - `return_sequences=True` ensures that each LSTM layer returns the full sequence of outputs.

3. **Dense Layer**
   - Units: 1024
   - Activation function: ReLU
   - The dense layer helps to capture complex patterns in the sequential data.

4. **Dropout Layer**
   - Rate: 0.5
   - This layer randomly drops 50% of the input units during training to prevent overfitting.

5. **Output Dense Layer**
   - Units: 10,000 (vocab_size)
   - Activation function: Softmax
   - Produces the output probabilities for each token in the vocabulary, representing the dotted Arabic characters.

### Compilation
- Loss function: Sparse categorical cross-entropy
- Optimizer: Adam
- Metrics: Accuracy

### Input Shape
- The model expects input sequences with a length of 100 characters.


