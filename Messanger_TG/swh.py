# set_web_hook
import os

import requests
from dotenv import load_dotenv # для хранения переменных окружения

load_dotenv()
TG_API = os.getenv("BOT_API_KEY") # token to @fastapi_msg_bot

whook = '748b37b92ef4e5.lhr.life'

r = requests.get(f'https://api.telegram.org/bot{TG_API}/setWebhook?url=https://{whook}/')

print(r.json())