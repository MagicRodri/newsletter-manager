import os
import requests
import json

from celery import shared_task
from .models import Newsletter,Message,Client

TOKEN = os.environ.get('TOKEN')

@shared_task
def add(a,b):
    return a+b

@shared_task
def send_message(newsletter_pk,client_pk):

    endpoint = 'https://probe.fbrq.cloud/v1/send/{id}'
    header = {
        'Authorization' : f'Bearer {TOKEN}'
    }
    newsletter = Newsletter.objects.get(pk = newsletter_pk)
    client = Client.objects.get(pk=client_pk)
    message = Message.objects.create(client=client, newsletter=newsletter)
    msg = {
        'id' : message.id ,
        'phone':int(client.phone_number),
        'text': newsletter.body
    }
    endpoint = endpoint.format(id=message.id)
    msg_json = json.dumps(msg)

    response = requests.post(endpoint, data=msg_json, headers=header)
    if response.ok:
        message.status = message.SENT
        message.save()
        return True

    return False

@shared_task
def distribute_newsletter(newsletter_pk):
    """
    """
    newsletter = Newsletter.objects.get(pk = newsletter_pk)
    clients = newsletter.get_clients()
    for client in clients:
        send_message.delay(newsletter_pk,client.pk)