import os

import celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DuolingoFree.settings")

app = celery.Celery("DuolingoFree")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
