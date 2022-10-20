from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from phone_book.models import Contacts


def show_contacts(request: HttpRequest) -> HttpResponse:
    contacts = Contacts.objects.all()
    return render(
        request,
        "phone_book/index.html",
        {
            "title": "Phone Book",
            "contacts": contacts,
        },
    )
