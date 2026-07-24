from fastapi import APIRouter,HTTPException
from models.product import Product

router = APIRouter(prefix="/products")
products = [
    {
        "pid":101,
        "pname":"Pen",
        "price":20,
        "category":"stationary"
    },
    {
        "pid":102,
        "pname":"Book",
        "price":250,
        "category":"stationary"
    },
    {
        "pid":103,
        "pname":"LAptop",
        "price":65000,
        "category":"electronics"
    },
    {
        "pid":104,
        "pname":"Mouse",
        "price":500,
        "category":"electronics"
    },
    {
        "pid":105,
        "pname":"Bag",
        "price":800,
        "category":"stationary"
    }
]

'''
usage:Create new Product
Rest API URL: http://127.0.0.1:8000/products/create
METHOD TYPE: POST
Request Fields: pid,pname,price,category
Access Type:Public
'''
@router.post("/create")
def create_product(product:Product):
    products.append(product.dict())
    return {"msg":"New Product Created Successfully"}



'''
usage:Fetch all Products
Rest API URL:http://127.0.0.1:8000/products/read
Method Type:GET
Request Fields:None
Access Type:Public
'''
@router.get("/read")
def get_products():
    return products



'''
usage:Fetch Product By Id
Rest API URL:http://127.0.0.1:8000/products/read/101
Method Type:GET
Request Fields:None
Access Type:Public
'''
@router.get("/read/{pid}")
def get_product(pid:int):

    for product in products:

        if product["pid"]==pid:
            return product

    raise HTTPException(
        status_code=404,
        detail="Product Not Found"
    )



'''
usage:Fetch Products By Category
Rest API URL:http://127.0.0.1:8000/products/category/electronics
Method Type:GET
Request Fields:None
Access Type:Public
'''
@router.get("/category/{category_name}")
def get_products_by_category(category_name:str):

    result=[]

    for product in products:

        if product["category"].lower()==category_name.lower():
            result.append(product)

    return result



'''
usage:Fetch all Stationary Products
Rest API URL:http://127.0.0.1:8000/products/stationary
Method Type:GET
Request Fields:None
Access Type:Public
'''
@router.get("/stationary")
def get_stationary_products():

    result=[]

    for product in products:

        if product["category"].lower()=="stationary":
            result.append(product)

    return result



'''
usage:Fetch all Stationary Products Below Given Price
Rest API URL:http://127.0.0.1:8000/products/st?price=500
Method Type:GET
Request Fields:price
Access Type:Public
'''
@router.get("/st")
def get_stationary_products_by_price(price:int):

    result=[]

    for product in products:

        if product["category"].lower()=="stationary" and product["price"]<price:
            result.append(product)

    return result