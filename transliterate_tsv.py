import csv
from transliterate import ChechenTransliterator

def process_tsv(input_file, output_file):
    transliterator = ChechenTransliterator()
    with open(input_file, mode='r', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile, delimiter='\t')
        writer = csv.writer(outfile, delimiter='\t')
        header = next(reader)
        writer.writerow(header)
        
        for row in reader:
            original_word, count = row
            transliterated_word = transliterator.apply_transliteration(original_word)
            writer.writerow([transliterated_word, count])

# Example usage of the script
input_tsv_path = 'corpora_wordlist.tsv'  # Update the input path
output_tsv_path = 'translated_corpora_wordlist.tsv'  # Update the output path

process_tsv(input_tsv_path, output_tsv_path)
