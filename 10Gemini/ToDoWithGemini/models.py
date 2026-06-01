from database import Base # database.py'deki temel yapıyı (declarative_base) çağırır
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

# Todo tablosu tanımı
class Todo(Base):
    __tablename__ = 'todos' # Veritabanındaki gerçek tablo ismi

    # Sütunlar ve Özellikleri
    id = Column(Integer, primary_key=True, index=True) # Sayısal kimlik (ID)
    title = Column(String)                             # Başlık metni
    description = Column(String)                       # Açıklama metni
    priority = Column(Integer)                         # Öncelik sayısı
    complete = Column(Boolean, default=False)          # Bitti/Bitmedi durumu
    owner_id = Column(Integer, ForeignKey('users.id'))

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)
    phone_number = Column(String)