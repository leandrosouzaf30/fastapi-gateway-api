from enum import Enum
from dataclasses import dataclass
from typing import Optional
from uuid import UUID

class InvoiceStatus(str, Enum):
    pending = "Pending"
    approved = "Approved"
    rejected = "Rejected"


@dataclass
class CreditCard:
    number: str

    def last_digits(self) -> str:
        return self.number[-4:] if len(self.number) >= 4 else self.number

@dataclass
class Invoice:
    id: UUID
    account_id: UUID
    amount: float
    status: InvoiceStatus
    description: Optional[str]
    payment_type: Optional[str]
    card_last_digits: Optional[str]
