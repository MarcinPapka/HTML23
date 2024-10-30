from tests.gorest_handler import GoRESTHandler
from faker import Faker
import random

gorest_handler = GoRESTHandler()

user_data = {
    "name": "Ross Geller",
    "gender": "male",
    "email": Faker().email(),
    "status": "active"}
user_data1 = {
    "name": Faker().name(),
    "email": Faker().email(),
    "status": random.choice(["inactive"])
}


def test_from_create_to_delete_user():
    body = gorest_handler.create_user(user_data).json()
    user_id = body["id"]
    assert "id" in body
    assert body["email"] == user_data["email"]
    assert body["name"] == user_data["name"]

    body = gorest_handler.get_user(user_id).json()
    assert body["name"] == user_data["name"]
    assert body["email"] == user_data["email"]
    assert body["name"] == user_data["name"]

    body = gorest_handler.update_user(user_id, user_data1).json()
    assert body["name"] != user_data["name"]
    assert body["gender"] == user_data["gender"]
    assert body["email"] != user_data["email"]
    assert body["status"] != user_data["status"]

    body = gorest_handler.delete_user(user_id)




