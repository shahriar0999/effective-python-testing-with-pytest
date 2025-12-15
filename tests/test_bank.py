from app.bank import BankAccount
import pytest 


@pytest.fixture
def default_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(initial_balance=200)

def test_default_balance(default_bank_account):
    assert default_bank_account.get_balance() == 0

def test_initial_balance(bank_account):
    assert bank_account.get_balance() == 200

def test_deposit(bank_account):
    bank_account.deposit(50)
    assert bank_account.get_balance() == 250

def test_withdraw(bank_account):
    bank_account.withdraw(30)
    assert bank_account.get_balance() == 170

def test_withdraw_insufficient_funds(bank_account):
    try:
        bank_account.withdraw(100)
    except ValueError as e:
        assert str(e) == "Insufficient funds"