import unittest
from transliterate import ChechenTransliterator

class TestChechenTransliterator(unittest.TestCase):
    def setUp(self):
        self.transliterator = ChechenTransliterator()

    def test_transliterate_word(self):
        # Test transliteration of individual words
        self.assertEqual(self.transliterator.transliterate_word("халкъе"), "xalq̇e")
        self.assertEqual(self.transliterator.transliterate_word("елла"), "yella")
        self.assertEqual(self.transliterator.transliterate_word("шелъелча"), "şelyelça")
        self.assertEqual(self.transliterator.transliterate_word("дечиган"), "deçigaŋ")
        self.assertEqual(self.transliterator.transliterate_word("чекхъели"), "çeqyeli")
        self.assertEqual(self.transliterator.transliterate_word("къоьрта"), "q̇örta")
        self.assertEqual(self.transliterator.transliterate_word("цхьаъ"), "cẋaə")

    def test_transliterate_text(self):
        # Test transliteration of entire text
        text = "Сан Даймохк бац хьуна абата тӏера, виначу юьртара болалац и. Сан Даймохк мотт сецна бӏешерийн кхера, сан Даймохк тарраш тӏехь лардина сий. Ца оьшуш хӏумма а тардина кхолла, ма цӏена бакъ а ду-кх заманан аз. Сан Даймохк ӏаьршашка кхевдина хӏоллам, сан Даймохк аренца къух даьлла барз."
        expected = "Saŋ Daymoxk bac ẋuna abata ṫera, vinaçu yürtara bolalac i. Saŋ Daymoxk mott secna bjeşeriyŋ qera, saŋ Daymoxk tarraş ṫeẋ lardina siy. Ca öşuş humma ə tardina qolla, ma ċena baq̇ ə du-q zamanaŋ az. Saŋ Daymoxk järşaşka qevdina hollam, saŋ Daymoxk arenca q̇ux dälla barz."
        self.assertEqual(self.transliterator.apply_transliteration(text), expected)

    def test_transliterate_lower_single_a(self):
        # Test transliteration of a lower single 'а' character
        text = "Мелхо а, шуна цхьанна а тхайх бала ца бархьама, дийнахь а, буса а, къа а хьоьгуш, болх бора оха"
        expected = "Melxo ə, şuna cẋanna ə txayx bala ca barẋama, diynaẋ ə, busa ə, q̇a ə ẋöguş, bolx bora oxa"
        self.assertEqual(self.transliterator.apply_transliteration(text), expected)
    
    def test_transliterate_upper_single_a(self):
        # Test transliteration of a upper single 'А' character
        text = "МЕЛХО А, ШУНА ЦХЬАННА А ТХАЙХ БАЛА ЦА БАРХЬАМА, ДИЙНАХЬ А, БУСА А, КЪА А ХЬОЬГУШ, БОЛХ БОРА ОХА"
        expected = "MELXO Ə, ŞUNA CẊANNA Ə TXAYX BALA CA BARẊAMA, DIYNAẊ Ə, BUSA Ə, Q̇A Ə ẊÖGUŞ, BOLX BORA OXA"
        self.assertEqual(self.transliterator.apply_transliteration(text), expected)

    def test_transliterate_mixed_case_1(self):
        # Test transliteration of mixed case "ъ" and "е" characters
        text = "къегина Къегина кЪегина КЪегина къЕгина КъЕгина кЪЕгина КЪЕгина КЪЕГИНА Къегина"
        expected = "q̇egina Q̇egina q̇egina Q̇egina q̇Egina Q̇Egina q̇Egina Q̇Egina Q̇EGINA Q̇egina"
        self.assertEqual(self.transliterator.apply_transliteration(text), expected)

        # Test transliteration of mixed case "ъ" and "е" characters
    def test_transliterate_mixed_case_2(self):
        text = "чекхъели чекХъели чекхЪели чекХЪели чекхъЕли чекХъЕли чекхЪЕли чекХЪЕли ЧЕКХЪЕЛИ Чекхъели"
        expected = "çeqyeli çeqyeli çeqyeli çeqyeli çeqYeli çeqYeli çeqYeli çeqYeli ÇEQYELI Çeqyeli"
        self.assertEqual(self.transliterator.apply_transliteration(text), expected)

    def test_transliterate_e(self):
        text = "еара еАра еарА еАрА ЕАра ЕАрА ЕАРА Еара"
        expected = "yeara yeAra yearA yeArA YEAra YEArA YEARA Yeara"
        self.assertEqual(self.transliterator.apply_transliteration(text), expected)

if __name__ == '__main__':
    unittest.main()
