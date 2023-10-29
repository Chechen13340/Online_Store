from django import template
from django.conf import settings
import os

register = template.Library()


@register.filter
def full_media_url(value):
    # print(value, 11111)
    if value.startswith(settings.MEDIA_URL):
        return value
    else:
        return os.path.join(settings.MEDIA_URL, value)
