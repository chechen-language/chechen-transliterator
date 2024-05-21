from transliterate import ChechenTransliterator

# Create an instance of the transliterator
transliterator = ChechenTransliterator()

while True:
    # Get user input
    word = input("Enter a word in Cyrillic script: ")

    # Check if input contains only one word
    if ' ' in word.strip():
        print("Please enter only one word.")
    else:
        # Transliterate the input
        transliterated_word = transliterator.apply_transliteration(word.strip())
        print(f"Transliterated word: {transliterated_word}")
