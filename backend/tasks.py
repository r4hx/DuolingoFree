import traceback

from celery import states
from django.utils import timezone
from DuolingoFree.celery import app

from backend.duolingo import Duolingo
from backend.models import Task
from backend.telegram import Telegram


@app.task(bind=True, ignore_result=False)
def create_a_new_invited_user(self, pk: int):
    """
    Создает нового пользователя из данных Task
    """
    task = Task.objects.get(pk=pk)
    result = None
    try:
        task.state = 2
        task.running_at = timezone.now()
        task.save()
        with Duolingo(task.url) as e:
            result = e
        task.finished_at = timezone.now()
        task.state = 3
        task.save()
        Telegram().send_message(message=f"Task #{task.pk} - FINISHED")
    except Exception as e:
        task.state = 4
        task.save()
        Telegram().send_message(message=f"Task #{task.pk} - ERROR")
        raise e
    return result
