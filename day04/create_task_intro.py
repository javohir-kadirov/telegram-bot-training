import asyncio


async def download_file(filename: str, delay: int) -> None:
    print(f"Downloading: {filename}...")
    
    await asyncio.sleep(delay)
    
    print(f"Download completed: {filename}")

async def main() -> None:
    download = asyncio.create_task(download_file("report.pdf", 3))
    
    print("Checking notifications...")
    
    await asyncio.sleep(1)

    print("Notifications checked.")
    
    await download
    
    print("Program finished")

asyncio.run(main())
