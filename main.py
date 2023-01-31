from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def root():
    return {"message": "Hey, this is fastapi"}