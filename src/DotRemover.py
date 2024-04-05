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

def transform_text(text):
    transformed_text = []
    words = text.split()
    for word in words:
        transformed_word = transform_characters(word)
        transformed_text.append(transformed_word)
    return ' '.join(transformed_text)

def arabic_diacritics_remover(text):
    """
    Convert Arabic text with diacritics (dots) to dotless text.
    
    Args:
    text (str): Arabic text with diacritics.
    
    Returns:
    str: Dotless Arabic text.
    """
    # Define dictionary mapping diacritics to empty string
    diacritics_map = {
        'َ': '',  # Fatha
        'ُ': '',  # Damma
        'ِ': '',  # Kasra
        'ً': '',  # Tanwin Fath
        'ٌ': '',  # Tanwin Damm
        'ٍ': '',  # Tanwin Kasr
        'ّ': '',  # Shadda
        'ْ': '',  # Sukun
        'ٰ': '',  # Dagger Alef
    }
    
    # Remove diacritics from the text
    for diacritic, replacement in diacritics_map.items():
        text = text.replace(diacritic, replacement)
    
    return text