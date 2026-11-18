import asyncio
import logging

from aiogram import Bot, Dispatcher

from day05.config import get_bot_token
from day06.handlers.text import text_router
from day06.handlers.media import media_router
from day06.handlers.fallback import fallback_router

dp = Dispatcher()


async def main() -> None:
    token = get_bot_token()
    bot = Bot(token=token)
    dp.include_routers(text_router, media_router, fallback_router)
    

    logging.info("Bot is starting...")
    await dp.start_polling(bot)
    logging.info("Bot stopped")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )
    asyncio.run(main())