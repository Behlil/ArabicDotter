# ArabicDotter
 Build an NLP model for converting dotless Arabic text to dotted text

 ### Dotless special characters
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


### Table 1: Normal Characters
| Character | Character | Character | Character | Character | Character | Character | Character | Character | Character |
|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
|    ا      |    ب      |    ت      |    ث      |    ج      |    ح      |    خ      |    د      |    ذ      |    ر      |
|    ز      |    س      |    ش      |    ص      |    ض      |    ط      |    ظ      |    ع      |    غ      |    ق      |
|    ف      |    ك      |    ل      |    م      |    ن      |    ه      |    و      |    ي      |    ء      |    ى      |
|    ئ      |    ؤ      |    ة      |    إ      |    أ      |    ٱ      |    آ      |  Space    |           |           |

### Table 2: Decimal Unicode
| Decimal Code | Decimal Code | Decimal Code | Decimal Code | Decimal Code | Decimal Code | Decimal Code | Decimal Code | Decimal Code | Decimal Code |
|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|
|     1575     |     1576     |     1578     |     1579     |     1580     |     1581     |     1582     |     1583     |     1584     |     1585     |
|     1586     |     1587     |     1588     |     1589     |     1590     |     1591     |     1592     |     1593     |     1594     |     1602     |
|     1601     |     1603     |     1604     |     1605     |     1606     |     1607     |     1608     |     1610     |     1569     |     1609     |
|     1574     |     1572     |     1577     |     1573     |     1571     |     1649     |     1570     |     32       |              |              |

### Project steps
To implement a sequence-to-sequence (seq2seq) model for transforming dotless Arabic text to dotted text, you can follow these general steps:

1. **Data Collection and Preprocessing**:
   - Collect a dataset of dotless Arabic text paired with their corresponding dotted versions. This dataset will be used for training the seq2seq model.
   - Preprocess the dataset by tokenizing the input and output sequences into individual characters or tokens. You may also need to handle any data cleaning or normalization tasks.

2. **Tokenization and Vocabulary Creation**:
   - Tokenize the input and output sequences into individual characters or tokens.
   - Create vocabularies for the input and output sequences, mapping each unique token to a unique index. This step is essential for converting text data into numerical format that the model can process.

3. **Model Architecture**:
   - Design the architecture of the seq2seq model. It typically consists of an encoder and a decoder.
   - The encoder takes the input sequence (dotless text) and processes it into a fixed-length vector representation, capturing the semantic information of the input.
   - The decoder takes the vector representation from the encoder and generates the output sequence (dotted text) one token at a time.

4. **Training**:
   - Split the dataset into training, validation, and possibly test sets.
   - Train the seq2seq model on the training data using techniques like teacher forcing, where the decoder is fed the ground-truth tokens from the target sequence during training.
   - Monitor the model's performance on the validation set to prevent overfitting and fine-tune hyperparameters as needed.

5. **Evaluation**:
   - Evaluate the trained model on the test set to measure its performance in generating accurate dotted text from dotless input.
   - Use metrics such as BLEU score or edit distance to quantify the quality of the generated output compared to the ground truth.

6. **Inference**:
   - Use the trained model for inference by feeding dotless text as input and generating dotted text as output.
   - Implement a decoding strategy such as greedy decoding or beam search to generate the output sequence based on the probabilities predicted by the model.

7. **Deployment**:
   - Once satisfied with the model's performance, deploy it for use in your application or system.
   - Ensure that the deployment environment can handle the computational requirements of the model, especially if deploying on resource-constrained devices or in real-time applications.

