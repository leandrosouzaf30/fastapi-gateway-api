import secrets
from dataclasses import dataclass, field
from typing import List
from uuid import UUID
from .invoice import Invoice, InvoiceStatus


@dataclass
class Account:
    id: UUID
    name: str
    email: str
    api_key: str = field(default_factory=lambda: secrets.token_hex(8))

    def balance(self, invoices: List['Invoice']) -> float:
        return sum(i.amount for i in invoices if i.account_id == self.id and i.status == InvoiceStatus.approved)
