import os
import requests
import json

from celery import shared_task
from .models import Newsletter,Message,Client

TOKEN = os.environ.get('TOKEN')


@shared_task(bind=True, autoretry_for=(requests.RequestException,Exception),retry_backoff=60*2,retry_backoff_max=60*60,max_retries=5)
def send_message(self,newsletter_pk,client_pk):
    """
        Create and send message to client with newsletter body attribute
        Retry sending on any exception, 5 times with variable interval of time before given up
    """

    endpoint = 'https://probe.fbrq.cloud/v1/send/{id}'
    header = {
        'Authorization' : f'Bearer {TOKEN}'
    }
    newsletter = Newsletter.objects.get(pk = newsletter_pk)
    client = Client.objects.get(pk=client_pk)
    message,_ = Message.objects.get_or_create(client=client, newsletter=newsletter)

    # message to the endpoint
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
    else:
        raise Exception()


@shared_task
def distribute_newsletter(newsletter_pk):
    """
        Grab matched clients to the given newsletter and broadcast the message to them
    """
    newsletter = Newsletter.objects.get(pk = newsletter_pk)
    clients = newsletter.get_clients()
    for client in clients:
        succeeded = send_message.apply_async((newsletter_pk,client.pk))