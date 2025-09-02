from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, FastAPI with Python 3.11!"}
