from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    a = 1
    b = 2
    suma = a + b
    return {"hello":"world4","la suma es":suma}