from django.urls import path

from . import views

urlpatterns = [
    path("subscribe/", views.subscribe, name="subscribe"),
    path("publish/", views.publish, name="publish"),
]
