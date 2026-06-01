from fastapi import FastAPI, Body, Path, Query, HTTPException
from typing import Optional
from pydantic import BaseModel, Field
from starlette import status  

app = FastAPI()

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


courses_db = [
    Course(id: 1, title: "Python", instructor: "Atil", rating: 5, published_date: 2029),
    Course(id: 2, title: "Kotlin", instructor: "Ahmet", rating: 5, published_date: 2026),
    Course(id: 3, title: "Jenkins", instructor: "Atil", rating: 5, published_date: 2023),
    Course(id: 4, title: "Kubernetes", instructor: "Zeynep", rating: 2, published_date: 2030),
    Course(id: 5, title: "Machine Learning", instructor: "Fatma", rating: 3, published_date: 2036),
    Course(id: 6, title: "Deep Learning", instructor: "Atlas", rating: 1, published_date: 2039)
]