import requests

base_url = "https://jsonplaceholder.typicode.com"

def create_user(payload):
    return requests.post(f"{base_url}/users", json = payload)


def get_user(user_id):
    return requests.get(f"{base_url}/users/{user_id}")


def update_user(user_id, payload):
    return requests.put(f"{base_url}/users/{user_id}", json=payload)


def delete_user(user_id):
    return requests.delete(f"{base_url}/users/{user_id}")