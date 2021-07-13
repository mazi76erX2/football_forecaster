from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Creates superuser'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str)
        parser.add_argument('--password', type=str)

    def handle(self, *args, **options):
        username = options['username']
        u = User(username=username)
        u.set_password(options['password'])
        u.is_superuser = True
        u.is_staff = True
        u.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully created superuser {username}'))
