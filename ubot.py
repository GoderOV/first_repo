import requests
import time

api_url = 'https://api.telegram.org/bot'
bot_token = '7663613416:AAEfF5p5qJEf7wVapIGBZEvwBZN6QZzLeHw'
text = 'Super! Very fine update!!!'
max_counter = 100

offset = -2
counter = 0
chat_id: int

while counter < max_counter:
    
    print('attempt = ', counter) #Для показателя работы и жизни кодаа в консоли
    
    updates = requests.get( f'{api_url}{bot_token}/getUpdates?offset={offset + 1}').json()
    
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{api_url}{bot_token}/sendMessage?chat_id={chat_id}&text={text}')

    time.sleep(1)
    counter += 1