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


# post işlemi
@app.post("/courses/create_course")
async def create_course(new_course=Body()):
    courses_db.append(new_course)


#* UPDATE (PUT) – Güncelleme İşlemi
@app.put("/courses/update_course")
async def update_course(update_course = Body()):

    # Body() ile gelen JSON verisini alıyoruz
    # Kullanıcı güncellenmiş kurs bilgisini gönderir

    # Örnek gönderilen JSON:
    # {
    #   "id": 1,
    #   "instructor": "Atil",
    #   "title": "Advanced Python",
    #   "category": "Development"
    # }

    # Listeyi index ile dolaşıyoruz
    for index in range(len(courses_db)):

        # Eğer id eşleşirse
        if courses_db[index].get("id") == update_course.get("id"):

            # Eski veriyi tamamen yeni veri ile değiştiriyoruz
            courses_db[index] = update_course

# 🔥 PUT Mantığı
# PUT = Var olan veriyi tamamen değiştirir
# id’ye göre bulur
# Eski kaydı silmez, yerine yenisini koyar

# 🔴 DELETE – Silme İşlemi
@app.delete("/courses/delete_course/{course_id}")
async def delete_course(course_id: int):

    # course_id path parametresinden gelir
    # Örnek:
    # /courses/delete_course/3

    for index in range(len(courses_db)):

        # Eğer id eşleşirse
        if courses_db[index].get("id") == course_id:

            # Listeden o kaydı siliyoruz
            courses_db.pop(index)

            # Silince döngüyü durduruyoruz
            break
# 🔥 DELETE Mantığı
# DELETE = Veri siler
# id path üzerinden gelir
# Eşleşen kaydı listeden çıkarır



"""
| İşlem  | HTTP   | Ne Yapar         |
| ------ | ------ | ---------------- |
| Create | POST   | Yeni veri ekler  |
| Read   | GET    | Veri getirir     |
| Update | PUT    | Veriyi günceller |
| Delete | DELETE | Veriyi siler     |

Swagger’dan Test
http://127.0.0.1:8000/docs

Buradan:

POST → veri ekle

PUT → güncelle

DELETE → sil

🧠 Küçük Profesyonel Not

Şu an:

Validation yok

Hata kontrolü yok

404 dönüşü yok

Gerçek projede:

Pydantic model kullanılır

HTTPException eklenir

Status code döndürülür
"""