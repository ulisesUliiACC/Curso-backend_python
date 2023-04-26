from fastapi import APIRouter
#para esto solo se usaria este "/" y acompañado con parametros
#el prefix indica la ruta en el router 
router = APIRouter( prefix="/products", tags=["products"],responses={404:{"message": "Not Found"}})

products_list = ["producto 1",
                "producto 2",
                "producto 3",
                "producto 4",
                "producto 5"]

#en esta tecion solo con el prefijo "/" indica que es /products
@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def products():
    return products_list