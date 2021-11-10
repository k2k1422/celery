

from celery import Celery
from tasks import add
celery = Celery()
celery.config_from_object('celeryconfig')
results = add.delay(2,3)

print(results.id)