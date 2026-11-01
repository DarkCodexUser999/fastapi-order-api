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

app = FastAPI()

@app.get("/")
def root():
    return {"Welcome": "Welcome to the API demonstration"}

orders = {
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
}

@app.get("/hello")
def get_hello():
    return {"message": "this is a hello message"}

@app.get("/order")
def stat():
    return "To check Order status, enter order number followed by /order/your_number."

@app.get("/order/{order_id}")
def get_order_status(order_id: int):
    if order_id not in orders:
        raise HTTPException(
            status_code=404,
            detail="Order not found",
        )
    return {
        "order_id": order_id,
        "product": orders[order_id]["product"],
        "status" : orders[order_id]["status"],
        "city" : orders[order_id]["city"]
    }

