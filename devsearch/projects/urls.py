from django.urls import path
from .views import projects, project

urlpatterns = [
    path('', projects, name='projects'),
    path('project/<str:id>', project, name='project'),
]