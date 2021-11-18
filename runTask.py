

from celery import Celery
from tasks import add
celery = Celery()
celery.config_from_object('celeryconfig')
results = celery.send_task('tasks.add', (1,2))

print(results.id)