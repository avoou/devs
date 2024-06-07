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
            username=instance.username,
            name=instance.first_name,
            email=instance.email
        )
        profile.save()
    

def updateProfile(sender, instance, created, **kwargs):
    user = instance.user

    if not created:
        user.first_name = instance.name
        user.username = instance.username
        user.email = instance.email
        user.save()
        print('user ', instance, ' was updated')


def deletedProfile(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    print("User has deleted")


post_save.connect(createProfileReciever, sender=User)
post_save.connect(updateProfile, sender=Profile)
post_delete.connect(deletedProfile, sender=Profile)