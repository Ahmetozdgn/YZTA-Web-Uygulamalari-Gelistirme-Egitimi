# ==============================================================================
# ANA UYGULAMA NOTU:
# 1. FastAPI: Yazdığın kodların internetten erişilmesini sağlayan çerçevedir.
# 2. Base.metadata: Tüm tabloların ve sütunların listesini tutan kayıt defteridir.
# 3. create_all: Bu defteri okuyarak tabloları fiziksel olarak oluşturur.
# ==============================================================================

from fastapi import FastAPI # API çerçevesi
from models import Base # Tablo modelleri
from database import engine # Veritabanı motoru

# FastAPI uygulamasını başlatıyoruz
app = FastAPI()

# Kayıt defterindeki (metadata) tabloları veritabanında fiziksel olarak oluşturur
Base.metadata.create_all(bind=engine)