from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.getProfiles, name='profiles'),
    path('profiles/<str:id>/', views.userProfile, name='user-profile'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('account/', views.getUserAccount, name='account'),
]