import asyncio


async def send_message(username: str, delay: int) -> None:
    print(f"Sending message to {username}...")
    await asyncio.sleep(delay)
    print(f"Message sent to {username}")

async def main() -> None:
    
    await asyncio.gather(
        send_message("Ali", 2),
        send_message("Vali", 1),
        send_message("Sardor", 3)
    )
    
asyncio.run(main())