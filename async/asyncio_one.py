import asyncio


async def async_function(arg):
    print(f"Processing {arg}...")
    await asyncio.sleep(5)
    print(f"Finished processing {arg}.")
    return arg


async def main():
    tasks = [async_function(i) for i in range(10)]
    await asyncio.gather(*tasks)


asyncio.run(main())
