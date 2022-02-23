from django import template

from notes.profiles.views import get_profile

register = template.Library()

@register.simple_tag()
def has_profile():
    return bool(get_profile())