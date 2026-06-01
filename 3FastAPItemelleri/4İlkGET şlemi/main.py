from fastapi import FastAPI

app = FastAPI()

courses_db = [
    {'id': 1, 'instructor': 'Atil', 'title': 'Python', 'category': 'Development'},
    {'id': 2, 'instructor': 'Ahmet', 'title': 'Python', 'category': 'Development'},
    {'id': 3, 'instructor': 'Atil', 'title': 'Python', 'category': 'Devops'},
    {'id': 4, 'instructor': 'Zeynep', 'title': 'Python', 'category': 'Devops'},
    {'id': 5, 'instructor': 'Fatma', 'title': 'Python', 'category': 'AI'},
    {'id': 6, 'instructor': 'Atlas', 'title': 'Python', 'category': 'AI'}
]


@app.get("/hello")
async def hello_world():
    return{"message":"Hello world"}


@app.get("/courses")
async def get_all_courses():
    return courses_db



#terminale: uvicorn main:app --reload  