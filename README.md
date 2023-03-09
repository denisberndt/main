# Main
A part of react-crud app

## To start the App

In the project directory, run:

First startup Database
### `docker-compose up -d db`

After start entire app:
### `docker-compose up`


Optional:
### `docker-compose up --build`

## Useful comands to start the App:

To enter Docker:
### `docker-compose exec backend sh`

Flask db migration(react-crud):

### `python manage.py db init`
### `python manage.py db migrate`
### `python manage.py db upgrade`
