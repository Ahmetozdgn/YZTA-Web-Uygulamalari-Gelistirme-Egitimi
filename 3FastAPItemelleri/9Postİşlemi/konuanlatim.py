from fastapi import FastAPI, Body

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


# Path ve Query Aynı Anda

@app.get("/courses/{course_instructor}/")
async def get_instructor_category_by_query(course_instructor: str, category: str):
    courses_to_return = []
    for course in courses_db:
        if (course.get('instructor').casefold() == course_instructor.casefold() 
                and course.get('category').casefold() == category.casefold()):
            courses_to_return.append(course)
    return courses_to_return


# POST İŞLEMİ (CREATE)

# POST metodu yeni veri eklemek için kullanılır
# Yani veritabanına yeni kurs ekliyoruz

@app.post("/courses/create_course")
async def create_course(new_course = Body()):

    # Body() ne demek?
    # Gelen verinin URL'den değil,
    # isteğin gövdesinden (body) geleceğini söyler

    # Yani kullanıcı Swagger veya başka bir yerden
    # JSON formatında veri gönderir

    # Örnek gönderilen JSON:
    # {
    #   "id": 7,
    #   "instructor": "Mehmet",
    #   "title": "Docker",
    #   "category": "Devops"
    # }

    # new_course değişkeni bu JSON verisini alır

    # Gelen yeni kursu listeye ekliyoruz
    courses_db.append(new_course)

    # Eklenen veriyi geri döndürmek iyi pratiktir
    return {
        "message": "Kurs başarıyla eklendi",
        "added_course": new_course
    }


"""
POST Nasıl Çalışır?

Swagger’a git:

http://127.0.0.1:8000/docs

POST /courses/create_course seç

"Try it out" tıkla

JSON gönder

Execute yap

Sunucu:

JSON’u alır

new_course değişkenine koyar

Listeye ekler

Geri cevap döner


| GET               | POST                    |
| ----------------- | ----------------------- |
| Veri getirir      | Veri ekler              |
| Body yok          | Body vardır             |
| URL'den veri alır | JSON body'den veri alır |

Body Nedir?

Body = İsteğin içinde gizli gelen veri kısmı

Path → URL içinden gelir
Query → ? ile gelir
Body → JSON olarak gönderilir

"""

#terminale: uvicorn main:app --reload  
# http://127.0.0.1:8000/docs