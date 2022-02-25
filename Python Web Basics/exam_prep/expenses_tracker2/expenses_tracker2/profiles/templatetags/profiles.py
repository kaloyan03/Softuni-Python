from django import template

from expenses_tracker2.profiles.views import get_profile

register = template.Library()

@register.simple_tag()
def has_profile():
    profile = get_profile()

    if profile:
        return True
    return False