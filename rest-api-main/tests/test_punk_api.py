import requests


def test_default_beers():
    response = requests.get("https://api.punkapi.com/v2/beers")
    body = response.json()
    assert body[0]["id"] == 1
    assert body[-1]["id"] == 25
    assert len(body) == 25


def test_ids_range_11_to_20():
    params = {
        "ids": "11|12|13|14|15|16|17|18|19|20"
    }
    response = requests.get("https://api.punkapi.com/v2/beers", params=params)
    body = response.json()
    assert len(body) == 10

    beer_id = 11
    for beer in body:
        assert beer["id"] == beer_id
        beer_id += 1


def test_default_beers():
    response = requests.get("https://api.punkapi.com/v2/beers/123")
    body = response.json()
    assert body[0]["id"] == 123


def test_20_results_from_page5():
    response = requests.get("https://api.punkapi.com/v2/beers?page=5&per_page=20")
    body = response.json()
    assert body[1]
