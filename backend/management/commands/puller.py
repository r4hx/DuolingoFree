import time

from backend.models import Task
from backend.tasks import create_a_new_invited_user
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Проверяет базу на наличие новых задач"

    def handle(self, *args, **options):
        while True:
            for task in Task.objects.filter(state=0):
                create_a_new_invited_user.delay(task.pk)
                task.state = 1
                task.save()
            time.sleep(5)
