import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "22727464"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "f0e595a263c89aa17f6571b8af296ced")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7983413191:AAGMbDb9bqTTT68pMjjRd0Q4Y6y4UCyHITo")

OWNER_ID = int(os.environ.get("OWNER_ID", "887699812"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "887699812").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://makwanaram:Hackthis008@cluster0.w69onvk.mongodb.net/?retryWrites=true&w=majority")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002807057819"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "-1002807057819")  # Optional here you'll get all logs
