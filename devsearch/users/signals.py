from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from .models import Profile

def createProfileReciever(sender, instance, created, **kwargs):
    print("sender ", sender)
    print("instance ", instance)
    print("created ", created)
    if created:
        profile = Profile.objects.create(
            user=instance,
            name=instance.username
        )
        profile.save()
    


def deletedProfile(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    print("User has deleted")


post_save.connect(createProfileReciever, sender=User)
post_delete.connect(deletedProfile, sender=Profile)