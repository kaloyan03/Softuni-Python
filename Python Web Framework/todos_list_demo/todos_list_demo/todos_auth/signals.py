from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from todos_list_demo.todos_auth.models import Profile


@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        profile = Profile(
            user=instance,
        )
        profile.save()