import logging

from django.core.management import BaseCommand, CommandParser

from phone_book import models


class Command(BaseCommand):
    help = 'Delete amount of users info'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("django")

    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            '--all',
            help="Delete ALL users",
            action='store_true',
        )
        parser.add_argument(
            '--duplicate',
            action='store_true',
            help='Delete duplicates',
        )

    def handle(self, *args, **options):
        amount_of_user_info = models.Contacts.objects.all().count()
        self.logger.info(f"Now amount of users is: {amount_of_user_info}")

        if options['all']:
            all_info = models.Contacts.objects.all()
            answer = input('You try to delete ALL users, are you sure? Y/n \n')
            if answer == 'Y':
                all_info.delete()

        if options['duplicate']:
            unique_contact = set()
            count_duplicates = 1

            contacts = models.Contacts.objects.all()

            for contact in contacts:
                if contact.name in unique_contact:
                    self.logger.info(f"Duplicate deleted {count_duplicates}")
                    count_duplicates += 1
                    contact.delete()
                unique_contact.add(contact.name)

        db_query = models.Contacts.objects.filter(is_auto_generated=True)
        db_query.delete()

        number_after_deleting = models.Contacts.objects.all().count()
        deleted_amount_of_users = amount_of_user_info - number_after_deleting

        self.logger.info(f"Delete {deleted_amount_of_users} of users info.")

        number_after_deleting = models.Contacts.objects.all().count()
        self.logger.info(f"Current amount of users info is: {number_after_deleting}")
