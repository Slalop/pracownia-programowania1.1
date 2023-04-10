from flask import Flask
import pytest
from ItemCreationRestriction import check_price
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_limit_price():
    mini_price = 50
    maxi_price = 200

    assert check_price(60, mini_price, maxi_price) == 60
    assert check_price(300, mini_price, maxi_price) == 200
    assert check_price(9, mini_price, maxi_price) == 50