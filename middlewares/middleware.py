import logging
from typing import Callable

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

from middlewares.models import VisitHandler


class LoggingMiddleware:
    def __init__(self, get_response: Callable):
        self.get_response = get_response
        self.logger = logging.getLogger('django')
        self.logger.info('Start')

    def __call__(self, request: WSGIRequest):

        # Get_user_session__start
        session = request.session
        if not session.session_key:
            session.save()
        session_key = session.session_key
        count_of_visits = session.get("count", 0)
        # Get_user_session__stop

        logger_message = f"Path:{request.path} - User:{request.user} - Session:{session_key}"

        # Get_response__start
        self.logger.info(f"Before - {logger_message}")
        response: HttpResponse = self.get_response(request)
        self.logger.info(f"After - {logger_message}")
        # Get_response__stop

        visit_handler = VisitHandler.objects.filter(session_key=session_key, path=request.path).first()

        if visit_handler is not None:
            user_visit = visit_handler
            count_of_visits = user_visit.count_of_visits
        else:
            user_visit = VisitHandler()
            count_of_visits = 0
            if request.user.is_authenticated:
                user_visit.user = request.user

            user_visit.path = request.path
            user_visit.session_key = session_key

        count_of_visits += 1
        session['count'] = count_of_visits
        user_visit.count_of_visits = session['count']

        user_visit.save()

        return response
