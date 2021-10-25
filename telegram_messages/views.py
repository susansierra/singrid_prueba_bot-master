import requests
import json
from rest_framework import response, status
from rest_framework.decorators import api_view

import environ

env = environ.Env()
environ.Env.read_env()

TELEGRAM_URL = 'https://api.telegram.org/bot'
SINGRID_PRUEBA = env('SINGRID_PRUEBA_TOKEN')



def getUpdates():
    """Get Updates Telegram.
    Este metodo permite la utilizacion del comando getUpdates de telegram
    el cual permite acceder a la información del chat.

    Al final el objeto devuelto es de tipo object pero se necesita ser transformado a str
    con el fin de ser utilizado en el siguiente método

    """
    get_update = f'{TELEGRAM_URL}{SINGRID_PRUEBA}' + '/getUpdates'
    content = requests.get(get_update).content.decode("utf8")
    js = json.loads(content)
    return js

def getLastChatIdText(updates):
    """Metodo opcional para tomar el ultimo chat con el cual el bot interactuó."""
    num_updates = len(updates['result'])
    last_update = num_updates-1
    chat_id = updates['result'][last_update]['message']['chat']['id']
    return chat_id

@api_view(['GET'])
def sendMessageToEveryOne(request):
    """Método de envio colectivo.

        Este método permite enviar un mensaje a todos los que se han suscrito al bot,
        accediendo al resultado tomado de los updates para tomar el chat_id de cada persona.
        El mensaje enviado es un mensaje por igual a todos.

    """
    updates = getUpdates()
    for chat in range(0,len(updates)):
        chat_id = updates['result'][chat]['message']['chat']['id']
        bot_message = "Buenos dias, te espero en la reunión 8:00 AM"
        send_text = f'{TELEGRAM_URL}{SINGRID_PRUEBA}' + f'/sendMessage?chat_id={chat_id}' + f'&text={bot_message}'
        respuesta = requests.get(send_text).content.decode("utf8")
        js = json.loads(respuesta)
    return response.Response(js, status=status.HTTP_200_OK)

@api_view(['GET'])
def sendMessage(request):
    """Método de envío personal.

    Este método permite enviar un mensaje a una persona, siempre y cuando se proporcione su id.
    No su número telefónico ya que el bot y telegram no permiten el acceso a información personal
    del usuario.

    """
    id = '568554618'
    chat_id = id
    bot_message = "Buenos dias, te espero Roberth en la reunión 8:00 AM"
    send_text = f'{TELEGRAM_URL}{SINGRID_PRUEBA}' + f'/sendMessage?chat_id={chat_id}' + f'&text={bot_message}'
    respuesta = requests.get(send_text).content.decode("utf8")
    js = json.loads(respuesta)
    return response.Response(js, status=status.HTTP_200_OK)