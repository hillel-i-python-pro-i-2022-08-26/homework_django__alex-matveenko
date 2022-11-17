import logging
from typing import Callable

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

from middlewares.models import SessionHandler


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

        session_handler = SessionHandler.objects.filter(session_key=session_key)

        user_session_query = [session_key.get('session_key') for session_key in session_handler.values()]
        user_path_query = [path.get('path') for path in session_handler.values()]

        if session_key in user_session_query and request.path in user_path_query:
            user_session = SessionHandler.objects.get(
                session_key=session_key,
                path=request.path,
            )
            count_of_visits = user_session.count_of_visits
        else:
            user_session = SessionHandler()
            count_of_visits = 0

        if request.user.is_authenticated:
            user_session.user = request.user
        user_session.path = request.path
        user_session.session_key = session_key

        count_of_visits += 1
        session['count'] = count_of_visits
        user_session.count_of_visits = session['count']

        user_session.save()

        return response
