#!/bin/bash

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi


echo "Making database migrations..."
python manage.py makemigrations
echo "done"
echo

echo "Applying database migrations..."
python manage.py migrate
echo "done"
echo
python manage.py runserver 0.0.0.0:8000

exec "$@"