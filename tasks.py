from celery import Celery
import time
from dotenv import load_dotenv

load_dotenv()

app = Celery()
app.config_from_object('celeryconfig')

@app.task
def add(x, y):
    # time.sleep(10)
    return x + y

@app.task
def multi(x, y):
    # time.sleep(10)
    return x + y