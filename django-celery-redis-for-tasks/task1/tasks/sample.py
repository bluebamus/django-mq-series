import random
import time

from celery import Celery, shared_task


@shared_task()
def working(id=1):
    # 1~5초 사이의 랜덤한 Delay를 발생.
    time.sleep(random.randint(1, 3))
    return "{}번째, 일을 끝냈다.".format(id)
