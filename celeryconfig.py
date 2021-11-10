broker_url = 'redis://:docker@192.168.1.5:6379/0'
result_backend = 'redis://:docker@192.168.1.5:6379/1'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Asia/Kolkata'
enable_utc = True