from django.db.models.signals import post_save, post_delete
from .models import Project, Review


def saveProject(sender, instance, created, **kwargs):
    print('in saveProject')
    print('tags: ', instance.tag.all())


def updateProjectsVote(sender, instance, **kwargs):
    print('in updateProjectsVote')
    instance.project.updateVotesRatio()


post_save.connect(saveProject, sender=Project)
post_delete.connect(updateProjectsVote, sender=Review)