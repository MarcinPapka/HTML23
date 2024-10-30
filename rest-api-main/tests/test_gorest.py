from faker import Faker
from src.gorest_handler import GoRESTHandler

gorest_handler = GoRESTHandler()


def test_from_create_to_delete_user():
    user_data = {
        "name": "Ross Geller",
        "gender": "male",
        "email": Faker().email(),
        "status": "active"
    }
    body = gorest_handler.create_user(user_data).json()
    assert "id" in body
    user_id = body["id"]

    body = gorest_handler.get_user_by_id(user_id).json()
    assert body["email"] == user_data["email"]
    assert body["name"] == user_data["name"]
    print(body)

    user_data_2 = {
        "name": Faker().name(),
        "gender": "male",
        "email": Faker().email(),
        "status": "active"
    }
    user_id = body["id"]

    body = gorest_handler.update_user(user_id, user_data_2).json()
    assert body["email"] == user_data_2["email"]
    assert body["name"] == user_data_2["name"]
    print(body)
    response = gorest_handler.delete_user(user_id)
    assert response.status_code == 204



