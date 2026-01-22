from fastapi import FastAPI
from db import Base, engine

app = FastAPI()

@app.on_event("startup")
def start():
    Base.metadata.create_all(engine)

@app.get("/")
def root():
    return {"status": "Backend running"}