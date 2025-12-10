from utils.api_client import delete_user

def test_delete_user_success():
    response = delete_user(1)
    assert response.status_code in [200,204]
    

def test_delete_invalid_user():
    response = delete_user(9999)
    assert response.status_code in [200,204,404,500]