# Bu kod SENKRON çalışır
# Yani satırlar yukarıdan aşağıya, sırayla çalışır

x = 5
y = 4
print(x + y)   # 5 + 4 = 9, bu satır bitmeden alttaki satıra geçilmez


# Basit bir liste tanımlıyoruz
benim_listem = [10, 20, 30, 40, 50, 60]


# Bu blok dosya direkt çalıştırıldığında devreye girer
# (import edilirse çalışmaz)
if __name__ == '__main__':

    print("loop başlıyor")

    # for döngüsü SENKRON çalışır
    # Bir sayı yazdırılmadan diğeri başlamaz
    for num in benim_listem:
        print(num)

    print("loop bitiyor")
