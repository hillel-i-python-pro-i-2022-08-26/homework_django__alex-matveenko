from rest_framework import routers
from django.urls import path

from . import views
from .views import ContactCreateApi, ContactUpdateApi, ContactDeleteApi, ContactViewApi

router = routers.DefaultRouter()
router.register(r'contacts', views.ContactViewSet)

urlpatterns = [
    path('create/', ContactCreateApi.as_view()),
    path('update/<int:pk>/', ContactUpdateApi.as_view()),
    path('show/<int:pk>/', ContactViewApi.as_view()),
    path('delete/<int:pk>/', ContactDeleteApi.as_view()),

]
