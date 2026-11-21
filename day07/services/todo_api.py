import logging

import asyncio
import aiohttp


async def get_todo(url: str) -> dict:
    timeout = aiohttp.ClientTimeout(total=5)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get(url) as response:
            response.raise_for_status()
            data = await response.json()
            return data


