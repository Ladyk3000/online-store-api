#!/bin/bash

echo "Waiting for database to start..."
while !</dev/tcp/db/5432; do
  sleep 1
done
echo "done"
echo

echo "PostgreSQL started"

echo "Making new database migrations..."
python manage.py makemigrations
echo "done"
echo

echo "Applying database migrations..."
python manage.py migrate
echo "done"
echo
python manage.py runserver 0.0.0.0:8000

exec "$@"