import os

import celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DuolingoFree.settings")

app = celery.Celery(
    "DuolingoFree",
    broker="redis://redis:6379",
    backend="redis://redis:6379",
)

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
