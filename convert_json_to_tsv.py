import json
from collections import Counter
import re
import csv

# Load the JSON data from a file
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Function to clean and split text into words
def extract_words(text):
    text = re.sub(r'[^\w\s]', '', text.lower())  # Normalize and remove non-alphabetic characters
    words = text.split()  # Split by whitespace
    return words

# Count word frequencies in the JSON data
def count_words(json_data):
    word_freq = Counter()
    for item in json_data:
        words = extract_words(item['text'])
        word_freq.update(words)
    return word_freq

# Write the word frequencies to a TSV file
def write_tsv(output_path, word_freq):
    with open(output_path, 'w', newline='', encoding='utf-8') as tsv_file:
        writer = csv.writer(tsv_file, delimiter='\t')
        writer.writerow(['word', 'count'])  # Header row
        for word, count in sorted(word_freq.items(), key=lambda x: -x[1]):
            writer.writerow([word, count])

# Main function to handle the process
def main():
    # Prompt for file paths
    json_file_path = input("Enter the path to the JSON file: ")
    tsv_file_path = input("Enter the path to the output TSV file: ")

    # Process the files
    json_data = load_json(json_file_path)
    word_freq = count_words(json_data)
    write_tsv(tsv_file_path, word_freq)

# Run the main function
main()
