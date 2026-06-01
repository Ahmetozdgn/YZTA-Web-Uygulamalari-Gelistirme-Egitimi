from fastapi import FastAPI, Depends

app = FastAPI()


def hello_world():
    return "Hello, welcome to FastAPI!"


def get_hello_world(hello: str = Depends(hello_world)):
    return f"Hello world service: {hello_world()}"


@app.get("/hello")
def hello(message: str = Depends(get_hello_world)):
    return {"message": message}