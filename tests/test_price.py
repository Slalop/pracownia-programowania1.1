from flask import Flask
import pytest
from restrictions import limit_price
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200

def test_limit_price():
    assert limit_price(50, 0, 100) == 50
    assert limit_price(150, 0, 100) == 100
    assert limit_price(-50, 0, 100) == 0

