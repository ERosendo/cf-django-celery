from __future__ import absolute_import, unicode_literals

from django.conf import settings
from celery import shared_task, Task
from .models import UserProfile


class BaseTaskWithRetry(Task):
    autoretry_for = (Exception,)
    max_retries = settings.CELERY_TASK_MAX_RETRIES
    retry_backoff = True
    retry_backoff_max = 700
    retry_jitter = False

@shared_task(base=BaseTaskWithRetry)
def create_superadmin(user_id):
    if UserProfile.objects.filter(id=user_id).exists():
        user = UserProfile.objects.get(id = user_id)
        user.trx = 1
        user.save()
    
    return user_id