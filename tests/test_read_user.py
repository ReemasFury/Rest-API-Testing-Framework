from utils.api_client import get_user

def test_read_user_success():
    response = get_user(1)
    assert response.status_code == 200 
    
    data = response.json()
    assert "id" in data
    assert data["id"] == 1
    

def test_read_invalid_user():
    response = get_user(999)
    assert response.status_code in [200,204,404]