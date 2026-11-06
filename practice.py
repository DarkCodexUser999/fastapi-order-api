from fastapi import FastAPI
from typing import Callable, Any
from fastapi import HTTPException

app = FastAPI()
@app.get("/")
def root():
    return {"message": "This is a starting root message"}

routes : dict[str, Callable[[],Any]] = {}

def route(path:str):
    def register_path(func):
        routes[path] = func
        return func
    return register_path

@route("/Hello")
def get_hello():
    return "You are receiving a HELLO message"

@route("/welcome")
def get_wel():
    return "Welcome to the class of APIs"


# request : str=""

# while request != "quit":
#     request = input(">")

#     if request in routes:
#         response = routes[request]()
#         print(response)
#     else:
#         print("Server Error - 404 not found")

orders: dict[int, dict[str, Any]] = {
    101: {
        "product": "Macbook",
        "status": "On the way",
        "city": "Mumbai",
    },
    102: {
        "product": "Windows Pro",
        "status": "Delivered",
        "city": "Pune",
    },
    103: {
        "product": "Pure Linux XDX PC",
        "status": "Processing",
        "city": "Delhi",
    },
}

@app.get("/orders")
def get_orders():
    return{ "orders" : orders}

@app.get("/orders/id/{order_id}")
def get_one_order(order_id: int):
    if order_id not in orders:
        raise HTTPException(
            status_code= 404,
            detail = "order missing"
        )
    return { "order": orders[order_id] }

@app.get("/orders/query")
def get_order(order_id : int) ->dict[str, Any]:
    if order_id not in orders:
        raise HTTPException(
            status_code= 404,
            detail = "order missing"
            )
    return { "order": orders[order_id] }

@app.get("/orders/field/{field}")
def get_order_field(field: str, order_id : int) -> dict[str,str]:
    if order_id not in orders:
        raise HTTPException(
            status_code= 404,
            detail = "order missing"
            )
    if field not in orders[order_id]:
        raise HTTPException(
            status_code=404,
            detail = "invalid details"
        )
    return { field: orders[order_id][field] }

#6th and 7th and 8th
@app.post("/orders", status_code =201)
def order_post(data: dict[str,Any])->dict[str, Any]:
    
    product= data["product"]
    status = data["status"]
    city = data["city"]

    # if product not in orders:
    #     raise HTTPException(
    #         status_code = 400,
    #         detail = "Invalid product name provided"
    #     )
    # # if product not isinstance(str, (str,Any)):
        
    # if status not in orders:
    #         raise HTTPException(
    #             status_code = 400,
    #             detail = "Invalid product name provided"
    #         )
    # if city not in orders:
    #         raise HTTPException(
    #             status_code = 400,
    #             detail = "Invalid product name provided"
    #         )

    if not isinstance(product, str) or not product.strip():
        raise HTTPException(
            status_code=400,
            detail = "Product MUST be a text"
        )
    if not isinstance(status, str) or not status.strip():
        raise HTTPException(
            status_code=400,
            detail = "Status MUST be a text"
        )
    if not isinstance(city, str) or not city.strip():
        raise HTTPException(
            status_code=400,
            detail = "city MUST be a text"
        )
    
    new_id = max(orders.keys()) +1 

    orders[new_id] ={
        "product": product,
        "status": status,
        "city": city
    }

    return{"order_id": new_id }
