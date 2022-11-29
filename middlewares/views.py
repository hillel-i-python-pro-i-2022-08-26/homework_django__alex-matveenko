from django.views.generic import TemplateView, ListView

from middlewares.models import VisitHandler
from middlewares.services.aggregator import aggregator


class MiddlewareView(TemplateView):
    template_name = "middlewares/main_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Middleware"
        return context


class AllInfoViews(ListView):
    model = VisitHandler
    template_name = "middlewares/sessions_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "All session info"

        session_handler = VisitHandler.objects.all()

        context['object_list'] = session_handler
        context.update(aggregator(session_handler))
        return context


class CurrentSessionInfoViews(ListView):
    model = VisitHandler
    template_name = "middlewares/current_sessions_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Current session info"

        session_handler = VisitHandler.objects.filter(session_key=self.kwargs['session_key'])

        context['object_list'] = session_handler
        context.update(aggregator(session_handler))
        return context


class CurrentUserInfoViews(ListView):
    model = VisitHandler
    template_name = "middlewares/current_user_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Current user session info"

        session_handler = VisitHandler.objects.filter(user=self.kwargs['pk'])

        context['object_list'] = session_handler
        context.update(aggregator(session_handler))
        return context
