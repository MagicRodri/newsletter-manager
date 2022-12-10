from datetime import datetime

from django.db.models.signals import post_save
from .models import Newsletter
from django.utils import timezone

from .tasks import distribute_newsletter


def post_newsletter_save(instance,created,*args, **kwargs):

    if created:
        start = instance.start_at
        end = instance.end_at
        if timezone.now() < start:
            distribute_newsletter.apply_async((instance.pk,), eta = start, expires=end)

        elif start <= timezone.now() < end : 
            distribute_newsletter.apply_async((instance.pk,), expires=end)


post_save.connect(post_newsletter_save, sender=Newsletter)
