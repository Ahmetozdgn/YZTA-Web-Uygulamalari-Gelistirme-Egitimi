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


#terminale: uvicorn main:app --reload  
# http://127.0.0.1:8000/docs