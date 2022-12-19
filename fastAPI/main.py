#uvicorn main:app --reload
#http://127.0.0.1:8000

from fastapi import FastAPI 
app = FastAPI()

@app.get("/")
def test():
    return "FreeD Group"

