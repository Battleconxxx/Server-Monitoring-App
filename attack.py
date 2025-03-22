import requests
import multiprocessing

URL = "http://localhost:3000"

def req_sender():
    r = requests.get(url=URL)
    print(str(r))

while True:
    req_sender()