import os
from dotenv import load_dotenv

load_dotenv('.env')

TELEGRAM_BOT_API_KEY = os.environ.get("TELEGRAM_BOT_API_KEY")
OPEN_AI_API_KEY = os.environ.get("OPENAI_API_KEY")
