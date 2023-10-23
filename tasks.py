import asyncio
import time
import aiohttp


async def perform_get_request(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                print(f"Done: {url}")

    except Exception as e:
        print(f"Error: {url}")
        print(str(e))


async def main():
    urls = ['https://www.google.com']*100

    start_time = time.time()

    tasks = []

    for url in urls:
        task = asyncio.create_task(perform_get_request(url))
        tasks.append(task)

    await asyncio.gather(*tasks)

    end_time = time.time()

    total_execution_time = end_time - start_time
    print(f"Time is: {total_execution_time:.2f} sec")


if __name__ == "__main__":
    asyncio.run(main())
