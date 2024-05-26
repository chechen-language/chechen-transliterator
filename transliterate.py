import json
import re
import unicodedata

class ChechenTransliterator:
    def __init__(self, filename='cyrl_latn_dictionary.json'):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.transliteration = data['cyrl_latn']

    def transliterate_word(self, word):
        result = ''
        i = 0
        while i < len(word):
            match = None
            # Check all case variations
            for key in [
                word[i:i + 3], # Try to match 3 character
                word[i:i + 2], # Try to match 2 character
                word[i:i + 1], # Try to match 1 character
            ]:
                # Handle 'ъ' and 'Ъ' before 'е', 'ё', 'ю', 'я' and their uppercase versions
                if key.lower() == 'ъ' and i + 1 < len(word) and word[i + 1].lower() in 'еёюя':
                    if i > 0 and word[i - 1].lower() == 'к': # and after 'к'
                        match = 'q̇' if key.islower() else 'Q̇' # match to 'къ'
                    else:
                        match = '' # else skip 'ъ'
                elif key.lower() == 'е': # 'е' can be 'ye' or 'e' depending on the context
                    if i == 0: # if 'е' at the start of the word
                        match = 'ye' if key.islower() else 'Ye'
                    elif i > 0 and word[i - 1].lower() == 'ъ' and (i < 2 or word[i - 2:i].lower() != 'къ'): # and after 'ъ' but not after 'къ'
                        match = 'ye' if key.islower() else 'Ye'
                    else:
                        match = self.transliteration[key] # Regular transliteration for 'е'
                elif key.lower() == 'н' and i == len(word) - 1: # 'н' at the end of the word
                    match = 'ŋ' if key.islower() else 'Ŋ'
                else:
                    match = self.transliteration.get(key, None)

                if match is not None:
                    result += match
                    i += len(key)
                    break

            if match is None:
                result += word[i]
                i += 1
        return result

    def apply_transliteration(self, text):
        text = re.sub(r'\bа\b', 'ə', text) # Replace 'а' with 'ə' if it is a separate word
        text = re.sub(r'\bА\b', 'Ə', text) # Replace 'А' with 'Ə' if it is a separate word
        
        words = text.split()
        transliterated_words = [self.transliterate_word(word) for word in words]
        transliterated_text = ' '.join(transliterated_words)

        # Normalize the result to NFC form to handle composed characters properly
        normalized_text = unicodedata.normalize('NFC', transliterated_text)
        return normalized_text
