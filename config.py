import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ALLOWED_USER_ID = os.getenv("ALLOWED_USER_ID")
if ALLOWED_USER_ID:
    ALLOWED_USER_ID = int(ALLOWED_USER_ID)
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")

if not TELEGRAM_BOT_TOKEN or not ALLOWED_USER_ID:
    print("Warning: Missing TELEGRAM_BOT_TOKEN or ALLOWED_USER_ID")
