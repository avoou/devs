from django.shortcuts import render, redirect
from .models import Project, Tag
from .forms import ProjectForm, ReviewForm
from django.contrib.auth.decorators import login_required
from .utils import searchProjects, custom_pagination
from django.contrib import messages


def projects(request):
    """Get projects for one page"""

    projectObjs, search_query = searchProjects(request)
    page = request.GET.get('page')
    results_on_page = 4
    projects, custom_range = custom_pagination(page=page, projectList=projectObjs, results_on_page=results_on_page)

    context = {
        'projectsList': projects,
        'search_query': search_query,

        'custom_range': custom_range,
    }
    
    return render(request, 'projects/projects.html', context=context)


def project(request, id):
    """Get all info about specific project by id"""

    specific_project = Project.objects.get(id=id)
    tags = specific_project.tag.all()
    reviews = specific_project.review_set.all()
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.owner = request.user.profile
            review.project = specific_project
            review.save()
            specific_project.updateVotesRatio()
            return redirect('project', id=id)
            #redirect('project')

    context = {
        'specific_project': specific_project,
        'tags': tags,
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'projects/single-project.html', context=context)


@login_required(login_url='login')
def create_project(request):
    """View to create project"""

    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            #при наличии м2м отношений родитель сначала должен быть сохранен. отакот
            project.save()
            form.save_m2m()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'projects/project-form.html', context=context)


@login_required(login_url='login')
def update_project(request, id):
    """View to update some info in project profile"""

    profile = request.user.profile
    project = profile.project_set.get(id=id)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'projects/project-form.html', context=context)


@login_required(login_url='login')
def delete_project(request, id):
    """View to delete specific project profile by id"""
    
    profile = request.user.profile
    project = profile.project_set.get(id=id)

    if request.method == 'POST':
        project.delete()        
        return redirect('account')
    
    context = {'object': project}
    return render(request, 'delete-form.html', context=context)