from fastapi import Depends, Header, HTTPException, APIRouter
from typing import List
from uuid import uuid4, UUID
from src.domain.account import Account
from src.domain.invoice import Invoice, InvoiceStatus
from src.mockdb import MockDatabase
from src.repositories.account_repository import AccountRepository
from src.repositories.invoice_repository import InvoiceRepository
from src.schemas.invoice_schemas import InvoiceRequest, InvoiceResponse

router = APIRouter(
    prefix="/invoices",
    tags=["invoices"],
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


@router.post("/invoices", response_model=InvoiceResponse)
def create_invoice(data: InvoiceRequest, account: Account = Depends(get_account)):
    invoice = Invoice(
        id=uuid4(),
        account_id=account.id,
        amount=data.amount,
        status=InvoiceStatus.pending,
        description=data.description,
        payment_type=data.payment_type,
        card_last_digits=data.card_last_digits
    )
    invoice_repo.add(invoice)
    return invoice

@router.get("/invoices", response_model=List[InvoiceResponse])
def list_invoices(account: Account = Depends(get_account)):
    invoices = invoice_repo.list_by_account(account.id)
    return invoices

@router.get("/invoices/{invoice_id}", response_model=InvoiceResponse)
def get_invoice(invoice_id: UUID, account: Account = Depends(get_account)):
    invoice = invoice_repo.get(invoice_id)
    if not invoice or invoice.account_id != account.id:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice
