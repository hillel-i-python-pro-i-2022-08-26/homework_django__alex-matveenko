from django.http import HttpResponse, HttpRequest

from core.services.generate_name import generate_name


def greetings(request: HttpRequest, name: str = generate_name()) -> HttpResponse:
    return HttpResponse(f"Hello, {name.title()}!")
