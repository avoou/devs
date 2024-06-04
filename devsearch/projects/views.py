from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Tag
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required


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


@login_required(login_url='login')
def create_project(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'projects/project-form.html', context=context)


@login_required(login_url='login')
def update_project(request, id):
    project = Project.objects.get(id=id)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'projects/project-form.html', context=context)


@login_required(login_url='login')
def delete_project(request, id):
    project = Project.objects.get(id=id)

    if request.method == 'POST':
        project.delete()        
        return redirect('projects')
    
    context = {'project': project}
    return render(request, 'projects/delete-form.html', context=context)