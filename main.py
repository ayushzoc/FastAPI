from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[float] = None

@app.get("/")
async def read_root():
    return {"message": "Welcome to my app!"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/posts")
def create_posts(post: Post):
    print(post.model_dump())
    return {"data": "New Post"}