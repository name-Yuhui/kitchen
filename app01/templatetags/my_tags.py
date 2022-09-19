from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def remainder(v1,v2):
    return int(v1)%int(v2)