# coding: utf8
import requests
import os
import time
import datetime
from config import Config
from termcolor import colored
from dialog import answers

# Make URL
def get_url(action, **params):
    API_TOKEN = os.environ.get('API_TOKEN')
    url = Config.API_URL + action + '?access_token=' + API_TOKEN
    if params:
        for key, value in params.items():
            url = url + '&' + key + '=' + value
    return url

# Send message
def send_message(user_id, text):
    data='{"text":"%(text)s"}'%{'text':text}
    post_message = requests.post(get_url('messages', user_id=str(user_id)), data)
    print(colored(datetime.datetime.now(), 'red'), colored('message', 'yellow'), post_message.content)

# Listener
while True:
    get_updates = requests.get(get_url('updates'))
    updates = get_updates.json()['updates']
    print(colored(datetime.datetime.now(), 'red'), colored('updates', 'green'), updates)
    if (updates):
        for update in updates:
            message = update['message']
            user_id = message['sender']['user_id']
            text = message['body']['text']
            try:
                answer_text = answers[text]
                send_message(user_id, answer_text)
            except:
                send_message(user_id, 'I am very stuped')
    time.sleep(Config.LISTEN_INTERVAL)