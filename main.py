from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {'message': 'Hello World'}

@app.get("/about")
def about():
    return {'message': 'In this learning we will work really hard and focus on Fundamentals.'}
