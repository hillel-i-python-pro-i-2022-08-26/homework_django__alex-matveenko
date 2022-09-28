from django.urls import path

from . import views

urlpatterns = [
    path("", views.greetings),
    path("<str:name>", views.greetings)
]
