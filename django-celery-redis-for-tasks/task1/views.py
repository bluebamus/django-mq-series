from django.shortcuts import render

from .tasks.progress import django_progress


def index(request):
    task = django_progress.delay(1)

    return render(request, "task1/index.html", {"task_id": task.task_id})
