import re
import pandas as pd

def replace_punctuations(text):
    arabic_punctuation = '؟،؛'
    english_punctuation = r"!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    all_punctuation = arabic_punctuation + english_punctuation
    return text.translate(str.maketrans(all_punctuation, ' ' * len(all_punctuation)))

def remove_arabic_diacritics(text):
    diacritics = [
        '\u064B',  # fathatan
        '\u064C',  # dammatan
        '\u064D',  # kasratan
        '\u064E',  # fatha
        '\u064F',  # damma
        '\u0650',  # kasra
        '\u0651',  # shadda
        '\u0652'   # sukun
    ]
    for diacritic in diacritics:
        text = text.replace(diacritic, '')
    return text

def normalize_alef(text):
    alef_variants = ['أ', 'إ', 'آ']
    for alef in alef_variants:
        text = text.replace(alef, 'ا')
    return text

def remove_english_chars(text):
    return re.sub(r'[a-zA-Z]', '', text)

def delete_duplicate_spaces(text):
    return re.sub(r'\s+', ' ', text)

def transform_characters(word):
    transformed_word = []
    for i, char in enumerate(word):
        char_code = ord(char)
        if char_code in [1576, 1578, 1579]:  # ب، ت، ث
            transformed_word.append(chr(1646))
        elif char_code in [1580, 1582]:  # ج، خ
            transformed_word.append(chr(1581))
        elif char_code == 1584:  # ذ
            transformed_word.append(chr(1583))
        elif char_code == 1586:  # ز
            transformed_word.append(chr(1585))
        elif char_code == 1588:  # ش
            transformed_word.append(chr(1587))
        elif char_code == 1590:  # ض
            transformed_word.append(chr(1589))
        elif char_code == 1592:  # ظ
            transformed_word.append(chr(1591))
        elif char_code == 1594:  # غ
            transformed_word.append(chr(1593))
        elif char_code in [1601, 1602]:  # ف، ق
            if i == len(word) - 1:
                transformed_word.append(chr(1647))
            else:
                transformed_word.append(chr(1697))
        elif char_code == 1606:  # ن
            if i == len(word) - 1:
                transformed_word.append(chr(1722))
            else:
                transformed_word.append(chr(1646))
        elif char_code == 1577:  # ة
            transformed_word.append(chr(1607))
        elif char_code == 1610:  # ي
            if i == len(word) - 1:
                transformed_word.append(chr(1609))
            else:
                transformed_word.append(chr(1646))
        else:
            transformed_word.append(char)
    return ''.join(transformed_word)

def to_dotless_text(text):
    words = text.split()
    transformed_words = [transform_characters(word) for word in words]
    return ' '.join(transformed_words)

def clean_text(text):
    text = replace_punctuations(text)
    text = remove_arabic_diacritics(text)
    text = normalize_alef(text)
    text = remove_english_chars(text)
    text = delete_duplicate_spaces(text)
    return text



def clean_and_export_data(parquet_path, output_csv_path):
    """
    Cleans the text data from a specified Parquet file, applies text cleaning 
    and transformation functions, and exports the cleaned data to a CSV file.
    
    Args:
    - parquet_path (str): Path to the input Parquet file containing text data.
    - output_csv_path (str): Path where the cleaned data CSV will be saved.
    """
    # Load data from parquet file
    data = pd.read_parquet(parquet_path)
    
    # Clean and transform text columns
    data["text"] = data["clean"].apply(clean_text)
    data["dotless"] = data["text"].apply(to_dotless_text)
    
    # Drop unnecessary columns
    data = data.drop(columns=["clean"])
    
    # Reset index
    data = data.reset_index(drop=True)
    
    # Export cleaned data to CSV file
    data.to_csv(output_csv_path, index=False)
    print(f"Cleaned data saved to {output_csv_path}")

