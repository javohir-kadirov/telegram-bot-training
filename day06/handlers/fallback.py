import logging

from aiogram import Router
from aiogram.types import Message


fallback_router = Router()


@fallback_router.message()
async def fallback_handler(message: Message) -> None:
    logging.info("Unknown message received")
    await message.answer("Sorry, I don't understand this message.")