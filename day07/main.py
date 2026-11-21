import asyncio
import logging

from aiogram import Bot, Dispatcher

from day05.config import get_bot_token
from day07.handlers.todo import todo_router

dp = Dispatcher()


async def main() -> None:
    token = get_bot_token()
    bot = Bot(token=token)
    dp.include_router(todo_router)


    logging.info("Bot is starting")
    await dp.start_polling(bot)
    logging.info("Bot stopped")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )
    asyncio.run(main())

