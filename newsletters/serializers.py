from rest_framework import serializers
from .models import Client, Newsletter, Message




class ClientSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):

        """
            The purpose of this is to be able to dynamically choose the fields to be rendered on instantiation without creating a seperate serializer
        """

        fields = kwargs.pop('fields', None)

        # Instantiation
        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Client
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):

        """
            The purpose of this is to be able to dynamically choose the fields to be rendered on instantiation without creating a seperate serializer
        """

        fields = kwargs.pop('fields', None)

        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    newsletter = serializers.ReadOnlyField(source = 'newsletter.name')
    client = serializers.ReadOnlyField(source = 'client.phone_number')

    class Meta:
        model = Message
        fields = ['id','newsletter','client','status']


class NewsletterSerializer(serializers.ModelSerializer):
    """
        Serializer to grab minimum informations about newsletter
    """
    
    class Meta:
        model = Newsletter
        fields = ['id','name','body','filter','complete_percentage','start_at','end_at']


class NewsletterFullSerializer(serializers.ModelSerializer):
    """
        Serializer to grab full statistics about newsletter
    """
    pending_messages = MessageSerializer(many=True, fields = ['id','client','status'], read_only = True)
    sent_messages = MessageSerializer(many=True, fields = ['id','client','status'],read_only = True)
    matched_clients = ClientSerializer(many=True, fields = ['phone_number'],read_only = True)

    class Meta:
        model = Newsletter
        fields = [
            'id',
            'name',
            'body',
            'filter',
            'matched_clients',
            'pending',
            'sent',
            'pending_messages',
            'sent_messages',
            'complete_percentage',
            'start_at',
            'end_at'
        ]