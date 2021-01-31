#!/bin/sh
python manage.py migrate --noinput


if [ -x "$(command -v gunicorn)" ]; then
    gunicorn --bind 0.0.0.0:8000 wsgi
else
    echo "Gunicorn not installed: Using built-in server."
    python manage.py collectstatic --noinput
    watchmedo shell-command --patterns="*.css" -R -c "python manage.py collectstatic --noinput" &
    python manage.py runserver 0.0.0.0:8000
fi