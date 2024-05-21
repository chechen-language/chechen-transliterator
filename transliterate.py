import json

class ChechenTransliterator:
    # def __init__(self):
    #     self.transliteration = {
    #         # Add your transliteration mappings here
    #         'а': 'a', 'аь': 'ä', 'б': 'b', 'в': 'v', 'г': 'g', 'гӏ': 'ġ', 'ц': 'c', 'цӏ': 'ċ', 'д': 'd',
    #         'е': 'e', 'ё': 'ö', 'ж': 'ƶ', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'кх': 'q', 'къ': 'q̇',
    #         'кӏ': 'k̇', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'оь': 'ö', 'п': 'p', 'пӏ': 'ṗ', 'р': 'r',
    #         'с': 's', 'т': 't', 'тӏ': 'ṫ', 'у': 'u', 'уь': 'ü', 'ф': 'f', 'х': 'x', 'хь': 'ẋ', 'хӏ': 'h',
    #         'ч': 'ç', 'чӏ': 'ç̇', 'ш': 'ş', 'щ': 'ş', 'ъ': 'ə', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
    #         'ӏ': 'j', 'Ӏ': 'J', 'ккх': 'qq', 'ккъ': 'q̇q̇', 'юь': 'yü', 'яь': 'yä'
    #     }

    def __init__(self, filename='cyrl_latn_dictionary.json'):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.transliteration = data['cyrl_latn']

    def apply_transliteration(self, word):
        result = ""
        i = 0
        while i < len(word):
            match = None
            for key in [word[i:i+3], word[i:i+2], word[i:i+1]]:
                if key in self.transliteration:
                    if key == 'ъ' and i + 1 < len(word) and word[i + 1] in 'еёюя':
                        if i > 0 and word[i - 1] == 'к':
                            match = 'q̇'
                        else:
                            match = ''  # 'ъ' is null before these characters unless after 'к'
                    elif key == 'е':
                        if i == 0:
                            match = 'ye'  # 'е' at the start of the word
                        elif i > 0:
                            if word[i - 1] == 'ъ' and (i < 2 or word[i - 2:i] != 'къ'):
                                match = 'ye'  # 'е' following 'ъ' that does not follow 'къ'
                            else:
                                match = self.transliteration[key]  # Regular transliteration for 'е'
                    elif key == 'н' and i == len(word) - 1:
                        match = 'ŋ'  # 'н' at the end of the word
                    else:
                        match = self.transliteration[key]
                    if match:
                        result += match
                        i += len(key)
                        break
            if not match:
                i += 1  # Move to next character if no match was found
        return result
