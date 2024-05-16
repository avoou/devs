from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


PROJECTS_LIST = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]


def projects(request):
    projectObjs = Project.objects.all()
    context = {
        'project_name': 'PROJECT777',
        'age': 17,
        'projectsList': projectObjs,
    }
    return render(request, 'projects/projects.html', context=context)

def project(request, id):
    specific_project = Project.objects.get(id=id)
    tags = specific_project.tag.all()
    reviews = specific_project.review_set.all()
    context = {
        'specific_project': specific_project,
        'tags': tags,
        'reviews': reviews,
    }
    return render(request, 'projects/single-project.html', context=context)

