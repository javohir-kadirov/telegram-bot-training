import logging
import asyncio
import aiohttp

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from day07.services.todo_api import get_todo


todo_router = Router()


@todo_router.message(Command("todo"))
async def todo_handler(message: Message) -> None:
    logging.info("Todo command received")
    
    try:
        todo = await get_todo("https://jsonplaceholder.typicode.com/todos/9999")
        await message.answer(f"📋 Task: {todo['title']} \n ✅ Done: {todo['completed']}", parse_mode=None)

    except asyncio.TimeoutError:
        logging.exception("Request time out received")
        await message.answer("Your request timed out")        

    except aiohttp.ClientResponseError as error:
        logging.exception("Response error received")
        await message.answer(f"Response error: {error.status}")

    except aiohttp.ClientConnectionError:
        logging.exception("Connection error received")
        await message.answer("You have connection error")

    
