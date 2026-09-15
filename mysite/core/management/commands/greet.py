from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Says hello to someone'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)

    def handle(self, *args, **options):
        name = options['name']
        self.stdout.write(f'Hello, {name}!')
