import requests

from .models import TeleSettings


def sendTelegram(name, email, order_phone):
    settings = TeleSettings.objects.get(pk=1)
    token = str(settings.tg_token)
    chat_id = str(settings.tg_chat)
    text = f'''Заявка с сайта:
    Имя:  {name},
    Email:  {email},
    Телефон:  {order_phone}'''

    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'





    req = requests.post(method, data={'chat_id': chat_id, 'text': text})

