from  fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

User_list=[User(id=1,name="gabriel",surname="MG",url="https://www.youtube.com/watch?v=_y9qQZXE24A",age=19),
           User(id=2,name="paulina",surname="gonzale",url="https://www.youtube.com/watch?v=_y9qQZXE24A",age=19),
           User(id=3,name="fer",surname="mondragon",url="https://www.youtube.com/watch?v=_y9qQZXE24A",age=19)] 

@router.get("/usersJson")
async def usersJson():
    return [{"name":"gabriel", "surname":"MG","url":"https://www.youtube.com/watch?v=_y9qQZXE24A","age":19},
            {"name":"paulina", "surname":"gonzale","url":"https://www.youtube.com/watch?v=_y9qQZXE24A","age":19},
            {"name":"fer","modragon":"MG","url":"https://www.youtube.com/watch?v=_y9qQZXE24A","age":19},]
 

@router.get("/users")
async def users():
    return User_list


#operacion  con path
@router.get("/user/{id}")
async def user(id: int):
    return search_user(id)

#operacion con query    
@router.get("/user/")
async def user(id: int):
    return search_user(id)

                #codigos de http
@router.post("/user/",response_model=User,status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
     raise   HTTPException (status_code=404, detail="El usuario existe :( ")
        
    
    User_list.append(user)
    return user

@router.put("/user/")
async def user(user: User):
    found = False

    for index, saved_user in enumerate(User_list):
        if saved_user.id == user.id:
            User_list[index] = user
            found = True
    if not found:
        return { "error":"No se a actulizado"}
    
    return user

@router.delete("/user/{id}") #usar el parametro de path para id 
async def user(id: int):
    found= False
    for index,save_user in enumerate(User_list):
        if save_user.id == id:
            del User_list[index]
            found = True
    if  not found: 
        return {"error": "No se ha eliminado el usuario"}

def search_user(id: int):
    users = filter(lambda user: user.id == id, User_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se encontro este usuario :("}