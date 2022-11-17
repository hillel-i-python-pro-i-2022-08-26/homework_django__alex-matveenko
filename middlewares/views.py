from django.db.models import Count, Sum
from django.views.generic import TemplateView, ListView

from middlewares.models import SessionHandler


class MiddlewareView(TemplateView):
    template_name = "middlewares/main_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Middleware"
        return context


class AllInfoViews(ListView):
    model = SessionHandler
    template_name = "middlewares/sessions_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "All session info"
        # Get_useful_info__start
        session_handler = SessionHandler.objects.all()
        total_visits = session_handler.aggregate(Sum('count_of_visits'))
        total_pages = session_handler.aggregate(Count('path'))
        # Get_useful_info__stop
        context['object_list'] = session_handler
        context['total_visits'] = total_visits["count_of_visits__sum"]
        context['count_of_visited_pages'] = total_pages["path__count"]
        return context


class CurrentSessionInfoViews(ListView):
    model = SessionHandler
    template_name = "middlewares/current_sessions_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Current session info"
        # Get_useful_info__start
        session_handler = SessionHandler.objects.filter(session_key=self.kwargs['session_key'])
        total_visits = session_handler.aggregate(Sum('count_of_visits'))
        total_pages = session_handler.aggregate(Count('path'))
        # Get_useful_info__stop
        context['object_list'] = session_handler
        context['total_visits'] = total_visits["count_of_visits__sum"]
        context['count_of_visited_pages'] = total_pages["path__count"]
        return context


class CurrentUserInfoViews(ListView):
    model = SessionHandler
    template_name = "middlewares/current_user_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Current user session info"
        # Get_useful_info__start
        session_handler = SessionHandler.objects.filter(user=self.kwargs['pk'])
        total_visits = session_handler.aggregate(Sum('count_of_visits'))
        total_pages = session_handler.aggregate(Count('path'))
        # Get_useful_info__stop
        context['object_list'] = session_handler
        context['object_list'] = session_handler
        context['total_visits'] = total_visits["count_of_visits__sum"]
        context['count_of_visited_pages'] = total_pages["path__count"]
        return context
