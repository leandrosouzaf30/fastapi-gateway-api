from pydantic import BaseModel
from uuid import UUID

class AccountRequest(BaseModel):
    name: str
    email: str

class AccountResponse(BaseModel):
    id: UUID
    name: str
    email: str
    api_key: str
    balance: float