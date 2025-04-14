from src.domain.account import Account
from typing import List, Optional
from src.mockdb import MockDatabase


class AccountRepository:
    def __init__(self, db: MockDatabase):
        self.db = db

    def add(self, account: Account):
        self.db.accounts.append(account)

    def list(self) -> List[Account]:
        return self.db.accounts

    def get_by_api_key(self, api_key: str) -> Optional[Account]:
        return next((a for a in self.db.accounts if a.api_key == api_key), None)