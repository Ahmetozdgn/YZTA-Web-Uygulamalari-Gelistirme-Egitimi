import asyncio

async def birinci_fonksiyon():
    print("birinci fonksiyon başladı")
    await asyncio.sleep(5) #non blocking delay simülasyon
    print("birinci fonksiyon bitti")
    return 5

async def ikinci_fonksiyon():
    print("ikinci fonksiyon başladı")
    await asyncio.sleep(5) #non blocking delay simülasyon
    print("ikinci fonksiyon bitti")
    return 10 

#! bunu böyle çalsıtırmaz 
# if __name__ == "__main__":
#     x = birinci_fonksiyon()
#     y = ikinci_fonksiyon()

#     print(x)
#     print(y)

async def main():

    task1 = asyncio.create_task(birinci_fonksiyon())
    task2 = asyncio.create_task(ikinci_fonksiyon())

    x = await task1
    y = await task2

    print(x)
    print(y)

if __name__ == "__main__":
    asyncio.run(main())