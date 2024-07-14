<!-- # ArabicDotter
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

--------------------------- -->


# ReadMe

## Project Title: Dotless to Dotted Arabic Text Conversion using NLP

### Description
This project aims to develop a Natural Language Processing (NLP) model to convert dotless Arabic text to its dotted form. Arabic text without diacritics (dots) can be ambiguous and hard to read. The model leverages advanced techniques like Long Short-Term Memory (LSTM) and Gated Recurrent Units (GRU), utilizing Byte Pair Encoding (BPE) and character-level tokenizers for efficient and accurate text processing.

### Table of Contents
- [Description](#description)
- [Features](#features)
- [Model Architecture](#model-architecture)
- [Training and Evaluation](#training-and-evaluation)
- [Dataset](#dataset)
- [License](#license)
- [Contact](#contact)

### Features
- Converts dotless Arabic text to dotted Arabic text.
- Uses LSTM and GRU neural network architectures.
- Implements Byte Pair Encoding (BPE) and character-level tokenizers.
- Provides high accuracy.

### Model Architecture
The project employs two primary neural network architectures:
- **LSTM (Long Short-Term Memory)**: LSTMs are effective in capturing long-term dependencies and are suitable for sequence-to-sequence tasks like text conversion.
- **GRU (Gated Recurrent Units)**: GRUs are similar to LSTMs but have a simpler structure, making them computationally efficient.

Both models are trained using character-level and BPE tokenizers:
- **Character-level Tokenizer**: Processes text at the character level, handling each character as a distinct token.
- **Byte Pair Encoding (BPE) Tokenizer**: Compresses text data by merging frequently occurring sequences of characters, balancing between character and word-level representations.

### Training and Evaluation
The training process involves:
1. **Data Preparation**: Preprocessing text data to create training and validation sets.
2. **Model Training**: Training LSTM and GRU models on the prepared datasets.
3. **Evaluation**: Assessing model performance using accuracy.

### Dataset
The dataset used in this project is available [here](https://huggingface.co/datasets/dot-ammar/AR-dotless-medium
)


### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Contact
For any questions or feedback, please contact [bahlil2001@gmail.com](mailto:bahlil2001@gmail.com).

