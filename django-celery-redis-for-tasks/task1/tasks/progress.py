from time import sleep

from celery import Celery, shared_task
from celery_progress.backend import ProgressRecorder
from config.celery import app


@shared_task(bind=True)
def django_progress(self, duration):
    progress_recorder = ProgressRecorder(self)
    for i in range(100):
        sleep(duration)
        progress_recorder.set_progress(i + 1, 100, f"On iteration {i}")
    return "Done"
