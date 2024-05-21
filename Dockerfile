FROM python:3.9-slim

WORKDIR /app

COPY . /app

# Install dependencies
RUN python3 -m pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python", "./telegram_bot.py" ]