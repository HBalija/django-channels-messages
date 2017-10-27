# Django channels messages


### Quickstart

Before starting, make sure you have Redis server installed.

Create Python3 virtual environment:

    mkvirtualenv --python=/usr/bin/python3 messages

Get the source from GitHub:

    git clone git@github.com:HBalija/django-channels-messages.git

Navigate to the project directory:

    cd django-channels-messages

Create `.env` file and define environment variables
showed in `env.sample`.

Initial setup:

    make update

Create super user:

    python manage.py createsuperuser

Run development server:

    make run

Point your browser to:

    127.0.0.1:8000

### Testing

Run tests:

    make test

Run tests with coverage:

    make coverage

### Content

HTML templates should go to `/templates/`. Static assets should go to `/static/`.
