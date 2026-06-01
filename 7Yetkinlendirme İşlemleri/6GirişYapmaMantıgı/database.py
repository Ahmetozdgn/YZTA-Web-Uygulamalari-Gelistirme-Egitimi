# ==============================================================================
# GÜNCEL PROJE NOTU:
# 1. create_engine: Veritabanı dosyasını açan ve veri trafiğini yöneten tesisatçıdır.
# 2. declarative_base: Python sınıfını "Veritabanı tablosudur" diye işaretleyen temel yapıdır.
# 3. sessionmaker: Veri yazmak/okumak için açılan "oturumları" üreten fabrikadır.
# 4. Modellerde değişiklik yaparsan, yansıması için .db dosyasını silip yeniden çalıştır.
# ==============================================================================

from sqlalchemy import create_engine # Veritabanı motorunu kuran kütüphane
from sqlalchemy.ext.declarative import declarative_base # Temel model sınıfı oluşturucu
from sqlalchemy.orm import sessionmaker # Oturum yönetici kütüphane

# SQLite veritabanı dosya yolu
SQLALCHEMY_DATABASE_URL = "sqlite:///./todoai_app.db"

# Veritabanı bağlantı motoru (Tesisatçı)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Veritabanı oturum fabrikası (Gişe Memuru)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Tüm tabloların türetileceği ana sınıf
Base = declarative_base()