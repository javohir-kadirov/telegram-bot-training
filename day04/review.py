import asyncio


async def fetch_data(name: str, delay: int) -> None:
    print(f"{name} operation started...")
    
    await asyncio.sleep(delay)

    print(f"{name} operation finished.")


async def main() -> None:
    operation = asyncio.create_task(fetch_data("Database", 4))


    await asyncio.gather(
        fetch_data("API", 2),
        fetch_data("Cache", 1),
    )
    await operation

    print("All data loaded")

asyncio.run(main())