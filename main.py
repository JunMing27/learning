from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class post(BaseModel):
    title: str
    content: str

@app.get("/test")
async def root():
    return {"message": "Hello World"}

@app.post("/demoposts")
def demo_post(thisIsJustAReferenceName:post):
    return {"message": "this is a post",
            "newpost": f"title: {thisIsJustAReferenceName.title} content :{thisIsJustAReferenceName.content}"
            }

# this is without pydantic 
# @app.post("/demoposts")
# def demo_post(payload: dict = Body(...)):
#     print(payload)
#     return {"message": "this is a post",
#             "newpost": f"title: {payload['title']} content :{payload['content']}"
#             }

# implementing pydantic for data validation and parsing