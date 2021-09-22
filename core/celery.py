from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
import ssl

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('engine')

app.conf.broker_use_ssl = {
  'cert_reqs': ssl.CERT_NONE
}

 
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()