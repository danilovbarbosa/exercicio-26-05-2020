#!/bin/bash
# bash -f ./scripts/run.sh

python manage.py showmigrations

python manage.py makemigrations

python manage.py migrate

python manage.py runserver 0.0.0.0:8000