from django.urls import path

from . import views

app_name = "phone_book"

urlpatterns = [
    path("", views.show_contacts, name="index"),
    path("add-user/", views.add_user, name="add_user"),
    path("search-user/", views.search_user_info, name="user_search"),
    path("vieaw-user/", views.show_user_info, name="user_info"),
]
