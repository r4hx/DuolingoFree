from django.contrib import admin

from backend.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "url",
        "state",
        "created_at",
        "running_at",
        "finished_at",
    ]
    list_display_links = [
        "id",
        "url",
    ]
    search_fields = [
        "id",
        "url",
        "state",
        "created_at",
        "running_at",
        "finished_at",
    ]
    list_editable = [
        "state",
    ]
    ordering = ["-id"]


admin.site.register(Task, TaskAdmin)
