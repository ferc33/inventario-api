
from pydantic import BaseModel
from datetime import datetime

class InvoiceBase(BaseModel):
    provider_id: int
    date: datetime
    total: int

class InvoiceCreate(InvoiceBase):
    pass

class Invoice(InvoiceBase):
    id: int

    class Config:
        orm_mode = True
            