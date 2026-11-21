import asyncio
import aiohttp


async def fetch_todo() -> None:
    timeout = aiohttp.ClientTimeout(total=5)
    async with aiohttp.ClientSession(timeout=timeout) as session:
            try:
                async with session.get("https://jsonplaceholder.typicode.com/todos/999999") as response:
                    response.raise_for_status()
                    data = await response.json()
                    print(data["title"])

            except aiohttp.ClientResponseError as res_error:
                print(f"HTTP error: {res_error.status}")

            except asyncio.TimeoutError:
                print("Request timed out")

            except aiohttp.ClientConnectorError:
                print("Connection error")
            

if __name__ == "__main__":
    asyncio.run(fetch_todo())