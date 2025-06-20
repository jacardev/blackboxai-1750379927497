import webview
import threading
import sys
import os
import django
from django.core.management import execute_from_command_line
import time

def run_django():
    """Run the Django development server."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_password_manager.settings')
    django.setup()
    execute_from_command_line(['manage.py', 'runserver', '8000'])

def main():
    # Start Django server in a separate thread
    django_thread = threading.Thread(target=run_django, daemon=True)
    django_thread.start()

    # Wait for Django server to start
    time.sleep(2)

    # Create a desktop window
    webview.create_window(
        title='Gerenciador de Senhas',
        url='http://127.0.0.1:8000',
        width=1000,
        height=800,
        min_size=(800, 600)
    )
    
    # Start the desktop application
    webview.start()

if __name__ == '__main__':
    main()
