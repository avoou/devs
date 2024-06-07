from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
    skills = models.ManyToManyField('Skills', blank=True)
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


    def __str__(self) -> str:
        return str(self.user.username)


class Skills(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, 
        unique=True, 
        primary_key=True, 
        editable=False
    )


    def __str__(self) -> str:
        return self.name