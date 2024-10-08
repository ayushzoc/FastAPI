from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[float] = None

my_posts = [{"title": "title of post 1",
             "content": "content of post 1",
             "id": 1},
            {"title": "Favorite foods",
            "content": "I like Pizza",
            "id": 2}]

def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post

@app.get("/")
async def read_root():
    return {"message": "Welcome to my app!"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.model_dump()
    post_dict["id"] = randrange(0, 10000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"Post with id {id} not found")
    return {"post_detail": post}