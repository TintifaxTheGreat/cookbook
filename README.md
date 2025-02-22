# Cookbook

A simple web-app to maintain recipes.

These components are used:

* Wagtail CMS (https://docs.wagtail.io)
    based on Django (https://www.djangoproject.com/)
* SQLite (https://www.sqlite.org/)
* Meilisearch (https://www.meilisearch.com/)

## Installation

Install requirements

```bash
pip install -r requirements.txt
```

Add Django secret and Meilisearch key to .env file.
```bash
SECRET_KEY = "YOUR_VALUE"
MEILI_MASTER_KEY = "YOUR_VALUE"
```

Migrate resources

```bash
python manage.py makemigrations
python manage.py migrate
```

Create an admin account

```bash
python manage.py createsuperuser
```

* * *

Collect static files

```bash
python manage.py collectstatic
```

Update search index

```bash
python manage.py update_index
```

Run the webserver (for development)

```bash
python manage.py runserver
```

