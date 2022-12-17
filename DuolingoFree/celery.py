import os

import celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DuolingoFree.settings")

app = celery.Celery(
    "DuolingoFree",
    broker="redis://redis:6379",
    backend="redis://redis:6379",
)

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "restart_tasks_with_errors": {
        "task": "backend.tasks.restart_tasks_with_errors",
        "schedule": crontab(minute="*/60"),
    }
}
