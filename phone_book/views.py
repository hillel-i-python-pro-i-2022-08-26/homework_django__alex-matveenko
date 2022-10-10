from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from phone_book.forms import AddUserForm
from phone_book.models import PhoneBook


def show_contacts(request: HttpRequest) -> HttpResponse:
    contacts = PhoneBook.objects.all()
    return render(
        request,
        "phone_book/index.html",
        {
            "title": "Phone Book",
            "contacts": contacts,
        },
    )


def add_user(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("phone_book:index")
    else:
        form = AddUserForm()
    return render(request, "phone_book/add_user.html", {"title": "Add User", "form": form})


def search_user_info(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "phone_book/user_search.html",
        {
            "title": "Search User",
        },
    )


def show_user_info(request: HttpRequest) -> HttpResponse:
    query = request.GET.get("q")

    if query.startswith("0"):
        user = PhoneBook.objects.get(phone=query)
    else:
        user = PhoneBook.objects.get(pk=query)
    return render(
        request,
        "phone_book/user_info.html",
        {
            "title": f"Info of user {user.name}",
            "user": user,
        },
    )
