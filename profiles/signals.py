import logging

from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Profile


logger = logging.getLogger('fancy-shop-logger')


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(
            user=instance,
            nickname=instance.username,
            email=instance.email
        )
        Profile.save(profile)
        logger.info(f"The profile for user {instance.username} has been created")




