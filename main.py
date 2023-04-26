from   fastapi import  FastAPI

from routers import products,users

app = FastAPI()

#routers  importacion
#para llamar desde el main del proyecto 
app.include_router(products.router)
app.include_router(users.router)

@app.get("/")
def  root():
    return "hola ulises"

@app.get("/url")
async def url():
    return {"url": "https://github.com/ulisesUliiACC"}