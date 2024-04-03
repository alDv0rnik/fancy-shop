from .models import Profile


def update_profile(instance, *args, **kwargs):
    if instance:
        profile = Profile.objects.filter(user=instance.id).first()
        profile.first_name = instance.first_name
        profile.last_name = instance.last_name
        profile.email = instance.email
        profile.save()
