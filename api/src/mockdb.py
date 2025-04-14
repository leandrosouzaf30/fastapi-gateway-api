from src.domain.invoice import Invoice
from src.domain.account import Account
from dataclasses import dataclass
from typing import List

@dataclass
class MockDatabase:
    accounts: List[Account]
    invoices: List[Invoice]

    def __init__(self):
        self.accounts = []
        self.invoices = []

    def clear(self):
        self.accounts.clear()
        self.invoices.clear()