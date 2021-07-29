import requests
import json

BASE_URL_FOR_PKCHECK = 'http://127.0.0.1:8000/restbhm/pkcheck/'

def isPKonly(pk):
    url = BASE_URL_FOR_PKCHECK + str(pk)
    response = requests.get(url)
    if response.status_code == 200:
        return True
    elif response.status_code == 201:
        return False
    else:
        return 404, "ERROR"