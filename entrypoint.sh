#!/bin/bash
python manage.py livereload&
# sleep infinity
python manage.py runserver 0.0.0.0:8000
# Execute the main command (passed as CMD in Dockerfile)
exec "$@"
