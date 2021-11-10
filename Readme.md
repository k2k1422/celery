# Celery


### start celery by default
```
celery -A tasks worker --loglevel=INFO
```

### start celery by name(1@%host)
```
celery -A tasks worker --loglevel=INFO -n worker1@%h
```