import numpy as np
import pandas as pd
from tokenizers import Tokenizer, models, trainers, pre_tokenizers
from tensorflow.keras.preprocessing.sequence import pad_sequences # type: ignore

def BPE_tokenize_data(data):
    df = data.copy()
    # Ajout des tokens spéciaux pour indiquer le début et la fin des séquences
    df['dotless'] = df['dotless'].apply(lambda x: 's ' + str(x) + ' e')
    df['text'] = df['text'].apply(lambda x: 's ' + str(x) + ' e')

    # Initialisation du tokenizer BPE
    tokenizer = Tokenizer(models.BPE())
    trainer = trainers.BpeTrainer(special_tokens=["<s>", "<e>", "<pad>"])

    # Pré-tokenisation
    tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()

    # Formation du tokenizer
    tokenizer.train_from_iterator(df['dotless'].tolist() + df['text'].tolist(), trainer)

    # Encodeur et décodeur
    tokenizer.enable_padding(pad_id=tokenizer.token_to_id("<pad>"))

    # Conversion des textes en séquences
    def encode_sequences(texts):
        return [tokenizer.encode(text).ids for text in texts]

    input_sequences = encode_sequences(df['dotless'])
    target_sequences = encode_sequences(df['text'])

    # Padding des séquences
    max_length = max(max(len(seq) for seq in input_sequences), max(len(seq) for seq in target_sequences))
    input_sequences = pad_sequences(input_sequences, padding='post', maxlen=max_length, value=tokenizer.token_to_id("<pad>"))
    target_sequences = pad_sequences(target_sequences, padding='post', maxlen=max_length, value=tokenizer.token_to_id("<pad>"))

    # Définition des dimensions
    vocab_size = tokenizer.get_vocab_size()
    latent_dim = 64
    
    return input_sequences, target_sequences, vocab_size, latent_dim, max_length, tokenizer

