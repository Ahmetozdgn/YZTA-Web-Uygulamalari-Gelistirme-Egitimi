from fastapi import FastAPI, Body, Path, Query, HTTPException
from typing import Optional
from pydantic import BaseModel, Field
from starlette import status  

# FastAPI uygulamasını başlatıyoruz
app = FastAPI()

# Veritabanı modelleri için temel Python sınıfı
class Course:
    instructor: str
    rating: int
    published_date: int

    def __init__(self, id: int, title: str, instructor: str, rating: int, published_date: int):
        self.id = id
        self.title = title
        self.instructor = instructor
        self.rating = rating
        self.published_date = published_date

# Kullanıcıdan veri alırken (POST/PUT) yapılacak doğrulamaları içeren Pydantic Modeli
class CourseRequest(BaseModel):
    # Optional: ID gönderilmeyebilir (otomatik atanacak), Field: Swagger üzerinde açıklama ekler
    id: Optional[int] = Field(description="The id of the course, optional", default=None)
    # Başlık en az 3, en fazla 100 karakter olmalı
    title: str = Field(min_length=3, max_length=100)
    instructor: str = Field(min_length=3)
    # Rating 1 ile 5 arasında olmalı (gt: greater than, lt: less than)
    rating: int = Field(gt=0, lt=6)
    # Tarih 2020 ile 2100 arasında olmalı (gte: greater than equal)
    published_date: int = Field(gte=2020, lte=2100)

    # Swagger UI (docs) üzerinde görünecek örnek veri şablonu
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "course title",
                "instructor": "atil samancioglu",
                "rating": 5,
                "published_date": 2020
            }
        }
    }

# Geçici veritabanımız (Bellek üzerinde tutulan liste)
courses_db = [
    Course(id=1, title="Python", instructor="Atil", rating=5, published_date=2029),
    Course(id=2, title="Kotlin", instructor="Ahmet", rating=5, published_date=2026),
    Course(id=3, title="Jenkins", instructor="Atil", rating=5, published_date=2023),
    Course(id=4, title="Kubernetes", instructor="Zeynep", rating=2, published_date=2030),
    Course(id=5, title="Machine Learning", instructor="Fatma", rating=3, published_date=2036),
    Course(id=6, title="Deep Learning", instructor="Atlas", rating=1, published_date=2039)
]

# Tüm kursları listeleyen GET endpoint'i
@app.get(path="/courses", status_code=status.HTTP_200_OK)
async def get_all_courses():
    return courses_db

# Belirli bir ID'ye göre kurs getiren endpoint. Path(gt=0) ile ID'nin 0'dan büyük olması zorunlu tutulur.
@app.get("/courses/{course_id}", status_code=status.HTTP_200_OK)
async def get_course(course_id: int = Path(gt=0)):
    for course in courses_db:
        if course.id == course_id:
            return course
    # Kurs bulunamazsa 404 hatası fırlatır
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

# Query Parameter kullanarak Rating'e göre filtreleme yapan endpoint
@app.get("/courses/", status_code=status.HTTP_200_OK)
async def get_courses_by_rating(course_rating: int = Query(gt=0, lt=6)):
    courses_to_return = []
    for course in courses_db:
        if course.rating == course_rating:
            courses_to_return.append(course)
    return courses_to_return

# Yayın tarihine göre filtreleme yapan endpoint
@app.get("/courses/publish/", status_code=status.HTTP_200_OK)
async def get_courses_by_publish_date(publish_date: int = Query(gt=2005, lt=2040)):
    courses_to_return = []
    for course in courses_db:
        if course.published_date == publish_date:
            courses_to_return.append(course)
    return courses_to_return

# Yeni kurs oluşturan POST endpoint'i
@app.post("/create-course", status_code=status.HTTP_201_CREATED)
async def create_course(course_request: CourseRequest):
    # model_dump() ile Pydantic objesini sözlüğe çevirip Course sınıfına açarak (** unpack) gönderiyoruz
    new_course = Course(**course_request.model_dump())
    # Yeni ID atamasını yapıp listeye ekliyoruz
    courses_db.append(find_course_id(new_course))

