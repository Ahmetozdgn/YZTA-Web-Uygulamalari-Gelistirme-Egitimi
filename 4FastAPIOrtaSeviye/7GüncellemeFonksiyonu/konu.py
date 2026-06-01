from fastapi import FastAPI, Body, Path, Query, HTTPException
from typing import Optional
from pydantic import BaseModel, Field
from starlette import status  

app = FastAPI()

# --- VERİ MODELİ (Sınıf Yapısı) ---
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

# --- PYDANTIC MODELİ (İstek Doğrulama Şeması) ---
class CourseRequest(BaseModel):
    # Optional: ID gönderilmeyebilir (Yeni kayıt açılırken sistem atar).
    id: Optional[int] = Field(description="The id of the course, optional", default=None)
    # Field kısıtlamaları: Başlık 3-100 karakter arası, eğitmen min 3 karakter vb.
    title: str = Field(min_length=3, max_length=100)
    instructor: str = Field(min_length=3)
    rating: int = Field(gt=0, lt=6) # 1 ile 5 arası
    published_date: int = Field(gte=2020, lte=2100) # 2020 ve sonrası

    # Dokümantasyonda (Swagger) görünecek örnek JSON verisi
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

# --- GEÇİCİ VERİTABANI ---
courses_db = [
    Course(id=1, title="Python", instructor="Atil", rating=5, published_date=2029),
    Course(id=2, title="Kotlin", instructor="Ahmet", rating=5, published_date=2026),
    Course(id=3, title="Jenkins", instructor="Atil", rating=5, published_date=2023),
    Course(id=4, title="Kubernetes", instructor="Zeynep", rating=2, published_date=2030),
    Course(id=5, title="Machine Learning", instructor="Fatma", rating=3, published_date=2036),
    Course(id=6, title="Deep Learning", instructor="Atlas", rating=1, published_date=2039)
]

# --- GET: VERİ OKUMA İŞLEMLERİ ---

# Tüm kursları listele
@app.get(path="/courses", status_code=status.HTTP_200_OK)
async def get_all_courses():
    return courses_db

# Path Parameter: URL'den gelen ID ile tek bir kursu bulur.
@app.get("/courses/{course_id}", status_code=status.HTTP_200_OK)
async def get_course(course_id: int = Path(gt=0)):
    for course in courses_db:
        if course.id == course_id:
            return course
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

# Query Parameter: ?course_rating=X şeklinde puana göre filtreler.
@app.get("/courses/", status_code=status.HTTP_200_OK)
async def get_courses_by_rating(course_rating: int = Query(gt=0, lt=6)):
    courses_to_return = []
    for course in courses_db:
        if course.rating == course_rating:
            courses_to_return.append(course)
    return courses_to_return

# Query Parameter: Yayın tarihine göre filtreler.
@app.get("/courses/publish/", status_code=status.HTTP_200_OK)
async def get_courses_by_publish_date(publish_date: int = Query(gt=2005, lt=2040)):
    courses_to_return = []
    for course in courses_db:
        if course.published_date == publish_date:
            courses_to_return.append(course)
    return courses_to_return

# --- POST: VERİ EKLEME ---

@app.post("/create-course", status_code=status.HTTP_201_CREATED)
async def create_course(course_request: CourseRequest):
    # Pydantic modelini alıp, Course sınıfına (nesneye) dönüştürür.
    new_course = Course(**course_request.model_dump())
    # Otomatik ID atayarak listeye ekler.
    courses_db.append(find_course_id(new_course))

# --- ID ATAMA YARDIMCISI ---
def find_course_id(course: Course):
    # Liste boşsa ID 1, değilse son kursun ID'sine 1 ekler.
    course.id = 1 if len(courses_db) == 0 else courses_db[-1].id + 1
    return course

# --- PUT: VERİ GÜNCELLEME ---

# 204_NO_CONTENT: İşlem başarılı ama geriye büyük bir veri dönmeyecek demektir.
@app.put("/courses/update_course", status_code=status.HTTP_204_NO_CONTENT)
async def update_course(course_request: CourseRequest):
    course_updated = False
    
    # Listedeki her kursun üzerinden geçiyoruz
    for i in range(len(courses_db)):
        # Gelen verideki ID ile listedeki ID eşleşiyor mu?
        if courses_db[i].id == course_request.id:
            # Eşleşirse, o indeksteki veriyi gelen yeni veriyle değiştiriyoruz.
            courses_db[i] = course_request
            course_updated = True
            break # Hedef bulundu, döngüyü durdur (Performans için önemli).

    # Eğer döngü bittiği halde ID bulunamadıysa hata fırlatılır.
    if not course_updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Course not found"
        )
    

"""
💡 Konu Özeti (Neleri Öğreniyoruz?)
range(len(courses_db)): Listede elemanların kendisiyle değil, konumlarıyla (indeks) çalışmak gerektiğinde kullanılır. Güncelleme yaparken o sıradaki veriyi tamamen değiştirmek için idealdir.

status.HTTP_204_NO_CONTENT: PUT ve DELETE işlemlerinde yaygın kullanılır. "İsteğini aldım, güncellemeyi yaptım, her şey yolunda ama sana gösterecek yeni bir sayfa/içerik yok" anlamına gelir.

course_updated Flag (Bayrak) Kullanımı: Döngü içinde bir şeyin olup olmadığını kontrol etmek için kullanılan mantıksal bir değişkendir. Eğer True olmazsa, kursun listede olmadığını anlarız.

"""