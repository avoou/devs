from .models import Skills, Profile
from django.db.models import Q


def searchProfiles(request):
    search_query = ''

    if request.GET.get('query'):
        search_query = request.GET.get('query')

    skills = Skills.objects.filter(name__icontains=search_query)
    profileObjs = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(short_intro__icontains=search_query) |
        Q(skills__in=skills)
    )

    return profileObjs, search_query