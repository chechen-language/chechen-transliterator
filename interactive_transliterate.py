from transliterate import ChechenTransliterator
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Create an instance of the transliterator
transliterator = ChechenTransliterator()

while True:
    # Get user input
    text = input("Enter text in Cyrillic script: ")

    # Transliterate the input
    transliterated_text = transliterator.apply_transliteration(text)
    print(f"{Fore.GREEN}{transliterated_text}{Style.RESET_ALL}")
