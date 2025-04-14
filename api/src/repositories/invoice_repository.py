from src.domain.invoice import Invoice
from typing import List, Optional
from uuid import UUID
from src.mockdb import MockDatabase



class InvoiceRepository:
    def __init__(self, db: MockDatabase):
        self.db = db

    def add(self, invoice: Invoice):
        self.db.invoices.append(invoice)

    def list(self) -> List[Invoice]:
        return self.db.invoices

    def get(self, id: UUID) -> Optional[Invoice]:
        return next((i for i in self.db.invoices if i.id == id), None)

    def list_by_account(self, account_id: UUID) -> List[Invoice]:
        return [i for i in self.db.invoices if i.account_id == account_id]