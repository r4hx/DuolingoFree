import os
from datetime import timedelta

from backend.models import Task
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect, render
from django.utils import timezone

from frontend.forms import TaskForm


def index(request):
    max_unique_links_per_day = os.getenv("MAX_UNIQUE_LINKS_PER_DAY", 5)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            links_of_day = Task.objects.filter(
                url=form.cleaned_data["url"],
                created_at__range=[
                    timezone.now() - timedelta(days=1),
                    timezone.now(),
                ],
            ).count()
            if links_of_day >= max_unique_links_per_day:
                messages.info(
                    request,
                    f"You sent more than {max_unique_links_per_day} links for the day",
                )
                return HttpResponseRedirect("/")
            form.save()
            messages.success(request, "Link sending to queue")
            return HttpResponseRedirect("/")
        else:
            messages.error(request, "Your link is bad, check it")
            return HttpResponseRedirect("/")
    elif request.method == "GET":
        form = TaskForm
        queued = Task.objects.filter(state=1).count()
        running = Task.objects.filter(state=2).count()
        finished = Task.objects.filter(state=3).count()
        errored = Task.objects.filter(state=4).count()
        start_after = (running + queued) * 60
        context = {
            "form": form,
            "queued": queued,
            "running": running,
            "finished": finished,
            "errored": errored,
            "start_after": start_after,
        }
        return render(request, "index.html", context)
