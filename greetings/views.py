from django.http import HttpResponse, HttpRequest

from core.services.generate_name import generate_name


def greetings(request: HttpRequest, name: str | None = None) -> HttpResponse:
    if name is None:
        name = generate_name()
    return HttpResponse(f'Hello, {name.title()}!')
