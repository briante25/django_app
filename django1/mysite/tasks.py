# mysite/tasks.py

from celery import shared_task
from datetime import datetime

@shared_task
def my_celery_task():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Celery task executed at {current_time}")
