import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer # type: ignore
from tensorflow.keras.preprocessing.sequence import pad_sequences # type: ignore

def tokenize_char_level(data):
    df = data.copy()
    # Ajout des tokens spéciaux pour indiquer le début et la fin des séquences
    df['dotless'] = df['dotless'].apply(lambda x: 's ' + str(x) + ' e')
    df['text'] = df['text'].apply(lambda x: 's ' + str(x) + ' e')

    # Tokenisation au niveau des caractères
    tokenizer = Tokenizer(char_level=True, filters='')
    tokenizer.fit_on_texts(df['dotless'].tolist() + df['text'].tolist())

    # Conversion des textes en séquences
    input_sequences = tokenizer.texts_to_sequences(df['dotless'])
    target_sequences = tokenizer.texts_to_sequences(df['text'])

    # Padding des séquences
    max_length = max(len(seq) for seq in input_sequences + target_sequences)
    input_sequences = pad_sequences(input_sequences, padding='post', maxlen=max_length)
    target_sequences = pad_sequences(target_sequences, padding='post', maxlen=max_length)

    # Définition des dimensions
    vocab_size = len(tokenizer.word_index) + 1
    latent_dim = 64

    return input_sequences, target_sequences, vocab_size, latent_dim, max_length, tokenizer

