
from pydantic import BaseModel

class ProviderBase(BaseModel):
    name: str
    contact_info: str

class ProviderCreate(ProviderBase):
    pass

class Provider(ProviderBase):
    id: int

    class Config:
        orm_mode = True
            