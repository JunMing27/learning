from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class post(BaseModel):
    title: str
    content: str
    published: bool = True # this will assign default value

my_posts = [{"title":"title of post", "content": "ipsum ", "id": 1},
            {"title":"title of post", "content": "ipssum ", "id": 2}
            ]

@app.get("/test")
async def root():
    return {"message": my_posts}

@app.post("/demoposts")
def demo_post(thisIsJustAReferenceName:post):
    # return {"message": "this is a post",
    #         "newpost": f"title: {thisIsJustAReferenceName.title} content :{thisIsJustAReferenceName.content}"
    #         }
    newDict = thisIsJustAReferenceName.dict()
    newDict['id']= randrange(0,1000000)
    my_posts.append(newDict)
    return{"data":newDict}

# this is without pydantic 
# @app.post("/demoposts")
# def demo_post(payload: dict = Body(...)):
#     print(payload)
#     return {"message": "this is a post",
#             "newpost": f"title: {payload['title']} content :{payload['content']}"
#             }

# implementing pydantic for data validation and parsing