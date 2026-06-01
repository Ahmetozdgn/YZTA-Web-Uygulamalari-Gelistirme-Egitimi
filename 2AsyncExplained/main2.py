import time

def my_func_1():
    print("1. fonksiyon başlıyor")
    time.sleep(5)
    print("1. fonksiyon bitti")
    return 5

def my_func_2():
    print("2. fonksiyon başlıyor")
    time.sleep(5)
    print("2. fonksiyon bitti")
    return 10

if __name__ == "__main__":
    x = my_func_1()
    y = my_func_2()

    print(f"my func 1'in çalışması sonucu x'in değeri {x}")
    print(f"my func 2'nin çalışması sonucu y'in değeri {y}")


# Bu kod senkrondur.
# İki fonksiyon da sırayla çalışır.
# Her biri 5 saniye beklediği için toplam bekleme süresi 10 saniyedir.
# Asenkron yapıya geçildiğinde bu iki fonksiyon aynı anda çalıştırılabilir.