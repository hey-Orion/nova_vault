from pydantic import BaseModel

class Transaction(BaseModel):
    userId: int
    id: int
    title: str
