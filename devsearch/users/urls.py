from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.getProfiles, name='profiles'),
    path('profiles/<str:id>/', views.userProfile, name='user-profile'),
]