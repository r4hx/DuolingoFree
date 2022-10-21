from backend.models import Task
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Перезагрузка задач в очереди"

    def handle(self, *args, **options):
        # restart queued tasks
        tasks = Task.objects.filter(state=1)
        for t in tasks:
            t.state = 0
            t.save()
        # restart running tasks
        tasks = Task.objects.filter(state=2)
        for t in tasks:
            t.state = 0
            t.save()
        # restart errored tasks
        tasks = Task.objects.filter(state=4)
        for t in tasks:
            t.state = 0
            t.save()
