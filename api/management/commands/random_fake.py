from django.core.management.base import BaseCommand

from api.fake_data import AuthorFactory, BookFactory


class Command(BaseCommand):
    """
    Команда для заполнения базы рандомными данными.
    """

    help = 'Create random data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--omnis',
            default=20,
        )

    def handle(self, *args, **options):
        for _ in range(options['omnis']):
            AuthorFactory()
            BookFactory()
