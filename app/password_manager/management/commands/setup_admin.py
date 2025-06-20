from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import transaction

class Command(BaseCommand):
    help = 'Creates a superuser'

    def handle(self, *args, **kwargs):
        try:
            with transaction.atomic():
                if not User.objects.filter(username='admin').exists():
                    User.objects.create_superuser(
                        username='admin',
                        email='admin@example.com',
                        password='admin123'
                    )
                    self.stdout.write(self.style.SUCCESS('Superuser created successfully!'))
                else:
                    self.stdout.write(self.style.WARNING('Superuser already exists.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating superuser: {e}'))
