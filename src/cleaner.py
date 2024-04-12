import re

def replace_ponctuations(text):
    arabic_punctuation = '؟،؛'
    english_punctuation = r"!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    ponctuation = arabic_punctuation + english_punctuation
    return text.translate(str.maketrans(ponctuation, ' ' * len(ponctuation)))

def remove_arabic_dialects(text):
    # remove fathatan
    text = text.replace('\u064B', '')
    # remove dammatan
    text = text.replace('\u064C', '')
    # remove kasratan
    text = text.replace('\u064D', '')
    # remove fatha
    text = text.replace('\u064E', '')
    # remove damma
    text = text.replace('\u064F', '')
    # remove kasra
    text = text.replace('\u0650', '')
    # remove shadda
    text = text.replace('\u0651', '')
    # remove sukun
    text = text.replace('\u0652', '')
    return text

def normalize_alef(text):
    text = text.replace('أ', 'ا')
    text = text.replace('إ', 'ا')
    text = text.replace('آ', 'ا')
    return text



def remove_english_chars(text):
    clean_text = re.sub(r'[a-zA-Z]', '', text)
    return clean_text

def normalize_alef(text):
    clean_text = text.replace('أ', 'ا')
    clean_text = clean_text.replace('إ', 'ا')
    clean_text = clean_text.replace('آ', 'ا')
    return clean_text

def delete_duplicate_spaces(text):
    return re.sub(r'\s+', ' ', text)

def transform_characters(word):
    transformed_word = []
    for i, char in enumerate(word):
        char_code = ord(char)
        if char_code in [1576, 1578, 1579]:
            transformed_word.append(chr(1646))
        elif char_code in [1580, 1582]:
            transformed_word.append(chr(1581))
        elif char_code == 1584:
            transformed_word.append(chr(1583))
        elif char_code == 1586:
            transformed_word.append(chr(1585))
        elif char_code == 1588:
            transformed_word.append(chr(1587))
        elif char_code == 1590:
            transformed_word.append(chr(1589))
        elif char_code == 1592:
            transformed_word.append(chr(1591))
        elif char_code == 1594:
            transformed_word.append(chr(1593))
        elif char_code in [1601, 1602]:
            if i == len(word) - 1:
                transformed_word.append(chr(1647))
            else:
                transformed_word.append(chr(1697))
        elif char_code == 1606:
            if i == len(word) - 1:
                transformed_word.append(chr(1722))
            else:
                transformed_word.append(chr(1646))
        elif char_code == 1577:
            transformed_word.append(chr(1607))
        elif char_code == 1610:
            if i == len(word) - 1:
                transformed_word.append(chr(1609))
            else:
                transformed_word.append(chr(1646))
        else:
            transformed_word.append(char)
    return ''.join(transformed_word)

def to_dotless_text(text):
    transformed_text = []
    words = text.split()
    for word in words:
        transformed_word = transform_characters(word)
        transformed_text.append(transformed_word)
    return ' '.join(transformed_text)

def clean_text(text):
    text = replace_ponctuations(text)
    text = remove_arabic_dialects(text)
    text = normalize_alef(text)
    text = remove_english_chars(text)
    text = delete_duplicate_spaces(text)
    return text


