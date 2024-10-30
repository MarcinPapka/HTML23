import requests


class GoRESTHandler:
    base_url = "https://gorest.co.in/public/v2"
    users_endpoint = "/users"

    headers = {
        "Authorization": "Bearer 63832609ce8a25b0100e44c52f08547530d9ae3c798bd88571d1d7beeb35311b"
    }

    def create_user(self, user_data):
        response = requests.post(self.base_url + self.users_endpoint, json=user_data, headers=self.headers)
        assert response.status_code == 201
        return response

    def get_user_by_id(self, user_id):
        response = requests.get(f"{self.base_url}{self.users_endpoint}/{user_id}", headers=self.headers)
        assert response.status_code == 200
        return response

    def update_user(self, user_id, user_data_2):
        response = requests.put(f"{self.base_url}{self.users_endpoint}/{user_id}", json=user_data_2, headers=self.headers)
        return response

    def delete_user(self, user_id):
        response = requests.delete(f"{self.base_url}{self.users_endpoint}/{user_id}", headers=self.headers)
        return response