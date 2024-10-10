from pydantic import BaseModel, Field

# так выглядит сообщение отправленное боту

d = {
    'update_id': 286151577, 
    'message': {
        'message_id': 5, 
        'from': {
            'id': 788107265,
            'is_bot': False,
            'first_name': 'Samat',
            'last_name': 'Gatin',
            'username': 'janebeul',
            'language_code': 'en'
            },
        'chat': {
            'id': 788107265,
            'first_name': 'Samat',
            'last_name': 'Gatin',
            'username': 'janebeul',
            'type': 'private'
            },
        'date': 1728333159,
        'text': '345'
    }
}

# sticker
# sticker = {
#     'update_id': 286151632,
#     'message': {
#         'message_id': 104,
#         'from': {
#             'id': 788107265,
#             'is_bot': False,
#             'first_name': 'Samat',
#             'last_name': 'Gatin',
#             'username': 'janebeul',
#             'language_code': 'en'
#         }, 
#         'chat': {
#             'id': 788107265,
#             'first_name': 'Samat',
#             'last_name': 'Gatin',
#             'username': 'janebeul',
#             'type': 'private'
#         },
#         'date': 1728578757, 
#         'sticker': {
#             'width': 512,
#             'height': 512,
#             'emoji': '🙅\u200d♂️',
#             'set_name': 'kekisy4',
#             'is_animated': False,
#             'is_video': True,
#             'type': 'regular',
#             'thumbnail': {
#                 'file_id': 'AAMCAgADGQEAA2hnCATFs9ujlxx4OAXgAfQKcncxBAACoRcAAnXQEUg9dsbsk6NIpAEAB20AAzYE',
#                 'file_unique_id': 'AQADoRcAAnXQEUhy',
#                 'file_size': 15438,
#                 'width': 320, 
#                 'height': 320
#             },
#             'thumb': {
#                 'file_id': 'AAMCAgADGQEAA2hnCATFs9ujlxx4OAXgAfQKcncxBAACoRcAAnXQEUg9dsbsk6NIpAEAB20AAzYE',
#                 'file_unique_id': 'AQADoRcAAnXQEUhy',
#                 'file_size': 15438,
#                 'width': 320,
#                 'height': 320
#             },
#             'file_id': 'CAACAgIAAxkBAANoZwgExbPbo5cceDgF4AH0CnJ3MQQAAqEXAAJ10BFIPXbG7JOjSKQ2BA',
#             'file_unique_id': 'AgADoRcAAnXQEUg',
#             'file_size': 62270
#         }
#     }
# }


# photo
# photo = {
#     'update_id': 286151630,
#     'message': {
#         'message_id': 102, 
#         'from': {
#             'id': 788107265,
#             'is_bot': False,
#             'first_name': 'Samat',
#             'last_name': 'Gatin',
#             'username': 'janebeul',
#             'language_code': 'en'
#             },
#         'chat': {
#             'id': 788107265,
#             'first_name': 'Samat',
#             'last_name': 'Gatin',
#             'username': 'janebeul',
#             'type': 'private'
#             },
#         'date': 1728578300,
#         'photo': [
#             {'file_id': 'AgACAgIAAxkBAANmZwgC_BmO0M_cx8p8x6gVMg1W6JQAAiPjMRuz-EFIjSfKoWqRoxoBAAMCAANzAAM2BA',
#              'file_unique_id': 'AQADI-MxG7P4QUh4',
#              'file_size': 1013,
#              'width': 90,
#              'height': 51},
#             {'file_id': 'AgACAgIAAxkBAANmZwgC_BmO0M_cx8p8x6gVMg1W6JQAAiPjMRuz-EFIjSfKoWqRoxoBAAMCAANtAAM2BA',
#              'file_unique_id': 'AQADI-MxG7P4QUhy',
#              'file_size': 20529,
#              'width': 320,
#              'height': 180}, 
#             {'file_id': 'AgACAgIAAxkBAANmZwgC_BmO0M_cx8p8x6gVMg1W6JQAAiPjMRuz-EFIjSfKoWqRoxoBAAMCAAN4AAM2BA',
#             'file_unique_id': 'AQADI-MxG7P4QUh9',
#             'file_size': 34973,
#             'width': 480,
#             'height': 270}
#         ]
#    }
#}

# reply_to_message = {
#     'update_id': 286151645,
#     'message': {
#         'message_id': 120,
#         'from': {
#             'id': 788107265,
#             'is_bot': False,
#             'first_name': 'Samat',
#             'last_name': 'Gatin',
#             'username': 'janebeul',
#             'language_code': 'en'
#         },
#         'chat': {
#             'id': 788107265,
#             'first_name': 'Samat',
#             'last_name': 'Gatin',
#             'username': 'janebeul',
#             'type': 'private'
#         }, 
#         'date': 1728584131, 
#         'reply_to_message': {
#             'message_id': 112, 
#             'from': {
#                 'id': 7553021437, 
#                 'is_bot': True, 
#                 'first_name': 
#                 'fastapi_msg_bot',
#                 'username': 'fastapi_msg_bot'
#             }, 
#             'chat': {
#                 'id': 788107265,
#                 'first_name': 'Samat',
#                 'last_name': 'Gatin',
#                 'username': 'janebeul',
#                 'type': 'private'
#             },
#             'date': 1728582185,
#             'forward_origin': {
#                 'type': 'user',
#                 'sender_user': {
#                     'id': 788107265,
#                     'is_bot': False,
#                     'first_name': 'Samat',
#                     'last_name': 'Gatin', 
#                     'username': 'janebeul',
#                     'language_code': 'en'
#                 }, 
#                 'date': 1728582183
#             },
#             'forward_from': {
#                 'id': 788107265,
#                 'is_bot': False,
#                 'first_name': 'Samat',
#                 'last_name': 'Gatin',
#                 'username': 'janebeul',
#                 'language_code': 'en'
#             },
#             'forward_date': 1728582183,
#             'text': '123'
#         },
#         'text': '124'
#     }
# }




class FromTG(BaseModel):
    chat_id: int = Field(alias='id')
    is_bot: bool
    first_name: str
    last_name: str = None # set a defaul value
    username: str = None
    language_code: str = None

class Photo(BaseModel):
    file_id: str
    file_unique_id: str
    file_size: int
    width: int
    height: int


class Chat(BaseModel):
    chat_id: int = Field(alias='id')
    first_name: str
    last_name: str = None # set a defaul value
    username: str = None
    chat_type: str = Field(alias='type')

class ReplayMessage(BaseModel):
    message_id: int
    from_tg: FromTG = Field(alias='from') # замена поля отправителя
    chat: Chat
    date: int
    text: str = None
    sticker: str = None
    photo: list[Photo] = None
    caption: str = None
    forward_from: FromTG = None
    forward_origin: dict = None
    forward_date: int = None


class Message(BaseModel):
    message_id: int
    from_tg: FromTG = Field(alias='from') # замена поля отправителя
    chat: Chat
    date: int
    text: str = None
    sticker: str = None
    photo: list[Photo] = None
    caption: str = None
    reply_to_message: ReplayMessage = None

class Answer(BaseModel): # зачем это делать?
    update_id: int
    message: Message


# obj = Answer.model_validate(reply_to_message) # parse_obj is depricated
# print(obj.message.reply_to_message.forward_from.chat_id)
# print(obj.message.from_tg)