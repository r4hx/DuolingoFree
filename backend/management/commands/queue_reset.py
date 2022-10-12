import time

from backend.models import Task
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Перезагружает задачи из очереди"

    def handle(self, *args, **options):
        tasks = Task.objects.filter(state=1)
        for t in tasks:
            t.state = 0
            t.save()
        tasks = Task.objects.filter(state=2)
        for t in tasks:
            t.state = 0
            t.save()
