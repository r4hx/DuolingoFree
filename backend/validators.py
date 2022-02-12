from urllib.parse import urlparse

from django.core.exceptions import ValidationError


def validate_url(value):
    if not value:
        return
    obj = urlparse(value)
    if obj.hostname != "invite.duolingo.com":
        raise ValidationError("Only urls from Duolingo allowed")
