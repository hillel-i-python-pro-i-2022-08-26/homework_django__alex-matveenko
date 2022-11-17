import logging

from django.core.management import BaseCommand, CommandParser

from middlewares import models


class Command(BaseCommand):
    help = "Delete all session info"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("django")

    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            "-ds",
            "--delete_sessions",
            help="Delete ALL session info",
            action="store_true",
        )

    def handle(self, *args, **options):
        amount_of_session_info = models.SessionHandler.objects.all().count()
        self.logger.info(f"Now amount of sessions info is: {amount_of_session_info}")

        if options["delete_sessions"]:
            all_info = models.SessionHandler.objects.all()
            all_info.delete()

        number_after_deleting = models.SessionHandler.objects.all().count()
        deleted_amount_of_sessions_info = amount_of_session_info - number_after_deleting

        self.logger.info(f"Delete {deleted_amount_of_sessions_info} of sessions info.")

        number_after_deleting = models.SessionHandler.objects.all().count()
        self.logger.info(f"Current amount of users info is: {number_after_deleting}")
