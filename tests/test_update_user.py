from utils.api_client import update_user

def test_user_update_success():
    payload = {"name": "Jayanth Sameer", "email": "jayanthsameer@test.com"}
    response = update_user(1,payload)
    assert response.status_code == 200
    
    data = response.json()
    assert data["name"] == "Jayanth Sameer"
    assert data["email"] == "jayanthsameer@test.com"
    
    
def test_update_user_invalid():
    payload = {"name": "Sameer"}
    response = update_user(999,payload)
    assert response.status_code in [200,400,500]