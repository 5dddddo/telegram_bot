import requests
from decouple import config

api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id=config('CHAT_ID')
text = input('INPUT MSG : ')

requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
