import asyncio
import aiohttp


async def fetch_todo() -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get("https://jsonplaceholder.typicode.com/todos/1") as response:
            print(response.status)
            data = await response.json()
            print(data["title"])
            print(data["completed"])


if __name__ == "__main__":
    asyncio.run(fetch_todo())