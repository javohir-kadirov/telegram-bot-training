import logging

from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message


router = Router()

@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    logging.info("Start command received")
    await message.answer("Welcome to my first Telegram bot!")


@router.message(Command("help"))
async def help_handler(message: Message) -> None:
    logging.info("Help command received")
    help_text = (
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show available commands"
    )
    await message.answer(help_text)