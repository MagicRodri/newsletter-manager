from django.shortcuts import render

from rest_framework import generics

from newsletters.models import Client, Newsletter, Message
from newsletters.serializers import (
    ClientSerializer,
    NewsletterSerializer,
    MessageSerializer,
    NewsletterFullSerializer
)
# Create your views here.


class NewsletterList(generics.ListCreateAPIView):

    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

class NewsletterDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Newsletter.objects.all()
    serializer_class = NewsletterFullSerializer

class ClientList(generics.ListCreateAPIView):
    
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MessageList(generics.ListAPIView):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageDetail(generics.RetrieveAPIView):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer