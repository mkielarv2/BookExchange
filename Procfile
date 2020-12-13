release: python manage.py migrate
release: DJANGO_SUPERUSER_PASSWORD=admin123
release: python manage.py createsuperuser --no-input --username=admin --email=admin@bookswapp.com
web: python manage.py runserver 0.0.0.0:$PORT