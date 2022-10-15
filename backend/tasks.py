from django.utils import timezone
from DuolingoFree.celery import app

from backend.duolingo import Duolingo
from backend.models import Task
from backend.telegram import Telegram


@app.task(bind=True)
def create_a_new_invited_user(self, pk):
    task = Task.objects.get(pk=pk)
    try:
        task.state = 2
        task.running_at = timezone.now()
        task.save()
        with Duolingo(task.url):
            pass
        task.finished_at = timezone.now()
        task.state = 3
        task.save()
        Telegram().send_message(message=f"Task #{task.pk} - FINISHED")
    except Exception as e:
        print(e)
        task.state = 4
        task.save()
        Telegram().send_message(message=f"Task #{task.pk} - ERROR")
        raise self.retry(exc=e, max_retries=5)
