from  fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

User_list=[User(id=1,name="gabriel",surname="MG",url="https://www.youtube.com/watch?v=_y9qQZXE24A",age=19),
           User(id=2,name="paulina",surname="gonzale",url="https://www.youtube.com/watch?v=_y9qQZXE24A",age=19),
           User(id=3,name="fer",surname="mondragon",url="https://www.youtube.com/watch?v=_y9qQZXE24A",age=19)] 

@app.get("/usersJson")
async def usersJson():
    return [{"name":"gabriel", "surname":"MG","url":"https://www.youtube.com/watch?v=_y9qQZXE24A","age":19},
            {"name":"paulina", "surname":"gonzale","url":"https://www.youtube.com/watch?v=_y9qQZXE24A","age":19},
            {"name":"fer","modragon":"MG","url":"https://www.youtube.com/watch?v=_y9qQZXE24A","age":19},]
 

@app.get("/users")
async def users():
    return User_list

#operacion  con path
@app.get("/user/{id}")
async def user(id: int):
   return search_user

#operacion con query    
@app.get("/userquery/")
async def user(id: int):
    return search_user(id)

def search_user(id: int):
    user = filter(lambda user: user.id == id, User_list)
    try:
        return list(user)[0]
    except:
      return {"error": "No se encontro este usuario :("} 
