from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import transaction

try:
    with transaction.atomic():
        superuser = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123'
        )
        print("Superuser created successfully!")
except Exception as e:
    print(f"Error creating superuser: {e}")
