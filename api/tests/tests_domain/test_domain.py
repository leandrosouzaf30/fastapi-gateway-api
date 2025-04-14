import pytest
from uuid import uuid4
from src.domain.account import Account, Invoice, InvoiceStatus
from src.domain.invoice import CreditCard


def test_account_balance():
    account_id = uuid4()
    account = Account(id=account_id, name="Test", email="test@example.com")

    invoices = [
        Invoice(id=uuid4(), account_id=account_id, amount=100.0, status=InvoiceStatus.approved, description=None, payment_type=None, card_last_digits=None),
        Invoice(id=uuid4(), account_id=account_id, amount=50.0, status=InvoiceStatus.pending, description=None, payment_type=None, card_last_digits=None),
        Invoice(id=uuid4(), account_id=account_id, amount=200.0, status=InvoiceStatus.approved, description=None, payment_type=None, card_last_digits=None),
    ]

    assert account.balance(invoices) == 300.0

def test_account_balance_with_no_approved():
    account_id = uuid4()
    account = Account(id=account_id, name="Empty", email="empty@example.com")

    invoices = [
        Invoice(id=uuid4(), account_id=account_id, amount=10.0, status=InvoiceStatus.pending, description=None, payment_type=None, card_last_digits=None),
        Invoice(id=uuid4(), account_id=account_id, amount=20.0, status=InvoiceStatus.rejected, description=None, payment_type=None, card_last_digits=None),
    ]

    assert account.balance(invoices) == 0.0

def test_credit_card_last_digits():
    card = CreditCard(number="1234567812345678")
    assert card.last_digits() == "5678"

    short_card = CreditCard(number="123")
    assert short_card.last_digits() == "123"

def test_account_api_key_length():
    account = Account(id=uuid4(), name="KeyTest", email="key@example.com")
    assert isinstance(account.api_key, str)
    assert len(account.api_key) == 16
