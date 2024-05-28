from django.shortcuts import render
from .models import Profile


def getProfiles(request):
    profileObjs = Profile.objects.all()
    context = {'profiles': profileObjs}
    return render(request, 'users/profiles.html', context=context)


def userProfile(request, id):
    profile = Profile.objects.get(id=id)
    context = {'profile': profile}
    return render(request, 'users/user-profile.html', context=context)