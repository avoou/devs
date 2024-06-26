from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes),
    path('projects/', views.getProjects),
    path('projects/<str:id>/', views.getProject),
]