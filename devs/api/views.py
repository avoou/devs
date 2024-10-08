from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import ProjectsSerializer
from projects.models import Project, Review


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
#@permission_classes([IsAuthenticated])
def getProjects(request):
    print('USER: ', request.user)
    projects = Project.objects.all()
    serializer = ProjectsSerializer(projects, many=True)
    
    return Response(serializer.data)


@api_view(['GET'])
def getProject(request, id):
    project = Project.objects.get(id=id)
    serializer = ProjectsSerializer(project, many=False)
    
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request, id):
    user = request.user.profile
    project = Project.objects.get(id=id)
    serializer = ProjectsSerializer(project, many=False)
    review, _ = Review.objects.get_or_create(
        owner=user,
        project=project
    )
    data = request.data
    review.value = data['review_value']
    review.save()
    project.updateVotesRatio()

    return Response(serializer.data)