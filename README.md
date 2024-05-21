# Chechen Transliteration Project

## Overview
This project provides tools for transliterating Chechen text from Cyrillic script to Latin script.

## File Structure
- **convert_json_to_tsv.py**: Script to convert a JSON text corpus to a TSV wordlist.
- **corpora_texts.json**: JSON file containing the text corpus.
- **corpora_wordlist.tsv**: TSV file containing the word list.
- **cyrl_latn_dictionary.json**: JSON file with the Cyrillic to Latin transliteration dictionary.
- **docker-compose.yml**: Docker Compose configuration file.
- **Dockerfile**: Dockerfile to build the Docker image.
- **example.env**: Example environment variable configuration file.
- **interactive_transliterate.py**: Script for interactive transliteration.
- **requirements.txt**: List of Python dependencies.
- **telegram_bot.py**: Script for the Telegram bot.
- **transliterate.py**: Transliteration library module.
- **transliterate_tsv.py**: Script to transliterate words in a TSV file.

## Usage

### Converting JSON to TSV
To convert the JSON text corpus to a TSV wordlist, run:
```bash
python convert_json_to_tsv.py
```

### Transliterate TSV
To transliterate words in a TSV file, run:
```bash
python transliterate_tsv.py
```

### Interactive Transliteration
To run the interactive transliteration script, run:
```bash
python interactive_transliterate.py
```

### Telegram Bot
To run the Telegram bot, ensure your environment variables are set correctly in `.env`, and run:
```bash
python telegram_bot.py
```

## Setup
1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the scripts as needed.

## Docker
1. Set up your environment variables in `.env`.

2. Build and run the project using Docker Compose:
    ```bash
    docker compose up -d
    ```
