from django.db.models import Q
from .models import Project, Tag
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def custom_pagination(page, projectList, results_on_page):
    paginator = Paginator(projectList, results_on_page)
    try:  
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
    except EmptyPage:
        page = paginator.num_pages
    finally:
        projects = paginator.page(page)
    #print('page: ', page, 'hasprevious: ', projects.has_previous(), 'previous_page: ', projects.previous_page_number)
    
    leftIndex = int(page) - 1
    rightIndex = int(page) + 2

    if leftIndex < 1:
        leftIndex = 1
        rightIndex = 4
    
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1
        
    if int(page) == paginator.num_pages:
        leftIndex = int(page) - 2
    
    custom_range = range(leftIndex, rightIndex)

    return projects, custom_range


def searchProjects(request):
    search_query = ''
    if request.GET.get('query'):
        search_query = request.GET.get('query')

    tags = Tag.objects.filter(name__icontains=search_query)
    projectObjs = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tag__in=tags)
    )
    return projectObjs, search_query