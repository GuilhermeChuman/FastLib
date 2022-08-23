from fastapi import FastAPI
from controllers import GenerosController

app = FastAPI()

@app.get("/generos")
def getGeneros():
    response = GenerosController.getGeneros()
    return response