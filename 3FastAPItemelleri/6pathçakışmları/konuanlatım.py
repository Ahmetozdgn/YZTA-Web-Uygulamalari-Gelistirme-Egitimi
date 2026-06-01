# FastAPI kütüphanesini içe aktarıyoruz
from fastapi import FastAPI

# Web uygulamamızı oluşturuyoruz
app = FastAPI()


# Sahte veritabanı (liste içinde sözlükler)
# Gerçek projelerde burası genelde SQL veya NoSQL veritabanıdır
courses_db = [
    {'id': 1, 'instructor': 'Atil', 'title': 'Python', 'category': 'Development'},
    {'id': 2, 'instructor': 'Ahmet', 'title': 'Java', 'category': 'Development'},
    {'id': 3, 'instructor': 'Atil', 'title': 'Jenkins', 'category': 'Devops'},
    {'id': 4, 'instructor': 'Zeynep', 'title': 'Kubernetes', 'category': 'Devops'},
    {'id': 5, 'instructor': 'Fatma', 'title': 'Machine Learning', 'category': 'AI'},
    {'id': 6, 'instructor': 'Atlas', 'title': 'Deep Learning', 'category': 'AI'}
]


# --------------------------------------------------
# TEST ENDPOINT
# --------------------------------------------------
# http://127.0.0.1:8000/hello
@app.get("/hello")
async def hello_world():
    return {"message": "Hello world"}


# --------------------------------------------------
# TÜM KURSLARI GETİRİR
# --------------------------------------------------
# http://127.0.0.1:8000/courses
@app.get("/courses")
async def get_all_courses():
    return courses_db


# --------------------------------------------------
# PATH PARAMETRE - BAŞLIĞA GÖRE ARAMA
# --------------------------------------------------
# http://127.0.0.1:8000/courses/Python
@app.get("/courses/{course_title}")
async def get_course(course_title: str):

    # Liste içinde tek tek dolaşıyoruz
    for course in courses_db:

        # casefold() büyük/küçük harf farkını kaldırır
        if course.get('title').casefold() == course_title.casefold():
            return course


# --------------------------------------------------
# ❌ BU ÇALIŞMAZ (PATH ÇAKIŞMASI)
# --------------------------------------------------
# Çünkü yukarıdaki /courses/{course_title} ile aynı kalıptadır
# FastAPI ilk tanımlanan route'u çalıştırır
# Bu yüzden bu fonksiyon devreye girmez
@app.get("/courses/{course_id}")
async def get_course_by_id(course_id: int):
    for course in courses_db:
        if course.get('id') == course_id:
            return course


# --------------------------------------------------
# ✅ BU ÇALIŞIR (PATH AYRIŞTIRILDI)
# --------------------------------------------------
# http://127.0.0.1:8000/courses/byid/1
# Burada "byid" sabit bir kelime olduğu için çakışma olmaz
@app.get("/courses/byid/{course_id}")
async def get_course_by_id(course_id: int):
    for course in courses_db:
        if course.get('id') == course_id:
            return course


# --------------------------------------------------
# UYGULAMAYI ÇALIŞTIRMA
# --------------------------------------------------

# Terminal:
# uvicorn main:app --reload

# Swagger dokümantasyonu:
# http://127.0.0.1:8000/docs


# Önemli Mantık
# Çakışma neden olur?

# FastAPI şu yapıları aynı görür:

# /courses/{bir_deger}
# /courses/{baska_deger}

# İkisi de aynı şablondur.

# FastAPI:

# Yukarıdan aşağı okur

# İlk eşleşeni çalıştırır

# Diğerini görmez