# Liste boşsa ID'yi 1 yapar, değilse son elemanın ID'sine 1 ekler
def find_course_id(course: Course):
    course.id = 1 if len(courses_db) == 0 else courses_db[-1].id + 1
    return course

# Mevcut bir kursu güncelleyen PUT endpoint'i (204 No Content döner)
@app.put("/courses/update_course", status_code=status.HTTP_204_NO_CONTENT)
async def update_course(course_request: CourseRequest):
    course_updated = False
    for i in range(len(courses_db)):
        # Gelen istekteki ID ile listedeki ID eşleşirse veriyi güncelle
        if courses_db[i].id == course_request.id:
            courses_db[i] = course_request
            course_updated = True
            break # Eşleşme bulundu, döngüden çık

    if not course_updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

# Kurs silme işlemi yapan DELETE endpoint'i
@app.delete("/courses/delete/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(course_id: int = Path(gt=0)):
    course_deleted = False
    for i in range(len(courses_db)):
        if courses_db[i].id == course_id:
            # pop(i) ile belirtilen indeksteki elemanı listeden kaldırır
            courses_db.pop(i)
            course_deleted = True
            break
            
    if not course_deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    

"""
Önemli Not:
Kodun en sonunda raise HTTPException(...) satırının sonundaki virgül (,) ve sonrasındaki açıklama kısmını temizledim; çünkü Python'da bu şekilde kullanım sözdizimi hatası (SyntaxError) verebilirdi.

Bu API'yi çalıştırmak için terminale uvicorn main:app --reload yazman yeterli olacaktır. Başka bir ekleme yapmamı ister misin?

"""


# ==========================================
# FASTAPI KOMUTLARI ÖZETİ
# ==========================================

# app = FastAPI(): Uygulamanın ana gövdesini oluşturur.
# @app.get(): Veri çekmek/okumak için kullanılan dekoratör.
# @app.post(): Yeni bir veri oluşturmak/kaydetmek için kullanılan dekoratör.
# @app.put(): Mevcut bir veriyi tamamen güncellemek için kullanılır.
# @app.delete(): Bir veriyi silmek için kullanılır.

# ==========================================
# PARAMETRE VE DOĞRULAMA (VALIDATION)
# ==========================================

# Path(): URL içindeki yolu doğrular. Örn: /courses/{id} kısmındaki id.
#   - gt=0: (Greater Than) 0'dan büyük olmalı.
#   - lt=6: (Less Than) 6'dan küçük olmalı.

# Query(): URL sonundaki sorgu parametrelerini doğrular. Örn: ?rating=5.
#   - gte=2020: (Greater Than Equal) 2020'ye eşit veya büyük olmalı.
#   - lte=2100: (Less Than Equal) 2100'e eşit veya küçük olmalı.

# Body(): İsteğin gövdesinde (JSON) veri göndermek için kullanılır.

# ==========================================
# PYDANTIC VE MODELLEME
# ==========================================

# BaseModel: Veri şablonu oluşturmak için miras alınan ana sınıf.
# Field(): Model içindeki değişkenlere özel kısıtlamalar ve açıklamalar ekler.
#   - min_length / max_length: Karakter sınırı koyar.
# Optional: Bir alanın gönderilmesinin zorunlu olmadığını belirtir (None olabilir).
# model_dump(): Pydantic nesnesini standart bir Python sözlüğüne (dict) dönüştürür.
# model_config / json_schema_extra: Swagger belgelerinde görünecek örnek verileri tanımlar.

# ==========================================
# DURUM KODLARI VE HATA YÖNETİMİ
# ==========================================

# status.HTTP_200_OK: İşlem başarılı (Varsayılan).
# status.HTTP_201_CREATED: Yeni kayıt başarıyla oluşturuldu.
# status.HTTP_204_NO_CONTENT: İşlem başarılı ama geri dönecek veri yok (Update/Delete için ideal).
# status.HTTP_404_NOT_FOUND: Aranan kaynak bulunamadı.

# HTTPException: Belirli bir hata durumunda (örn: ID bulunamadı) istemciye hata fırlatır.