from flask import Flask
import pytest
from restrictions import limit_price
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_limit_price():
    old_price = 100
    min_price = 50
    max_price = 200

    # testowanie poprawnej zmiany ceny
    assert limit_price(120, old_price, min_price, max_price) == 120

    # testowanie cena nie może zmaleć o więcej niż 60%
    assert limit_price(39, old_price, min_price, max_price) == old_price

    # testowanie cena nie może wzrosnąć o więcej niż 60%
    assert limit_price(199, old_price, min_price, max_price) == old_price

    # testowanie zmiany ceny poniżej wartości minimalnej
    assert limit_price(40, old_price, min_price, max_price) == old_price

    # testowanie zmiany ceny powyżej wartości maksymalnej
    assert limit_price(300, old_price, min_price, max_price) == old_price

