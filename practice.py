from fastapi import FastAPI
from typing import Callable, Any

app = FastAPI()
@app.get("/")
def root():
    return {"message": "This is a starting root message"}

routes : dict[str, Callable[[],Any]] = {}

def route(path:str):
    def register_path(func):
        routes[path] = func
        return route
    return register_path

@route("/Hello")
def get_hello():
    return "You are receiving a HELLO message"

@route("/welcome")
def get_wel():
    return "Welcome to the class of APIs"


request : str=""

while request != "quit":
    request = input(">")

    if request in routes:
        response = routes[request]()
        print(response)
    else:
        print("Server Error - 404 not found")
    