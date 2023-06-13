from __future__ import absolute_import, unicode_literals
import os
from celery import celery
import django.conf import settings


os.environ.setdefault('DJANGO_SETTING_MODULE', 'core.settings')

app = Celery('core')

app.conf.enable_utc = False 

app.conf.update(timezone= 'UTC')

app.config_from_object(settings, name='CELERY')

# celery Beat Setting 

app.autodiscover_task()

@app.task(bind=True)
def debug_task(self):
    print(f'request:, {self:request!r}')

