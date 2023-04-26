from fastapi import FastAPI, Depends, HTTPException,status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

#instancias de autentificacion

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username = str
    full_name: str
    email: str
    disabel: bool

class UserDB(BaseModel):
    password : str
    
users_db = {
    "mouredev":{
    
    "username":  "ulii-uwu",
    "full_name": "gabriel ulises",
    "email": "ulisesuliiuwu@gmail.com",
    "disabel": False,
    "password":"123456789"

    },
    "ulises2":{
    "username":  "ulii-uwu2",
    "full_name": " ulises",
    "email": "ulisesuliiuwu@gmail.com",
    "disabel": True,
    "password":"FDXD"

    }
}    


def search_user(username: str):
    if  username in users_db:
        return UserDB(users_db[username])
    
async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="credenciales no validas" , 
            headers={"WWW-Authenticate": "Bearer"})
    return user

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = user_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario no es correcto")
    user = search_user(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Contraseña no es correcta")
    
    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user


