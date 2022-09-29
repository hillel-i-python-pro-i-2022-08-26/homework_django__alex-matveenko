from django.http import HttpResponse, HttpRequest

from core.services.generate_name import generate_name


def greetings(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f'Hello, {generate_name()}!')


def self_greetings(request: HttpRequest, name: str) -> HttpResponse:
    return HttpResponse(f'Hello, {name.title()}!')
