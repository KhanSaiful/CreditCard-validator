import pytest

from card_validator.validator import get_issuer


def test_get_issuer_visa():
    assert get_issuer("4343 4123 1435 1231") == "Visa"


def test_get_issuer_master_card():
    assert get_issuer('5123 4553 2345 2345') == "MasterCard"
    with pytest.raises(ValueError):
        get_issuer('5623 4553 2345 2345') == "MasterCard"


def test_get_issuer_american_express():
    assert get_issuer("3723 2342 3454 343") == "American Express"
    with pytest.raises(ValueError):
        get_issuer("3123 2342 3454 343") == "American Express"


def test_length():
    with pytest.raises(ValueError):
        get_issuer("5343 4123 1435 1231 2")
    with pytest.raises(ValueError):
        get_issuer("5343 4123 1435 1231 3")
    with pytest.raises(ValueError):
        get_issuer("5343 4123 1435 1231 2")

    with pytest.raises(ValueError):
        get_issuer("4343 4123 1435 123")
    with pytest.raises(ValueError):
        get_issuer("5343 4123 1435 123")
    with pytest.raises(ValueError):
        get_issuer("5143 4123 1435 12")





