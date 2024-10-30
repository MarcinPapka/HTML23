import requests
from pokeapi_handler import PokeAPIHandler

pokeapi_handler = PokeAPIHandler()


def test_pokemon_api():
    response = requests.get("https://pokeapi.co/api/v2/pokemon")
    body = response.json()
    assert body["results"] != []


def test_status_code():
    response = requests.get("https://pokeapi.co/api/v2/pokemon")
    body = response.json()
    assert response.status_code == 200


def test_pokemon_number():
    response = requests.get("https://pokeapi.co/api/v2/pokemon")
    body = response.json()
    assert body['count'] == 1279


def test_response_time_under_1s():
    response = requests.get("https://pokeapi.co/api/v2/pokemon")
    assert response.elapsed.total_seconds() < 1
    print(response.elapsed.total_seconds())
    assert response.content.__sizeof__()
    print(response.content.__sizeof__())


def test_pagination():
    params = {
        "limit": 10,
        "offset": 20
    }
    response = pokeapi_handler.get_list_of_pokemons(params)
    body = response.json()

    assert len(body["results"]) == params["limit"]

    assert body["results"][0]["url"] == f"https://pokeapi.co/api/v2/pokemon/{params['offset'] + 1}/"
    assert body["results"][-1]["url"] == f"https://pokeapi.co/api/v2/pokemon/{params['offset'] + params['limit']}/"


def test_shapes():
    body = pokeapi_handler.get_shapes_of_pokemons().json()
    assert body["count"] == len(body["results"])

    pokemon_shape = body["results"][2]["name"]
    body = pokeapi_handler.get_shapes_of_pokemons(pokemon_shape).json()
    assert body["id"] == 3
