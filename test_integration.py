# test_integration.py
import pytest
from bank_app import transfer, calculate_interest

def test_transfer_success():
    from_balance, to_balance = transfer(2000, 1000, 500)
    assert from_balance == 1500
    assert to_balance == 1500

def test_transfer_insufficient_balance():
    with pytest.raises(ValueError):
        transfer(300, 1000, 500)

def test_transfer_and_interest_workflow():
    from_balance, to_balance = transfer(5000, 2000, 1000)
    final_balance = calculate_interest(to_balance, 10, 1)
    assert round(final_balance, 2) == 3300.00
