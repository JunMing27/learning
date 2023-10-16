from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
from . import models
from .database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True # this will assign default value

my_posts = [{"title":"title of post", "content": "ipsum ", "id": 1},
            {"title":"title of post", "content": "ipssum ", "id": 2}
            ]

@app.get("/test")
async def root():
    return {"message": my_posts}

@app.post("/demoposts", status_code=status.HTTP_201_CREATED)
def demo_post(post:Post, db : Session = Depends(get_db)):
    # return {"message": "this is a post",
    #         "newpost": f"title: {thisIsJustAReferenceName.title} content :{thisIsJustAReferenceName.content}"
    #         }
    newDict = post.dict()
    # print(newDict)
    # newDict['id']= randrange(0,1000000)
    # newpost = models.Post(title=post.title,content=post.content,published=post.published)
    # do a ** to convert the dict data (from base model format) into sql recognised data 
    newpost = models.Post(**post.dict())
    db.add(newpost)  # add to db
    db.commit() # commit it
    db.refresh(newpost) # retrieve and store value back in newpost var
    return{"data":newpost}

# this is without pydantic 
# @app.post("/demoposts")
# def demo_post(payload: dict = Body(...)):
#     print(payload)
#     return {"message": "this is a post",
#             "newpost": f"title: {payload['title']} content :{payload['content']}"
#             }

# implementing pydantic for data validation and parsing

@app.get("/demoposts/{id}")
def getpost(id: int,response:Response): #fastapi can validate and convert variable to int 

    post=find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f" id {id} is not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"post detail": f"id {id} is not found"}
    return {"post detail": post}

def find_post(id):
    for i in my_posts:
        if i['id'] == id:
            return i


@app.get("/sqlalchemy")
def test_posts(db:Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"data": posts}