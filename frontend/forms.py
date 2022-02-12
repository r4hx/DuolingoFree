from backend.models import Task
from backend.validators import validate_url
from django import forms


class TaskForm(forms.ModelForm):
    url = forms.URLField(
        min_length=27,
        max_length=65,
        validators=[validate_url],
        required=True,
    )

    class Meta:
        model = Task
        fields = ("url",)
