from fastapi import FastAPI
from fastapi.params import Body

app=FastAPI()

@app.get("/")
def root():
    return {"message": "Hey, this is fastapi;"}

@app.get("/posts")
def get_posts():
    return {"data":"This is an info script"}

@app.post("/createposts")
def create_posts(newpost: dict= Body(...)):
    print(newpost)
    return{"new_post": f"data: {newpost['data']} title: {newpost['title']} "}
