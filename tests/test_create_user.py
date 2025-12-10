import pytest
from utils.api_client import create_user

def test_create_user_success():
    payload = {"name":"Jayanth", "email": "Jayanth@test.com"}
    response = create_user(payload)
    assert response.status_code == 201
    
    data = response.json()
    assert data["name"] == "Jayanth"
    assert data["email"] == "Jayanth@test.com"
    

def test_create_user_miss_email():
    payload = {"name": "Jayanth"}
    response = create_user(payload)
    assert response.status_code in [400,201]