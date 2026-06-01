# Product adında bir class (şablon) tanımlıyoruz
# Bu class bir ürünün hangi bilgilere sahip olacağını belirler
class Product:

    # __init__ metodu (constructor)
    # Class'tan her yeni nesne oluşturulduğunda otomatik olarak çalışır
    # name, price, in_stock parametreleri dışarıdan alınır
    def __init__(self, name: str, price: float, in_stock: bool):

        # self -> oluşturulan nesnenin kendisini temsil eder
        # Aşağıda nesnenin özellikleri atanır
        self.name = name        # Ürünün adı
        self.price = price      # Ürünün fiyatı
        self.in_stock = in_stock  # Ürün stokta mı?


# Bu kontrol, dosyanın nasıl çalıştırıldığını anlamak için kullanılır
# Eğer bu dosya doğrudan çalıştırıldıysa __name__ değeri "__main__" olur
# Başka bir dosyadan import edilirse bu blok çalışmaz
if __name__ == '__main__':

    # Dış bir kaynaktan (API, JSON, dosya vb.) gelmiş gibi düşünülen veri
    # Buradaki tüm değerler STRING (str) tipindedir
    external_data = {
        "name": "Laptop",
        "price": "999.99",
        "in_stock": "True"
    }

    # Product class'ından bir nesne oluşturuluyor
    # Parantez içindeki değerler __init__ metoduna gider
    # NOT: Burada Product ismi hem class hem nesne olarak kullanılmıştır
    # (Çalışır ama gerçek projelerde önerilmez)
    Product = Product(
        name=external_data.get("name"),        # name parametresi
        price=external_data.get("price"),      # price parametresi (string)
        in_stock=external_data.get("in_stock") # in_stock parametresi (string)
    )

    # Oluşturulan nesnenin içindeki alanların tipleri yazdırılıyor
    # Type hint verilmiş olsa bile Python otomatik dönüşüm yapmaz
    print(type(Product.name))     # <class 'str'>
    print(type(Product.price))    # <class 'str'>
    print(type(Product.in_stock)) # <class 'str'>




"""

🧠 KONU ÖZETİ (KISA & NET)

class → Nesne üretmek için kullanılan şablon

__init__ → Nesne oluşturulurken otomatik çalışan fonksiyon

self → O an oluşturulan nesnenin kendisi

Type hint (: str, : float)
→ Zorunlu değildir, sadece bilgilendiricidir

Python otomatik tip dönüşümü yapmaz

__name__ → Dosyanın kimliği

__main__ → Dosya doğrudan çalıştırıldı anlamına gelir

if __name__ == '__main__':
→ Bu kod sadece dosya direkt çalıştırıldığında çalışsın demektir

Dış kaynaktan gelen veriler genelde string olur

Tip güvenliği ve otomatik dönüşüm için Pydantic kullanılır

"""