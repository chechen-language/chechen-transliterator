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

    def test_transliterate_single_a(self):
        # Test transliteration of a single 'а' character
        text = "Хьо а, леха а лоьхуш"
        expected = "Ẋo ə, lexa ə löxuş"
        self.assertEqual(self.transliterator.apply_transliteration(text), expected)

if __name__ == '__main__':
    unittest.main()
