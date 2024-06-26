from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectsSerializer
from projects.models import Project


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': 'api/projects'},
        {'GET': 'api/projects/id'},
        {'PUT': 'api/projects/vote'},
        {'POST': 'api/users/token'},
        {'POST': 'api/users/token/refresh'},
    ]
    return Response(routes)


@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectsSerializer(projects, many=True)
    
    return Response(serializer.data)


@api_view(['GET'])
def getProject(request, id):
    project = Project.objects.get(id=id)
    serializer = ProjectsSerializer(project, many=False)
    
    return Response(serializer.data)