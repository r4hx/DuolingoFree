from django.db import models
from django.utils.translation import ugettext_lazy as _

from backend.validators import validate_url


class Task(models.Model):
    class State(models.IntegerChoices):
        CREATED = 0
        QUEUED = 1
        RUNNING = 2
        FINISHED = 3
        ERROR = 4

    url = models.URLField(
        max_length=65,
        validators=[validate_url],
        verbose_name=_("MODEL_URL_VERBOSE_NAME"),
        help_text=_("MODEL_URL_HELP_TEXT"),
    )
    state = models.IntegerField(
        choices=State.choices,
        default=0,
        verbose_name=_("MODEL_STATE_VERBOSE_NAME"),
        help_text=_("MODEL_STATE_HELP_TEXT"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("MODEL_CREATED_AT_VERBOSE_NAME"),
        help_text=_("MODEL_CREATED_AT_HELP_TEXT"),
    )
    running_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=_("MODEL_RUNNING_AT_VERBOSE_NAME"),
        help_text=_("MODEL_RUNNING_AT_HELP_TEXT"),
    )
    finished_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=_("MODEL_FINISHED_AT_VERBOSE_NAME"),
        help_text=_("MODEL_FINISHED_AT_HELP_TEXT"),
    )

    def __str__(self) -> str:
        """
        Необходимо для отображение имени в админке
        """
        return str(self.pk)

    def save(self, *args, **kwargs):
        super(Task, self).save(*args, **kwargs)
