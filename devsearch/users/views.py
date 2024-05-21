from django.shortcuts import render
from .models import Profile


def getProfiles(request):
    profileObjs = Profile.objects.all()
    context = {'profiles': profileObjs}
    return render(request, 'users/profiles.html', context=context)