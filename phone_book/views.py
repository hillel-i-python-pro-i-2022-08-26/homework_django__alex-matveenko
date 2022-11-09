from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, ListView, DeleteView, TemplateView

from phone_book.models import Contact


class ContactListView(ListView):
    model = Contact


class ContactCreateView(CreateView):
    model = Contact
    fields = ("name", "phone", "birthday_date", "avatar",)

    def get_success_url(self):
        return reverse_lazy('phone_book:user', kwargs={'pk': self.object.pk})


class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy('phone_book:index')


class ContactView(TemplateView):
    template_name = "phone_book/user.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contact = Contact.objects.get(pk=context["pk"])
        context['contact'] = contact
        context['title'] = f"Info {contact.name}."
        return context


class ContactUpdateView(UpdateView):
    model = Contact
    fields = ("name", "phone", "birthday_date", "avatar",)
    template_name_suffix = '_update_form'

    def get_success_url(self):
        contact_pk = self.kwargs['pk']
        return reverse_lazy('phone_book:user', kwargs={'pk': contact_pk})


def search_user_info(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "phone_book/user_search.html",
        {
            "title": "Search User",
        },
    )


def show_user_search(request: HttpRequest) -> HttpResponse:
    query = request.GET.get("q")

    if query.startswith("0"):
        contact = Contact.objects.get(phone=query)
    else:
        contact = Contact.objects.get(pk=query)
    return render(
        request,
        "phone_book/user_info.html",
        {
            "title": f"Info of user {contact.name}",
            "contact": contact,
        },
    )
