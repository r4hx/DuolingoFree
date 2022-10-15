from django.db import models

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
        verbose_name="Ссылка",
        help_text="Введите ссылку-приглашение",
    )
    state = models.IntegerField(
        choices=State.choices,
        default=0,
        verbose_name="Состояние",
        help_text="Текущее состояние задачи",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Дата создания задачи",
    )
    running_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дата запуска",
        help_text="Дата запуска задачи",
    )
    finished_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дата завершения",
        help_text="Дата завершения задачи",
    )

    def __str__(self) -> str:
        """
        Необходимо для отображение имени в админке
        """
        return str(self.pk)

    def save(self, *args, **kwargs):
        super(Task, self).save(*args, **kwargs)
