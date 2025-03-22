import requests

URL = "http://google.com"
PARAMS = {}

r = requests.get(url=URL, params=PARAMS)

print(r)