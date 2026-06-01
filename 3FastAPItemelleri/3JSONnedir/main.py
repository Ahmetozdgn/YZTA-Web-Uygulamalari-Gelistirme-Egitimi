# JSON = JavaScript Object Notation
# İnternet üzerinden veri taşımak için kullanılan bir formattır.
# İnsan okuyabilir, makineler kolayca işler.

from fastapi import FastAPI

# Web uygulamamızı oluşturuyoruz
app = FastAPI()


# "/hello" adresine GET isteği gelirse bu fonksiyon çalışır
@app.get("/hello")
async def hello_world():

    # Burada bir Python sözlüğü (dict) döndürüyoruz
    # {"message": "Hello world"} bir dict'tir

    # FastAPI bu dict'i otomatik olarak JSON formatına çevirir
    # ve tarayıcıya JSON olarak gönderir

    return {"message": "Hello world"}


# Tarayıcıda görünen şey aslında JSON'dur:
# {
#   "message": "Hello world"
# }

# JSON yapısı:
# {
#   "anahtar": "değer"
# }

# Yani:
# message  → anahtar (key)
# Hello world → değer (value)

# JSON -> Javascript Object Notation


# UYGULAMAYI ÇALIŞTIRMA
# Terminale şunu yazıyoruz:
# uvicorn main:app --reload
