# ==============================================================================
# MODELLER NOTU:
# Bu dosya veritabanı şemasını (tabloları) belirler. 
# SQLAlchemy kütüphanesi buradaki sınıfları SQL tablolarına dönüştürür.
# ==============================================================================

from database import Base # database.py'deki temel yapıyı (declarative_base) çağırır
from sqlalchemy import Column, Integer, String, Boolean # Veri tipleri kütüphaneleri

# Todo tablosu tanımı
class Todo(Base):
    __tablename__ = 'todos' # Veritabanındaki gerçek tablo ismi

    # Sütunlar ve Özellikleri
    id = Column(Integer, primary_key=True, index=True) # Sayısal kimlik (ID)
    title = Column(String)                             # Başlık metni
    description = Column(String)                       # Açıklama metni
    priority = Column(Integer)                         # Öncelik sayısı
    complete = Column(Boolean, default=False)          # Bitti/Bitmedi durumu