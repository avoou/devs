from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.getProfiles, name='profiles'),
    path('profiles/<str:id>/', views.userProfile, name='user-profile'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('account/', views.getUserAccount, name='account'),
    path('edit-profile/', views.editAccount, name='edit-profile'),
    path('add-skill/', views.addSkill, name='add-skill'),
    path('update-skill/<str:id>/', views.updateSkill, name='update-skill'),
    path('delete-skill/<str:id>/', views.deleteSkill, name='delete-skill'),
]