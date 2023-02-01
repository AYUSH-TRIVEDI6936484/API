from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def root():
    return {"message": "Hey, this is fastapi;"}

@app.get("/posts")
def get_posts():
    return {"data":"This is an info script"}

@app.post("/createposts")
def create_posts():
    return{"status":"successfully created a post"}