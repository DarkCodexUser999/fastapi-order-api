from typing import Any, Callable

routes: dict[str,Callable[[Any],Any]]

def route(path: str):
    def register_route(func):
        routes[path] = func
        return func
    return register_route

