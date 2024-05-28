
from pydantic import BaseModel
from datetime import datetime

class OrderBase(BaseModel):
    provider_id: int
    date: datetime
    status: str

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True
            