from fastapi import FastAPI

app = FastAPI()

courses_db = [
    {'id': 1, 'instructor': 'Atil', 'title': 'Python', 'category': 'Development'},
    {'id': 2, 'instructor': 'Ahmet', 'title': 'Java', 'category': 'Development'},
    {'id': 3, 'instructor': 'Atil', 'title': 'Jenkins', 'category': 'Devops'},
    {'id': 4, 'instructor': 'Zeynep', 'title': 'Kubernetes', 'category': 'Devops'},
    {'id': 5, 'instructor': 'Fatma', 'title': 'Machine Learning', 'category': 'AI'},
    {'id': 6, 'instructor': 'Atlas', 'title': 'Deep Learning', 'category': 'AI'}
]


@app.get("/hello")
async def hello_world():
    return{"message":"Hello world"}


@app.get("/courses")
async def get_all_courses():
    return courses_db

# Path parametec
@app.get("/courses/{course_title}")
async def get_course(course_title: str):
    for course in courses_db:
        if course.get('title').casefold() == course_title.casefold():
            return course
        
# bu fonksiyon çalışmaz patikalar çakışır yukardki çalsırı
@app.get("/courses/{course_id}")
async def get_course_by_id(course_id: int):
    for course in courses_db:
        if course.get('id') == course_id:
            return course

# bu çalışır patikadan dolayı /courses/byid 
@app.get("/courses/byid/{course_id}")
async def get_course_by_id(course_id: int):
    for course in courses_db:
        if course.get('id') == course_id:
            return course



# Query
#* ?başlıyorsa path değil
@app.get("/courses/")
async def get_category_by_query(category: str):
    courses_to_return = []
    for course in courses_db:
        if course.get('category').casefold() == category.casefold():
            courses_to_return.append(course)
    return courses_to_return


# --------------------------------------------------
# PATH ve QUERY PARAMETREYİ AYNI ANDA KULLANMA
# --------------------------------------------------

# URL örneği:
# http://127.0.0.1:8000/courses/Atil/?category=Development

# Burada:
# Atil → PATH parametresi (URL'in içinde geliyor)
# category=Development → QUERY parametresi (? ile geliyor)

@app.get("/courses/{course_instructor}/")
async def get_instructor_category_by_query(course_instructor: str, category: str):

    # Eşleşen kursları tutmak için boş liste oluşturuyoruz
    courses_to_return = []

    # Tüm kursları tek tek kontrol ediyoruz
    for course in courses_db:

        # 1️⃣ Instructor eşleşiyor mu?
        # 2️⃣ Category eşleşiyor mu?
        # İkisi de doğruysa listeye ekle
        if (
            course.get('instructor').casefold() == course_instructor.casefold()
            and
            course.get('category').casefold() == category.casefold()
        ):
            courses_to_return.append(course)

    # Filtrelenmiş listeyi JSON olarak döndürür
    return courses_to_return

#terminale: uvicorn main:app --reload  
# http://127.0.0.1:8000/docs


"""
Bu Nasıl Çalışıyor?

Örnek istek:

/courses/Atil/?category=Development

FastAPI şunu yapar:

course_instructor = "Atil" (Path'ten aldı)

category = "Development" (Query'den aldı)

Sonra:

Instructor Atil mi?

Category Development mı?

İkisi de doğruysa listeye ekler ✅

"""


"""
Neden Path + Query Aynı Anda Kullanırız?

Çünkü genelde:

Path → ana kaynağı temsil eder (örneğin kullanıcı, instructor gibi)

Query → filtreleme için kullanılır

Profesyonel REST mantığında:

/courses/Atil/?category=AI

demek:

Atil'in kurslarından sadece AI kategorisini getir.

🧠 Mantık Özeti

Path → Zorunlu bilgi (kim?)
Query → Filtre bilgisi (hangi kategori?)

İkisini birlikte kullanarak daha esnek API yaparız 🚀

"""