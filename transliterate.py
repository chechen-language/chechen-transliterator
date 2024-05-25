import json
import re

class ChechenTransliterator:
    def __init__(self, filename='cyrl_latn_dictionary.json'):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.transliteration = data['cyrl_latn']

    def transliterate_word(self, word):
        # word = word.lower()
        result = ''
        i = 0
        while i < len(word):
            match = None
            for key in [
                word[i:i + 3], # Try to match 3 character
                word[i:i + 2], # Try to match 2 character
                word[i:i + 1], # Try to match 1 character
            ]:
                if key in self.transliteration:
                    if key == 'ъ' and i + 1 < len(word) and word[i + 1] in 'еёюя': # if 'ъ' before 'е', 'ё', 'ю', 'я'
                        if i > 0 and word[i - 1] == 'к': # and after 'к'
                            match = 'q̇' # match to 'къ'
                        else:
                            match = '' # else skip 'ъ'
                    elif key == 'е': # 'е' can be 'ye' or 'e' depending on the context
                        if i == 0:
                            match = 'ye' # if 'е' at the start of the word
                        elif i > 0:
                            if word[i - 1] == 'ъ' and (i < 2 or word[i - 2:i] != 'къ'):
                                match = 'ye' # 'е' following 'ъ' that does not follow 'къ'
                            else:
                                match = self.transliteration[key]  # Regular transliteration for 'е'
                        else:
                            match = self.transliteration[key]
                    elif key == 'н' and i == len(word) - 1:
                        match = 'ŋ'  # 'н' at the end of the word
                    else:
                        match = self.transliteration[key]
                    if match is not None:
                        result += match
                        i += len(key)
                        break
            if match is None:
                result += word[i]  # Add the character as is if no match was found
                i += 1  # Move to next character
        return result

    def apply_transliteration(self, text):
        words = text.split()
        transliterated_words = [self.transliterate_word(word) for word in words]
        return ' '.join(transliterated_words)
