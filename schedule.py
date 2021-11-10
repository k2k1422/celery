from celery.schedules import crontab
from celery import Celery
app = Celery()
app.config_from_object('celeryconfig')


app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'add-every-monday-morning': {
        'task': 'tasks.add',
        'schedule': 2.0,
        'args': (16, 16),
    },
}
app.conf.timezone = 'UTC'