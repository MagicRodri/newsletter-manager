from rest_framework import serializers
from .models import Client, Newsletter, Message


class NewsletterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Newsletter
        fields = ['name','body','filter','start_at','end_at']

class ClientSerializer(serializers.ModelSerializer):


    class Meta:
        model = Client
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['status']