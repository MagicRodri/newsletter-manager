from __future__ import absolute_import, unicode_literals

import os
from .settings import BASE_DIR
from celery import Celery
import dotenv


env_path = BASE_DIR / '.env'
dotenv.read_dotenv(env_path)

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))