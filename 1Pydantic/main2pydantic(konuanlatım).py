# Pydantic'in temel sınıfını içe aktarıyoruz
# BaseModel → veri doğrulama ve otomatik tip dönüşümü yapar
from pydantic import BaseModel


# Product için bir veri modeli tanımlıyoruz
# Bu sınıf normal class gibi görünür ama Pydantic tarafından yönetilir
class productpydantic(BaseModel):
    name: str        # ürün adı → string olmalı
    price: float     # fiyat → float olmalı
    in_stock: bool   # stok durumu → True / False olmalı


# Bu blok sadece dosya direkt çalıştırılırsa çalışır
# (başka bir dosyadan import edilirse çalışmaz)
if __name__ == '__main__':

    # Dışarıdan gelen (API, form, JSON vb.) ham veriyi temsil eder
    # Dikkat: price ve in_stock string olarak geliyor
    external_data = {
        "name": "Laptop",
        "price": "999.99",
        "in_stock": "True"
    }

    # Pydantic modeli oluşturuluyor
    # Burada BaseModel:
    # - string "999.99" → float 999.99 yapar
    # - string "True"   → bool True yapar
    Product = productpydantic(
        name=external_data.get("name"),
        price=external_data.get("price"),
        in_stock=external_data.get("in_stock")
    )

    # Alanların gerçek tiplerini yazdırıyoruz
    # Pydantic dönüşüm yapabildi mi kontrol ediyoruz
    print(type(Product.name))       # <class 'str'>
    print(type(Product.price))      # <class 'float'>
    print(type(Product.in_stock))   # <class 'bool'>







""""
GÜNCEL KISA ÖZET (Net & Akılda Kalıcı)

from pydantic import BaseModel
→ Pydantic’in çekirdeğini içeri alır
→ Normal class’a veri doğrulama + tip dönüşümü yeteneği kazandırır

class productpydantic(BaseModel):
→ Bu sınıf BaseModel’den miras alır
→ Yani:

type hint’leri (str, float, bool) gerçekten zorunlu olur

gelen veriler otomatik kontrol edilir

BaseModel ile bağlantı nasıl kuruldu?
→ productpydantic(BaseModel) yazarak
→ Pydantic’e şunu demiş olduk:
“Bu class’ı sen yönet, ben güvenli veri istiyorum.”

"999.99" → float 999.99

"True" → bool True
(Pydantic makul dönüşümleri yapar)

Saçma veri gelirse ("asdf", "laptop")
→ ❌ True/False uydurmaz
→ 💥 ValidationError fırlatır

__name__ == '__main__'
→ Kod sadece dosya direkt çalıştırılırsa çalışır
→ import edilirse çalışmaz (kontrollü çalışma)

"""