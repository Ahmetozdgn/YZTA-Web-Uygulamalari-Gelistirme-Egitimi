import asyncio
# asyncio → Python'un asenkron çalışma kütüphanesi
# Aynı anda birden fazla bekleyen işi yönetir


# ASENKRON FONKSİYON
# async def → bu fonksiyon bekleme (await) içerebilir
async def birinci_fonksiyon():
    print("birinci fonksiyon başladı")

    # await → burada bekler ama program KİLİTLENMEZ
    # asyncio.sleep → non-blocking (başka işler çalışabilir)
    await asyncio.sleep(5)

    print("birinci fonksiyon bitti")
    return 5


async def ikinci_fonksiyon():
    print("ikinci fonksiyon başladı")
    await asyncio.sleep(5)
    print("ikinci fonksiyon bitti")
    return 10 


# ❗ BU NEDEN ÇALIŞMAZ?
# Çünkü async fonksiyonlar NORMAL fonksiyon gibi çağrılamaz
# birinci_fonksiyon() çağrısı sonucu:
# → int değil
# → coroutine objesi döner
#
# await OLMADAN sonucu alamazsın
#
# if __name__ == "__main__":
#     x = birinci_fonksiyon()  # coroutine
#     y = ikinci_fonksiyon()   # coroutine
#     print(x)
#     print(y)


# ASENKRON ANA FONKSİYON
async def main():

    # create_task → coroutine'i EVENT LOOP'a ekler
    # Yani: "bu işi başlat, arka planda çalışsın"
    task1 = asyncio.create_task(birinci_fonksiyon())
    task2 = asyncio.create_task(ikinci_fonksiyon())

    # await → görev bitene kadar BEKLER
    # ama bu bekleme diğer görevleri engellemez
    x = await task1
    y = await task2

    print(x)
    print(y)


# Event loop'u başlatır
# Asenkron programın kalbidir
if __name__ == "__main__":
    asyncio.run(main())



# async def → asenkron fonksiyon tanımı
# await → bekler ama programı kilitlemez
# asyncio.sleep → non-blocking bekleme
# create_task → fonksiyonu aynı anda başlatır
# async fonksiyonlar await olmadan çalışmaz
# asyncio.run → event loop'u başlatır
# Asenkron = beklerken başka iş yapabilmek
