from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app=FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool= True
    rating: Optional[int]= None
    
    
my_posts=[{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "title of post 2", "content": "content of post 2", "id": 2}, {"title": "title of post 3", "content": "content of post 3", "id": 3}]


def find_post(id):
    for post in my_posts:
        if post["id"]==id:
            return post
        

def find_index(id):
    for i, p in enumerate(my_posts):
        if p["id"]==id:
            return i  



@app.get("/")
async def root():
    return {"message": "hii World"}


@app.get("/posts")
def get_posts():
    return{"data": my_posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post :Post):    
    post_dict=post.dict()
    post_dict['id']=randrange(0, 1000000)
    my_posts.append(post_dict)
    return{"data": post_dict}


@app.get("/posts/latest")
def get_latest_post():
    post=my_posts[len(my_posts)-1]
    return{"latest_post": post}


# USING RESPONSE

# @app.get("/posts/{id}")
# def get_post(id: int, response: Response):
#     post = find_post(id)
#     if not post:
#         response.status_code=status.HTTP_404_NOT_FOUND
#         return{"message": f"post with id: {id} not found!!"}
#     return{"post": post}



# USING HTTP EXCEPTION
# MOST PEREFERED AS IT IS SHORT
@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found!!")
    return{"post": post}


@app.delete("/posts/{id}")
def delete_post(id: int):
    index=find_index(id)
    
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found!!")
    
    my_posts.pop(index)
    return{"message": f"post with id {id} was deleted"}



@app.put("/posts/{id}")
def update_post(id: int ,post:Post):
    index=find_index(id)
    
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found!!")
    
    post_dict=post.dict()
    post_dict["id"]=id
    my_posts[index]=post_dict
    return{"data": post_dict}