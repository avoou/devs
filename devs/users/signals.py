from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings


def createProfileReciever(sender, instance, created, **kwargs):
    """Signal that create a profile when the user has been created. 
    Then message to email will send."""

    if created:
        profile = Profile.objects.create(
            user=instance,
            username=instance.username,
            name=instance.first_name,
            email=instance.email
        )
        profile.save()

        subject = 'devs'
        message = 'Welcome to devs'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )
    

def updateProfile(sender, instance, created, **kwargs):
    """Signal that update user info when profile has been edited"""

    user = instance.user

    if not created:
        user.first_name = instance.name
        user.username = instance.username
        user.email = instance.email
        user.save()
        print('user ', instance, ' was updated')


def deletedProfile(sender, instance, **kwargs):
    """Signal that delete user when profile has been deleted"""
    
    try:
        user = instance.user
        user.delete()
    except:
        pass


post_save.connect(createProfileReciever, sender=User)
post_save.connect(updateProfile, sender=Profile)
post_delete.connect(deletedProfile, sender=Profile)