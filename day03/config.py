import os
from dotenv import load_dotenv


def load_config() -> None:
    load_dotenv()

    bot_token = os.getenv("BOT_TOKEN")
    if not bot_token:
        raise ValueError("BOT_TOKEN is missing")
    admin_id = os.getenv("ADMIN_ID")

    if not admin_id:
        raise ValueError("ADMIN_ID is missing")
    
    try:
        admin_id = int(admin_id)
    except ValueError:
        raise ValueError("ADMIN_ID must be an integer")

    print("Configuration loaded")

load_config()