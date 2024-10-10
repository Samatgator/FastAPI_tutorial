from fastapi import FastAPI, Request
import requests
import uvicorn
import aiohttp
import os

from dotenv import load_dotenv
from schemas import Answer

load_dotenv()
TG_API = os.getenv("BOT_API_KEY")
MY_ID = os.getenv("MY_CHAT_ID")
ARINA = os.getenv("ARINA")


app = FastAPI()

# endpoint
@app.post("/answer")
async def answer(chat_id: int, text: str):
    data = {
        'chat_id': chat_id,
        'text': text
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(f'https://api.telegram.org/bot{TG_API}/sendMessage', data = data) as response:
            return response.status

# @app.post("/")
# async def root(request: Request):
#     result = await request.json()
#     print(result)


@app.post("/")
async def root(obj: Answer): # fastapi требует указать тип данных

    # передавая класс fastapi с помощью pydentic создает автоматическую
    # документацию в swagger

    # request: Request
    # result = await request.json() # await передает сигнал другим функциям для начала работы, не останавливаясь на текущей функции
    # obj = Answer.model_validate(result) # конвертация json в py obj
    # print(obj.message.text)
    
    # f_text = f'user: {obj.message.from_tg.chat_id}\n{obj.message.from_tg.first_name}\nwrites: {obj.message.text}'
    
    print(obj.model_dump_json())

    if obj.message.from_tg.chat_id == int(MY_ID):
        if obj.message.reply_to_message is not None:
            data = {
                'chat_id': obj.message.reply_to_message.forward_from.chat_id, # зависит от настройки персонализации перессылок
                'from_chat_id': obj.message.from_tg.chat_id,
                'message_id': obj.message.message_id
            }

            async with aiohttp.ClientSession() as session:
                async with session.post(f'https://api.telegram.org/bot{TG_API}/copyMessage', data = data) as response:
                    print(response.status)
    else:
        data = {
            'chat_id': MY_ID,
            'from_chat_id': obj.message.from_tg.chat_id,
            'message_id': obj.message.message_id
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(f'https://api.telegram.org/bot{TG_API}/forwardMessage', data = data) as response:
                print(response.status)


    return {"status": "ok!"}


# осуществляем запуск через localhost.run (нужен https)
# $ ssh -R 80:localhost:8000 nokey@localhost.run

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)