

from django.db import models
from django.db.models import Q
from core.models import BaseModel
from .validators import validate_phone_number
# Create your models here.



class Newsletter(BaseModel):

    name = models.CharField(max_length=128)
    body = models.TextField()
    filter = models.CharField(max_length=256, blank=True)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    started = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
        
    @property
    def pending_messages(self):
        """
            Return pending messages queryet
        """

        return self.messages.filter(status = Message.PENDING)

    @property
    def sent_messages(self):
        """
            Return sent messages queryset
        """
        return self.messages.filter(status = Message.SENT)
    
    @property
    def pending(self):
        """
            Return pending messages count
        """
        return self.messages.filter(status = Message.PENDING).count()

    @property
    def sent(self):
        """
            Return sent messages count
        """
        return self.messages.filter(status = Message.SENT).count()

    def matched_clients(self):

        """
            Filter down clients that match the newsletter filter
        """
        filter_set = set(self.filter.split())
        lookups = Q(phone_number__in=filter_set) | Q(operator_code__in = filter_set) | Q(tag__in =filter_set)
        return Client.objects.filter(lookups)

    def complete_percentage(self):
        sent = self.sent
        total = self.messages.count()
        try:
            return (sent/total)*100
        except ZeroDivisionError:
            return 0

class Client(BaseModel):

    phone_number = models.CharField(max_length=11, unique=True, validators=[validate_phone_number])
    operator_code = models.CharField(max_length=16)
    tag = models.CharField(max_length=128,blank=True)
    time_zone = models.CharField(max_length=4, default='UTC')

    def __str__(self) -> str:
        return self.phone_number


class Message(BaseModel):


    SENT = 'SENT'
    PENDING = 'PENDING'

    STATUS_CHOICES = (
        (SENT,'Sent'),
        (PENDING,'Pending'),
    )
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default=PENDING)
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, related_name='messages')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='messages')


    def __str__(self) -> str:
        return f'{self.newsletter}->{self.client}'