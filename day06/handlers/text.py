import logging

from aiogram import F, Router
from aiogram.types import Message


text_router = Router()


@text_router.message(F.text.lower() == "hello")
async def hello_handler(message: Message) -> None:
    logging.info("Hello message received")
    await message.answer("Hello! How are you?")


@text_router.message(F.text.lower() == "price")
async def price_handler(message: Message) -> None:
    logging.info("Price requested")
    await message.answer("Our service costs $100")
