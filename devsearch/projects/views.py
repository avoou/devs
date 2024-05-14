from django.shortcuts import render
from django.http import HttpResponse


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
    context = {
        'project_name': 'PROJECT777',
        'age': 17,
        'projectsList': PROJECTS_LIST,
    }
    return render(request, 'projects/projects.html', context=context)

def project(request, id):
    specific_project = None
    for project in PROJECTS_LIST:
        if int(project.get('id')) == id:
            specific_project = project

    context = {
        'specific_project': specific_project
    }
    return render(request, 'projects/single-project.html', context=context)

