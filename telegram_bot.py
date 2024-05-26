import os
from pyrogram import Client, filters
from pyrogram.types import Message
from transliterate import ChechenTransliterator
from collections import defaultdict
from datetime import datetime, timedelta
import re
import html

API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')
IPV6_ENABLED = os.getenv('IPV6_ENABLED', 'False').lower() in ('true', '1', 't')
RATE_LIMIT_ENABLED = os.getenv('RATE_LIMIT_ENABLED', 'False').lower() in ('true', '1', 't')
MESSAGE_LIMIT = int(os.getenv('MESSAGE_LIMIT', '100'))  # Default to 100 messages per minute

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

app = Client(
    "transliteration_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    ipv6=IPV6_ENABLED
)

transliterator = ChechenTransliterator()
user_message_counts = defaultdict(list)

def contains_cyrillic(text):
    return bool(re.search('[\u0400-\u04FF]', text))

@app.on_message(filters.command("start") & filters.private)
async def start(client, message: Message):
    await message.reply("Marşa doġiyla! Please send text in Cyrillic script to transliterate")

@app.on_message(filters.private)
async def transliterate_message(client, message: Message):
    user_id = message.from_user.id

    if RATE_LIMIT_ENABLED:
        current_time = datetime.now()
        # Filter out messages older than 1 minute
        user_message_counts[user_id] = [msg_time for msg_time in user_message_counts[user_id] if current_time - msg_time < timedelta(minutes=1)]

        if len(user_message_counts[user_id]) >= MESSAGE_LIMIT:
            await message.reply("Rate limit exceeded. Please wait a moment before sending more messages")
            return
        else:
            user_message_counts[user_id].append(current_time)

    text = message.text.strip()

    if not contains_cyrillic(text):
        await message.reply("Please enter valid text in Cyrillic script")
        return

    transliterated_text = transliterator.apply_transliteration(text)

    # Text incorrectly rendered in messages longer than 200 characters containing combining diacritical marks on Android Telegram.
    # To work around this issue, we send the transliterated text as a HTML document if the length exceeds 199 characters.
    if transliterated_text:
        if len(transliterated_text) > 199:
            # Create HTML content
            html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Transliteration Result</title>
    <style>
        body {{
            font-family: "Times New Roman", Times, serif;
            font-size: 18px;
            line-height: 1.4;
        }}
    </style>
</head>
<body>
    <p>{html.escape(transliterated_text)}</p>
</body>
</html>
            """
            
            # Get current date and time
            current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
            file_path = f"transliteration_result_{current_time}.html"
            
            # Write HTML content to a file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            # Send the HTML file as a document
            await message.reply_document(file_path)
            
            # Clean up the file after sending
            os.remove(file_path)
        else:
            # Send as plain text if the length is less than 200 characters
            await message.reply(transliterated_text)
    else:
        await message.reply("The transliteration resulted in an empty string. Please check your input")

if __name__ == "__main__":
    app.run()
