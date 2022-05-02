from django.utils import timezone
from DuolingoFree.celery import app

from backend.duolingo import Duolingo
from backend.models import Task
from backend.telegram import Telegram

app.control.time_limit("backend.tasks.create_a_new_invited_user", hard=120, reply=False)
t = Telegram()


@app.task(bind=True)
def create_a_new_invited_user(self, pk):
    task = Task.objects.get(pk=pk)
    task.state = 2
    task.running_at = timezone.now()
    task.save()
    t.send_message(message=f"task {task.pk} - RUNNING")
    try:
        with Duolingo(task.url):
            pass
        task.finished_at = timezone.now()
        task.state = 3
        task.save()
        t.send_message(message=f"task {task.pk} - FINISHED")
    except Exception as e:
        print(e)
        task.state = 4
        task.save()
        t.send_message(message=f"task {task.pk} - ERROR")
