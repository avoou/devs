from django.db import models
from users.models import Profile
import uuid


#project = Project.objects.get(title='Telegram')
#project.review_set.all() - for one to many relationship
#project.tag.all() - for many to many


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    tag = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default='default.png')
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, 
        unique=True, 
        primary_key=True, 
        editable=False
    )

    def __str__(self) -> str:
        return self.title
    

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, 
        unique=True, 
        primary_key=True, 
        editable=False
    )

    def __str__(self) -> str:
        return f'{self.project}|{self.created}|{self.value}' 
    

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, 
        unique=True, 
        primary_key=True, 
        editable=False
    )


    def __str__(self) -> str:
        return self.name
    

from django.db.models.signals import post_save, post_delete


def saveProject(sender, instance, created, **kwargs):
    print('in saveProject')
    print('tags: ', instance.tag.all())


post_save.connect(saveProject, sender=Project)