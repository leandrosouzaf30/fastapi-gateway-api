from fastapi import Header, HTTPException, APIRouter
from typing import List
from uuid import uuid4
from src.domain.account import Account
from src.mockdb import MockDatabase
from src.repositories.account_repository import AccountRepository
from src.repositories.invoice_repository import InvoiceRepository
from src.schemas.account_schemas import AccountRequest, AccountResponse


router = APIRouter(
    prefix="/accounts",
    tags=["accounts"],
    responses={404: {"description": "Não encontrado"}}
)

mock_db = MockDatabase()
account_repo = AccountRepository(mock_db)
invoice_repo = InvoiceRepository(mock_db)

# Dependency Injection
# account_repo = AccountRepository()
# invoice_repo = InvoiceRepository()


def get_account(api_key: str = Header(...)) -> Account:
    account = account_repo.get_by_api_key(api_key)
    if not account:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return account

# Routes
@router.post("/accounts", response_model=AccountResponse)
def create_account(data: AccountRequest):
    account = Account(id=uuid4(), name=data.name, email=data.email)
    account_repo.add(account)
    return AccountResponse(
        id=account.id,
        name=account.name,
        email=account.email,
        api_key=account.api_key,
        balance=account.balance(invoice_repo.list())
    )

@router.get("/accounts", response_model=List[AccountResponse])
def list_accounts():
    accounts = account_repo.list()
    invoices = invoice_repo.list()
    return [
        AccountResponse(
            id=a.id,
            name=a.name,
            email=a.email,
            api_key=a.api_key,
            balance=a.balance(invoices)
        ) for a in accounts
    ]
