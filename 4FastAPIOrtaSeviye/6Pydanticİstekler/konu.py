from fastapi import FastAPI, Body, Path, Query, HTTPException
from typing import Optional
from pydantic import BaseModel, Field
from starlette import status  

app = FastAPI()

# --- VERİ MODELİ (MANUEL YÖNETİM) ---
# Bu sınıf, bellekte tutacağımız gerçek nesnelerin kalıbıdır.
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

# --- PYDANTIC MODELİ (DOĞRULAMA VE ŞEMA) ---
# Kullanıcıdan veri alırken (POST) "Kurallarımızı" belirlediğimiz yerdir.
class CourseRequest(BaseModel):
    # Optional: Bu alan zorunlu değil (Default=None)
    id: Optional[int] = Field(description="The id of the course, optional", default=None)
    # Field: Verinin sınırlarını çizer (Min karakter, max karakter vb.)
    title: str = Field(min_length=3, max_length=100)
    instructor: str = Field(min_length=3)
    # gt=0, lt=6: Puanın mutlaka 1 ile 5 arasında olmasını sağlar.
    rating: int = Field(gt=0, lt=6)
    # gte/lte: "Eşit veya büyük/küçük" (2020 ve 2100 dahil)
    published_date: int = Field(gte=2020, lte=2100)

    # model_config: /docs sayfasında (Swagger UI) kullanıcıya hazır örnek veri gösterir.
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

# Uygulama başladığında hazır gelecek olan örnek veri listemiz
courses_db = [
    Course(id=1, title="Python", instructor="Atil", rating=5, published_date=2029),
    Course(id=2, title="Kotlin", instructor="Ahmet", rating=5, published_date=2026),
    Course(id=3, title="Jenkins", instructor="Atil", rating=5, published_date=2023),
    Course(id=4, title="Kubernetes", instructor="Zeynep", rating=2, published_date=2030),
    Course(id=5, title="Machine Learning", instructor="Fatma", rating=3, published_date=2036),
    Course(id=6, title="Deep Learning", instructor="Atlas", rating=1, published_date=2039)
]

# --- GET METODLARI (VERİ ÇEKME) ---

@app.get(path="/courses", status_code=status.HTTP_200_OK)
async def get_all_courses():
    # Tüm listeyi JSON formatında geri döner.
    return courses_db

@app.get("/courses/{course_id}", status_code=status.HTTP_200_OK)
async def get_course(course_id: int = Path(gt=0)):
    # Path Parameter: URL'den gelen ID'yi alır.
    for course in courses_db:
        if course.id == course_id:
            return course
    # Eğer döngü biter ve bulunamazsa 404 hatası fırlatır.
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

@app.get("/courses/", status_code=status.HTTP_200_OK)
async def get_courses_by_rating(course_rating: int = Query(gt=0, lt=6)):
    # Query Parameter: ?course_rating=5 şeklinde filtreleme yapar.
    courses_to_return = []
    for course in courses_db:
        if course.rating == course_rating:
            courses_to_return.append(course)
    return courses_to_return

@app.get("/courses/publish/", status_code=status.HTTP_200_OK)
async def get_courses_by_publish_date(publish_date: int = Query(gt=2005, lt=2040)):
    # Belirli bir yıla göre filtreleme yapar.
    courses_to_return = []
    for course in courses_db:
        if course.published_date == publish_date:
            courses_to_return.append(course)
    return courses_to_return

# --- POST METODU (YENİ VERİ EKLEME) ---

@app.post("/create-course", status_code=status.HTTP_201_CREATED)
async def create_course(course_request: CourseRequest):
    # .model_dump(): Pydantic nesnesini standart Python sözlüğüne (dict) çevirir.
    # **: Sözlükteki anahtar-değer ikililerini Course sınıfının içine dağıtır.
    new_course = Course(**course_request.model_dump())
    # find_course_id: Kursu veritabanına eklemeden önce otomatik ID atar.
    courses_db.append(find_course_id(new_course))

# --- YARDIMCI FONKSİYON ---
def find_course_id(course: Course):
    # Eğer liste boşsa ID'yi 1 yap, değilse son elemanın ID'sine 1 ekle.
    course.id = 1 if len(courses_db) == 0 else courses_db[-1].id + 1
    return course



"""
💡 Bilmen Gereken Kritik Noktalar
BaseModel (Pydantic): Gelen verinin tipini (int, str) ve içeriğini kontrol eder. Eğer kullanıcı rating kısmına 10 yazarsa, FastAPI kodun içine bile girmeden kullanıcıya hata döner.

model_dump(): Pydantic modelini normal bir sınıfa dönüştürürken kullanılan en güncel metottur (Eski sürümlerde .dict() kullanılırdı).

201 Created: Yeni bir şey oluşturulduğunda standart başarı kodu 200 değil, 201'dir.

find_course_id Mantığı: Veritabanı kullanmadığımız için courses_db[-1].id + 1 yaparak ID'nin her zaman benzersiz ve sıralı gitmesini sağlıyoruz.
"""