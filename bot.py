import requests
import os
import time
import datetime
from config import Config
from termcolor import colored

# Make URL
def get_url(action, **params):
    API_TOKEN = os.environ.get('API_TOKEN')
    url = Config.API_URL + action + '?access_token=' + API_TOKEN
    if params:
        for key, value in params.items():
            url = url + '&' + key + '=' + value
    return url

# Listener
while True:
    get_updates = requests.get(get_url('updates'))
    updates = get_updates.json()['updates']
    print(colored(datetime.datetime.now(), 'red'), colored('updates', 'green'), updates)
    if (updates):
        for update in updates:
            user_id = update['message']['sender']['user_id']
            post_message = requests.post(get_url('messages', user_id=str(user_id)), data='{"text":"Hello"}')
            print(colored(datetime.datetime.now(), 'red'), colored('message', 'yellow'), post_message.json()['message'])
    time.sleep(Config.LISTEN_INTERVAL)