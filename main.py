from fastapi import FastAPI  # type: ignore[reportMissingImports]

new_app = FastAPI()

@new_app.get("/")
def root():
    return {"message":"hello world this is harsh tari"}

# # damn = (1,1,2,1,2,1,22,2,1,2,3,3,5,6,4,2,2,2,2,3,5,7)
# # print(damn.count(2))

# # class Account:
# #     def __init__(self,bal, acc):
# #         self.balance = bal
# #         self.acc = acc

# #     def debit(self, amount):
# #         self.balance = self.balance - amount
# # account1 = Account(23000, 123456)
# # print(account1.balance)

# # def root(number : float | int):
# #     if number > 10:
# #         return "greter than 10"
# #     else:
# #         pass

# # yo = root(12)
# # print(yo)

# # digits: list[int] = [2.4,3,4,5,6]
# # table : tuple[int,...] = (1,2)

# from typing import Any,Callable
# # student_data : dict[str | int , float] = {
# #     45 : 83.23,
# #     "Jazzy" : 99.99
# # }
# # print(type(45))

# # class City:
# #     def __init__(self,name,loc):
# #         self.name = name
# #         self.loc = loc

# # city_temp : tuple[City,float] = (City("Mumbai","India"),22)
# # print(city_temp)

# def fence(f):
#     def wrapper():
#         print("="*10)
#         f()
#         print("="*10)
#     return wrapper

# @fence
# def log():
#     print("hazy.ai")

# x= fence(log())
# print(x)

# add: Callable[[int,int],int | float]
# anything: Callable[[Any],Any]

from typing import Any, Callable 

routes: dict[str, Callable[[], Any]] = {}

def route(path: str):
    def register_route(func):
        routes[path]=func
        return func
    return register_route

@route("/Hello")
def get_hello():
    return "Hello There Dear User welcome"

@route("World")
def get_world():
    return "Hello World, This is API Success Message"

request : str = ""

while request != "quit":
    request = input("> ")

    if request in routes:
        response = routes[request]()
        print(response)
    else:
        print("404 Error - Not Found ")
    
