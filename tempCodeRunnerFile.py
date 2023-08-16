import asyncio


async def f1():
    print("f1 started")
    await asyncio.sleep(1)
    print("f1 finished")


async def f2():
    print("f2 started")
    await asyncio.sleep(2)
    print("f2 finished")


async def main():
    await asyncio.gather(f1(), f2())

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
