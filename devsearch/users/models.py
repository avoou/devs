from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=300, null=True, blank=True)
    short_intro = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profiles/', default='default.png', null=True, blank=True)
    social_link = models.CharField(max_length=500, null=True, blank=True)
    expierence = models.TextField(null=False, blank=True)
    id = models.UUIDField(
        default=uuid.uuid4, 
        unique=True, 
        primary_key=True, 
        editable=False
    )


    @property
    def image_url(self):
        try:
            url = self.profile_image.url
        except:
            url = '/images/default.png'

        return url
    

    def __str__(self) -> str:
        return str(self.user.username)


class Skills(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, 
        unique=True, 
        primary_key=True, 
        editable=False
    )


    def __str__(self) -> str:
        return self.name
    

class Message(models.Model):
    sender = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    recipient = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL, related_name='messages')
    sender_name = models.CharField(max_length=200, null=True, blank=True)
    sender_email = models.EmailField(max_length=300, null=True, blank=True)
    subject = models.CharField(max_length=500, null=True, blank=True)
    body = models.TextField(null=False, blank=True)
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, 
        unique=True, 
        primary_key=True, 
        editable=False
    )


    def __str__(self):
        return f"{self.sender_email} - {self.subject} - {self.created}"
    

    class Meta:
        ordering = ['is_read', '-created']