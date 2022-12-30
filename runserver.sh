python manage.py collectstatic --no-input

python manage.py migrate

gunicorn --worker-temp-dir /dev/shm proiadmin.wsgi