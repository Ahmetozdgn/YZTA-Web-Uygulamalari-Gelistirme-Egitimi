# FastAPI kütüphanesini içe aktarıyoruz
from fastapi import FastAPI

# Web uygulamasını oluşturuyoruz
app = FastAPI()


# Bu bizim sahte veritabanımız (liste içinde sözlükler)
# Gerçek projede burası genelde veritabanı olur
courses_db = [
    {'id': 1, 'instructor': 'Atil', 'title': 'Python', 'category': 'Development'},
    {'id': 2, 'instructor': 'Ahmet', 'title': 'Java', 'category': 'Development'},
    {'id': 3, 'instructor': 'Atil', 'title': 'Jenkins', 'category': 'Devops'},
    {'id': 4, 'instructor': 'Zeynep', 'title': 'Kubernetes', 'category': 'Devops'},
    {'id': 5, 'instructor': 'Fatma', 'title': 'Machine Learning', 'category': 'AI'},
    {'id': 6, 'instructor': 'Atlas', 'title': 'Deep Learning', 'category': 'AI'}
]


# Basit test endpoint
# http://127.0.0.1:8000/hello
@app.get("/hello")
async def hello_world():
    return {"message": "Hello world"}


# Tüm kursları getirir
# http://127.0.0.1:8000/courses
@app.get("/courses")
async def get_all_courses():

    # Tüm listeyi JSON olarak döndürür
    return courses_db


# PATH PARAMETRESİ ÖRNEĞİ
# URL'den veri alıyoruz
# Örnek:
# http://127.0.0.1:8000/courses/Python
@app.get("/courses/{course_title}")
async def get_course(course_title: str):

    # Liste içinde tek tek dolaşıyoruz
    for course in courses_db:

        # course.get('title') → kursun başlığını alır
        # casefold() → büyük/küçük harf duyarlılığını kaldırır
        # (Python, python, PYTHON fark etmez)
        if course.get('title').casefold() == course_title.casefold():

            # Eşleşen kursu bulursa onu döndürür
            return course