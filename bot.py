import requests
import os
import time
from config import Config

def get_url(action):
    API_TOKEN = os.environ.get('API_TOKEN')
    url = Config.API_URL + action + '?access_token=' + API_TOKEN
    return url

while True:
    r = requests.get(get_url('updates'))
    print(r.text)
    time.sleep(0.5)