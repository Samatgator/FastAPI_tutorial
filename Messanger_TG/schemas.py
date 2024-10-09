from pydantic import BaseModel, Field

# так выглядит сообщение отправленное боту

# d = {
#     'update_id': 286151577, 
#     'message': {
#         'message_id': 5, 
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
#         'date': 1728333159,
#         'text': '345'
#     }
# }

class FromTG(BaseModel):
    chat_id: int = Field(alias='id')
    is_bot: bool
    first_name: str
    last_name: str = None # set a defaul value
    username: str = None
    language_code: str


class Message(BaseModel):
    message_id: int
    from_tg: FromTG = Field(alias='from') # замена поля отправителя
    chat: dict 
    date: int
    text: str

class Answer(BaseModel): # зачем это делать?
    update_id: int
    message: Message


#obj = Answer.model_validate(d) # parse_obj is depricated
#print(obj.message.from_tg)