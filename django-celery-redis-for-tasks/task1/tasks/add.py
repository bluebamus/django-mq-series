import time

from celery import Celery, shared_task
from config.celery import app


@shared_task()
def add(num1, num2):
    time.sleep(1)

    print("{} + {} = {}".format(num1, num2, num1 + num2))

    return num1 + num2


@app.task
def callback(results):
    return sum(results)
