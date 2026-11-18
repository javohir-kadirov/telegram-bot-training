import logging

from aiogram import F, Router
from aiogram.types import Message


media_router = Router()


@media_router.message(F.photo)
async def photo_handler(message: Message) -> None:
    logging.info("Photo received")
    await message.answer("I received your photo")


@media_router.message(F.document)
async def document_handler(message: Message) -> None:
    logging.info("Document received")
    await message.answer(f"Received document: {message.document.file_name or 'unknown'}")
