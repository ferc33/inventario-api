
from pydantic import BaseModel
from datetime import datetime

class RemittanceBase(BaseModel):
    order_id: int
    date: datetime

class RemittanceCreate(RemittanceBase):
    pass

class Remittance(RemittanceBase):
    id: int

    class Config:
        orm_mode = True
            