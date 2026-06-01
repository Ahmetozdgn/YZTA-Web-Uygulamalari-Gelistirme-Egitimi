from fastapi import FastAPI, Body, Path, Query, HTTPException
from typing import Optional
from pydantic import BaseModel, Field
from starlette import status  

app = FastAPI() # FastAPI uygulamasını başlatan ana nesne

# Kurs verilerini temsil eden sınıf (Veri Şablonu)
class Course:
    def __init__(self, id: int, title: str, instructor: str, rating: int, published_date: int):
        self.id = id
        self.title = title
        self.instructor = instructor
        self.rating = rating
        self.published_date = published_date

# Geçici veritabanı (Liste içinde Course nesneleri tutuluyor)
courses_db = [
    Course(id=1, title="Python", instructor="Atil", rating=5, published_date=2029),
    Course(id=2, title="Kotlin", instructor="Ahmet", rating=5, published_date=2026),
    Course(id=3, title="Jenkins", instructor="Atil", rating=5, published_date=2023),
    Course(id=4, title="Kubernetes", instructor="Zeynep", rating=2, published_date=2030),
    Course(id=5, title="Machine Learning", instructor="Fatma", rating=3, published_date=2036),
    Course(id=6, title="Deep Learning", instructor="Atlas", rating=1, published_date=2039)
]

# 1. Tüm kursları listeleyen endpoint
@app.get(path="/courses", status_code=status.HTTP_200_OK)
async def get_all_courses():
    return courses_db

# 2. Path Parameter kullanarak ID ile kurs bulma (ID 0'dan büyük olmalı)
@app.get("/courses/{course_id}", status_code=status.HTTP_200_OK)
async def get_course(course_id: int = Path(gt=0)):
    for course in courses_db:
        if course.id == course_id:
            return course
    # Kurs bulunamazsa 404 hatası döndürür
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

# 3. Query Parameter kullanarak puana (rating) göre filtreleme (1-5 arası)
@app.get("/courses/", status_code=status.HTTP_200_OK)
async def get_courses_by_rating(course_rating: int = Query(gt=0, lt=6)):
    courses_to_return = []
    for course in courses_db:
        if course.rating == course_rating:
            courses_to_return.append(course)
    return courses_to_return

# 4. Query Parameter kullanarak yıla göre filtreleme (2005-2040 arası)
@app.get("/courses/publish/", status_code=status.HTTP_200_OK)
async def get_courses_by_publish_date(publish_date: int = Query(gt=2005, lt=2040)):
    courses_to_return = []
    for course in courses_db:
        if course.published_date == publish_date:
            courses_to_return.append(course)
    return courses_to_return

"""
📝 Özet Konu Anlatımı
Path Parameter ({course_id}): URL'in bir parçasıdır. Örn: /courses/3. Belirli bir kaynağa doğrudan ulaşmak için kullanılır.

Query Parameter (?rating=5): URL'in sonuna eklenir. Kaynakları filtrelemek veya sıralamak için kullanılır.

Validation (gt/lt): gt (greater than - büyük), lt (less than - küçük) anlamına gelir. Kullanıcının hatalı veri girmesini (örneğin 100 puan vermesini) otomatik engeller.

HTTP Status Codes: İşlemin sonucunu tarayıcıya bildirir. 200 OK (Başarılı), 404 Not Found (Bulunamadı).
"""