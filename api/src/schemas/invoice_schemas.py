from typing import List, Optional
from pydantic import BaseModel
from uuid import UUID
from src.domain.invoice import InvoiceStatus

class InvoiceRequest(BaseModel):
    amount: float
    description: Optional[str]
    payment_type: Optional[str]
    card_last_digits: Optional[str]

class InvoiceResponse(BaseModel):
    id: UUID
    account_id: UUID
    amount: float
    status: InvoiceStatus
    description: Optional[str]
    payment_type: Optional[str]
    card_last_digits: Optional[str]