from app.bank import BankAccount


def test_default_balance():
    account = BankAccount()
    assert account.get_balance() == 0

def test_initial_balance():
    account = BankAccount(initial_balance=100)
    assert account.get_balance() == 100

def test_deposit():
    account = BankAccount()
    account.deposit(50)
    assert account.get_balance() == 50

def test_withdraw():
    account = BankAccount(initial_balance=100)
    account.withdraw(30)
    assert account.get_balance() == 70

def test_withdraw_insufficient_funds():
    account = BankAccount(initial_balance=50)
    try:
        account.withdraw(100)
    except ValueError as e:
        assert str(e) == "Insufficient funds"