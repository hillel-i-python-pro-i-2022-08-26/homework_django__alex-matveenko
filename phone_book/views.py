from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from phone_book.models import Contact


def show_contacts(request: HttpRequest) -> HttpResponse:
    contacts = Contact.objects.all()
    return render(
        request,
        "phone_book/index.html",
        {
            "title": "Phone Book",
            "contacts": contacts,
        },
    )
