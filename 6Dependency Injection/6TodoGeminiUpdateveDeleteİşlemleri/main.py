from fastapi import FastAPI, Depends, Path, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from starlette import status

# Kendi dosyalarımızdan modelleri ve veritabanı ayarlarını içeri aktarıyoruz
from models import Base, Todo 
from database import engine, SessionLocal
from typing import Annotated

# FastAPI uygulamasını nesne olarak başlatıyoruz
app = FastAPI()

# Veritabanı tablolarını otomatik olarak oluşturur (Tablolar yoksa)
Base.metadata.create_all(bind=engine)

# Pydantic Modeli: API'ye gönderilecek verilerin formatını ve kurallarını belirler
class TodoRequest(BaseModel):
    title: str = Field(min_length=3) # Başlık en az 3 karakter olmalı
    description: str = Field(min_length=3, max_length=1000) # Açıklama sınırları
    priority: int = Field(gt=0, lt=6) # Öncelik 1 ile 5 arasında olmalı
    complete: bool # Tamamlandı mı? (True/False)

# Veritabanı oturumunu yöneten fonksiyon. Her istekte açılır, iş bitince kapanır.
def get_db():
    db = SessionLocal() # Veritabanı bağlantısı oluşturulur
    try:
        yield db # Veritabanı nesnesi kullanılmak üzere teslim edilir
    finally:
        db.close() # İşlem bittiğinde bağlantı mutlaka kapatılır

# Veritabanı bağımlılığını (Dependency) daha temiz yazmak için Annotated kullanıyoruz
db_dependency = Annotated[Session, Depends(get_db)]

# [GET] Tüm kayıtları okuma endpoint'i
@app.get("/read_all")
async def read_all(db: db_dependency): 
    # db.query(Todo).all() -> Todo tablosundaki tüm verileri getirir
    return db.query(Todo).all()

# [GET] ID numarasına göre tek bir kayıt getirme
@app.get("/get_by_id/{todo_id}", status_code=status.HTTP_200_OK)
async def read_by_id(db: db_dependency, todo_id: int = Path(gt=0)): # ID 0'dan büyük olmalı
    # filter() ile ID eşleşmesi yapılır, .first() ile ilk bulunan kayıt alınır
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo is not None:
        return todo
    # Kayıt bulunamazsa 404 hatası döndürülür
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not foud")

# [POST] Yeni bir Todo oluşturma
@app.post("/create_todo", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todo_request: TodoRequest):
    # Gelen isteği sözlük yapısına çevirip Todo modeline aktarıyoruz
    todo = Todo(**todo_request.dict())
    db.add(todo) # Kaydı veritabanı sırasına ekle
    db.commit() # Değişikliği veritabanına işle (Kaydet)

# [PUT] Mevcut bir kaydı güncelleme
@app.put("/update_todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(db: db_dependency, 
                      todo_request: TodoRequest, 
                      todo_id: int = Path(gt=0)):

    # Önce güncellenecek veri var mı diye kontrol edilir
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

    # Mevcut verinin alanları, kullanıcıdan gelen yeni verilerle değiştirilir
    todo.title = todo_request.title
    todo.description = todo_request.description
    todo.priority = todo_request.priority
    todo.complete = todo_request.complete

    db.add(todo) # Güncellenen nesne tekrar eklenir
    db.commit() # Değişiklikler kaydedilir

# [DELETE] Kayıt silme işlemi
@app.delete("/delete_todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    # Silinmek istenen veri önce bulunur
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    
    # AŞAĞIDAKİ SATIR (Yorum Satırı):
    # db.query(Todo).filter(Todo.id == todo_id).delete() 
    # Bu yöntem, objeyi önce bulmaya gerek kalmadan doğrudan SQL'e silme komutu gönderir. 
    # Daha performanslıdır ancak hata kontrolü (ID var mı yok mu) yapmak zordur.
    
    db.delete(todo) # Bulunan nesneyi siler
    db.commit() # Silme işlemini onaylar

"""
Kullanılan Komutların Kısa Özellikleri
FastAPI(): Web uygulamasının ana iskeletini oluşturur; rotaları ve dökümantasyonu yönetir.

Pydantic (BaseModel): Veri doğrulama yapar. Yanlış tipte (örneğin sayı beklerken metin gelmesi) veri girişini engeller.

db.query(): Veritabanı üzerinde sorgulama başlatır (SELECT işlemi gibi).

.filter(): SQL'deki WHERE şartıdır. Sadece belirli kriterlere uyan verileri seçer.

db.add(): Yeni bir veriyi veya güncellenmiş bir veriyi işlem sırasına (staging) alır.

db.commit(): Yapılan tüm değişiklikleri (ekle, sil, güncelle) veritabanına kalıcı olarak yazar.

db.close(): Veritabanı bağlantısını serbest bırakır, böylece sistem kaynakları boşa harcanmaz.

HTTPException: Hata durumlarında istemciye (tarayıcıya) teknik bir mesaj ve hata kodu gönderir.

Depends: Bir fonksiyonun çalışması için gerekli olan başka bir fonksiyonu (örneğin veritabanı bağlantısı) otomatik olarak çağırır.

"""    