import asyncio

async def process_request(username: str, delay: int) -> None:
    print(f"Processing {username}'s request...")

    await asyncio.sleep(delay)

    print(f"{username}'s request processed")

async def main() -> None:
    task = asyncio.create_task(process_request("Ali", 3))
    
    await asyncio.gather(
        process_request("Vali", 1),
        process_request("Sardor", 5)
    )

    await task

    print(f"All requests processed")

asyncio.run(main())