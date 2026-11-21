import random
from pydantic import BaseModel, Field


def random_warehouse() -> int:
    return random.randint(1, 5)


class Product(BaseModel):
    name: str = Field(
        description="Product title",
        min_length=3,
        max_length=100,
    )
    price: float = Field(
        description="Price is USD",
        gt=0,
        le=1000,
    )