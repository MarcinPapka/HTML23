import requests


class PokeAPIHandler:
    base_url = "https://pokeapi.co/api/v2"
    pokemon_endpoint = "/pokemon"
    shape_endpoint = "/pokemon-shape"

    def get_list_of_pokemons(self, params):
        response = requests.get(self.base_url + self.pokemon_endpoint, params=params)
        assert response.status_code == 200
        return response

    def get_shapes_of_pokemons(self, name=""):
        response = requests.get(f"{self.base_url}{self.shape_endpoint}/{name}")
        assert response.status_code == 200
        return response
