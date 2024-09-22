import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_redis_celery.settings')

app = Celery('django_redis_celery')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

