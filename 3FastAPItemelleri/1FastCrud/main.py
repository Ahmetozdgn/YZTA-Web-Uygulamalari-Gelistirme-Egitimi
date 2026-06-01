# FastAPI kütüphanesinden FastAPI sınıfını içe aktarıyoruz
from fastapi import FastAPI


# Bir web uygulaması oluşturuyoruz
# Bu "app" bizim internet üzerinden çalışacak programımız
app = FastAPI()


# "/" ana sayfa demektir
# Tarayıcıdan http://127.0.0.1:8000/ yazılırsa
# aşağıdaki fonksiyon çalışır
@app.get("/")


# async demek:
# Bu fonksiyon bekleme yaparken (örneğin veri beklerken)
# sistemi durdurmaz, başka işleri de yapabilir.
# Yani daha verimli çalışır.
async def hello_world():

    # Tarayıcıya bir mesaj gönderiyoruz
    # FastAPI bunu otomatik olarak JSON formatına çevirir
    return {"message": "Hello World"}



# ================================
# UYGULAMAYI ÇALIŞTIRMA
# ================================

# Terminale şunu yazıyoruz:

# uvicorn main:app --reload

# Anlamı:

# uvicorn  → uygulamayı çalıştıran program
# main     → dosyanın adı (main.py olmalı)
# app      → yukarıda oluşturduğumuz uygulama adı
# --reload → kod değişince otomatik yeniler (geliştirme için iyi)

# Sonra tarayıcıya şunu yaz:
# http://127.0.0.1:8000/

# Ekranda şu görünür:
# {"message": "Hello World"}