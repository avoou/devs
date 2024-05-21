from django.shortcuts import render


def getProfiles(request):
    return render(request, 'users/profiles.html')