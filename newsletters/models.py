from datetime import datetime,timedelta

from django.utils import timezone
from django.db import models

from core.models import BaseModel
from .validators import validate_phone_number
# Create your models here.



class Newsletter(BaseModel):

    name = models.CharField(max_length=128)
    body = models.TextField()
    filter = models.CharField(max_length=256, blank=True)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()


    def __str__(self) -> str:
        return self.name

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
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f'{self.newsletter}->{self.client}'