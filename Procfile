release: python manage.py makemigrations && python manage.py migrate && python manage.py createsuperuser --no-input
web: gunicorn core.wsgi

