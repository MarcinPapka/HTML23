import pytest
import requests


response = requests.get("https://api.punkapi.com/v2/beers")
status_code = response.status_code
body = response.json()

print(status_code)
print(body)