import os
from dotenv import load_dotenv

def get_bot_token() -> str:
    load_dotenv()
    bot_token = os.getenv("BOT_TOKEN")

    if not bot_token:
        raise ValueError("BOT_TOKEN is missing")
    return bot_token