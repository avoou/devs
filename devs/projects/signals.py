from django.db.models.signals import post_save, post_delete
from .models import Project, Review


def saveProject(sender, instance, created, **kwargs):
    pass


def updateProjectsVote(sender, instance, **kwargs):
    """Signal which update project votes ratio when review has been created"""
    instance.project.updateVotesRatio()


post_save.connect(saveProject, sender=Project)
post_delete.connect(updateProjectsVote, sender=Review)