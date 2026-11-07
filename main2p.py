# from fastapi import FastAPI
# from typing import Any,Callable

# app = FastAPI()
# @app.get("/")
# def root():
#     return {"message":"Hello world this is Harsh Tari"}

# routes: dict[str, Callable[[],Any]] = {}

# def route(path: str):
#     def register_route(func):
#         routes[path] = func
#         return func
#     return register_route


# @route("/Hello")
# def get_hello():
#     return "This is a hello message"

# @route("/Welcome")
# def wel():
#     return "This is a welcome message"

# @route("/Intro")
# def intro():
#     return "This is a starting working introduction"

# @route("/about")
# def about():
#     return "Hi! This is harsh tari...uhh lets just say im a guy from mumbai \n passianate about many things in life like let's just say formula one ! wohoooo ! \nI think you must be liking that too .correct?? I turned 20 last month ! can't believe \n that I'm existing on this planet from the last 20 yrs..offff damn that's \n Just so Kwazyyyyy"


# request : str= ""

# while request != "quit":
#     request = input(">")

#     if request in routes:
#         response = routes[request]()
#         print(response)
#     else:
#         print("Error - 404 Not Found")

# from fastapi import FastAPI
# from typing import Callable, Any

# app = FastAPI()
# @app.get("/")
# def root():
#     return { "message":"Welcome to the APIs"}

# routes: dict[str, Callable[[],Any]]= {}

# def route(path: str):
#     def register_function(func):
#         routes[path]= func
#         return func
#     return register_function

# @route("/Hello")
# def get_hello():
#     return "Hello message printed"

# request : str=""

# while request != "quit":
#     request = input(">")

#     if request in routes:
#         response = routes[request]()
#         print(response)
#     else:
#         print("Error - 404 not found")


from fastapi import FastAPI, HTTPException
from typing import Any

app = FastAPI()

@app.get("/")
def root():
    return {"Welcome": "Welcome to the API demonstration"}

orders: dict[int, dict[str, Any]] = {
    101: {
        "product": "Keyboard",
        "status": "On the way",
        "city": "Mumbai",
    },
    102: {
        "product": "Mouse",
        "status": "Delivered",
        "city": "Pune",
    },
    103: {
        "product": "Headphones",
        "status": "Processing",
        "city": "Delhi",
    },
    105: {
            "product": "Mac",
            "status": "Processing",
            "city": "Banglore",
        },
}

@app.get("/hello")
def get_hello():
    return {"message": "this is a hello message"}


@app.get("/orders/{sec}")
def get_order_stat(sec: str, order_id: int):
    if order_id not in orders:
        raise HTTPException(
            status_code= 404,
            detail = "order not found",
        )

    if sec not in orders[order_id]:
        raise HTTPException(
            status_code = 404,
            detail = "order not found"
        )

    return{
        sec: orders[order_id][sec]
    }

# @app.get("/orders/{sec}")
# def prac_endpoint(sec: str,order_id:int) -> dict[str,Any]:
    
#     if order_id not in orders:
#         raise HTTPException(
#             status_code = 404,
#             detail = "error",
#         )

#     if sec not in orders[order_id]:
#         raise HTTPException(
#             status_code=404,
#             detail="Field not found",
#         )
#     return {
#         sec: orders[order_id][sec]
#     }

@app.post("/orders")
def create_new_id( data : dict[str, Any]) ->dict[str, int]:

    req_fields = ["name","price","stock"]

    for field in req_fields:
        if field not in data:
            raise HTTPException(
                status_code= 400,
                detail=f"{field} not found",
                )

    name = data["name"]
    price = data["price"]
    stock = data["stock"]

    if not isinstance(stock, int) or stock <0:
        raise HTTPException(
            status_code=404,
            detail="Order not found",
        )
 
    new_id = max(orders.keys()) + 1

    orders[new_id] = {
        "name" : name, 
        "price" : price, 
        "stock": stock
    }

    return {"order_id": new_id}

@app.get("/orders")
def get_orders():

    return{
        "orders" : orders
    }



# @app.get("/orders")
# def get_order_status(order_id: int | None = None) -> dict[str, Any]:

#     if order_id is None:
#         order_id = max(orders)
    
#     if order_id not in orders:
#         raise HTTPException(
#             status_code=404,
#             detail="Order not found",
#         )
#     else:
#         return orders[order_id]
    #     return{
    #     "order_id": order_id,
    #     "product": orders[order_id]["product"],
    #     "status" : orders[order_id]["status"],
    #     "city" : orders[order_id]["city"]
    # }

@app.post("/orders")
def create_order(name: str, data: dict[str, Any]) -> dict[str,int]:

    price = data["price"]
    stock = data["stock"]

    if not isinstance(price, (int, float)):
        raise HTTPException(
            status_code = 404,
            detail = "Price should be a number",
        )
    if name.isdigit():
        raise HTTPException(
            status_code = 400,
            detail = "The name section should contain words!"
        )

    new_id = max(orders.keys()) + 1

    orders[new_id] = {
        "name" : name, 
        "price" : price, 
        "stock": stock
    }

    return {"order_id": new_id}

@app.put("/orders")
def replace_order(product: str, status: str, city: str , order_id: int) ->dict[str, Any]:

    if order_id not in orders:
        raise HTTPException(
            status_code = 400,
            detail = "order_id is invalid "
            )

    order = orders[order_id]

    orders[order_id]={
        "product" : product, "status": status, "city": city
       }

    return orders[order_id]

@app.patch("/orders")
def replace_ind(order_id: int, body: dict[str, Any],
                # product: str | None = None,
                # status: str | None = None,
                # city: str | None = None,
                ) ->dict[str, Any]:
    
    if order_id not in orders:
        raise HTTPException(status_code=404, detail="Order not found")
    
    # order= orders[order_id]

    # if product is not None:
    #     order["product"] = product

    # if status is not None:()
    #     order["status"] = status

    # if city is not None:
    #     order["city"] = city

    orders[order_id].update(body)
    return orders[order_id]

@app.delete("/orders")
def delete_order(order_id: int) -> dict[str, Any]:

    del orders[order_id]
    return { "status": f"Order {order_id} has been deleted successfully!"}

