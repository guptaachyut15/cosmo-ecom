from datetime import datetime, timezone
from pydantic import BaseModel


class Item(BaseModel):
    productId: str
    boughtQuantity: int


class UserAddress(BaseModel):
    city: str
    country: str
    zipcode: int


class Order(BaseModel):
    items: list[Item]
    totalAmount: int
    userAddress: UserAddress
    createdOn: datetime = datetime.now(timezone.utc)
