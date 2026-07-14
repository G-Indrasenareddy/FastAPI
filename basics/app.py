from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def wish():
    return {"msg":"Good Evening"}