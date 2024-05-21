import os
from pyrogram import Client, filters
from pyrogram.types import Message
from transliterate import ChechenTransliterator
from collections import defaultdict
from datetime import datetime, timedelta
import re

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
    await message.reply("Marşa doġiyla! Please send a word in Cyrillic script to transliterate")

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

    word = message.text.strip()

    if not contains_cyrillic(word):
        await message.reply("Please enter a valid word in Cyrillic script")
        return

    if ' ' in word:
        await message.reply("Beta test yu: cẋa doş beŋ ma yaz de")
    else:
        transliterated_word = transliterator.apply_transliteration(word)
        if transliterated_word.strip():
            await message.reply(transliterated_word)
        else:
            await message.reply("The transliteration resulted in an empty string. Please check your input")

if __name__ == "__main__":
    app.run()
