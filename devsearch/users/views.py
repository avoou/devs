from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, ProfileForm, SkillForm
from .models import Profile, Skills
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utils import searchProfiles, custom_pagination


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    context = {'page': page, 'form': form}
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print('usercreationform is valid')
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User has created')

            login(request, user)
            return redirect('edit-profile')
        
        else:
            messages.error(request, 'Something went wrong')

    return render(request, 'users/login-register.html', context=context)


def logoutUser(request):
    logout(request)
    messages.success(request, "Sucssefully logout!)")
    return redirect('login')


def loginUser(request):
    page = 'login'
    context = {'page': page}
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User doesnt exist')
            #pass

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'users/login-register.html', context=context)


def getProfiles(request):
    profileObjs, search_query = searchProfiles(request)
    page = request.GET.get('page')
    results_on_page = 2
    profiles, custom_range = custom_pagination(page=page, profilesList=profileObjs, results_on_page=results_on_page)
    context = {
        'profiles': profiles, 
        'search_query': search_query,
        'custom_range': custom_range,
    }
    return render(request, 'users/profiles.html', context=context)


def userProfile(request, id):
    profile = Profile.objects.get(id=id)
    context = {'profile': profile}
    return render(request, 'users/user-profile.html', context=context)


@login_required(login_url='login')
def getUserAccount(request):
    profile = request.user.profile
    projects = profile.project_set.all()
    context = {'profile': profile, 'projects': projects}
    return render(request, 'users/account.html', context=context)


@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/edit-profile-form.html', context=context)


@login_required(login_url='login')
def addSkill(request):
    profile = request.user.profile
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save()
            #profile.skills.add(skill)
            profile.skills_set.add(skill) 
            profile.save()
            return redirect('account')
        
    context = {'form': form}
    return render(request, 'users/skill-form.html', context=context)


@login_required(login_url='login')
def updateSkill(request, id):
    profile = request.user.profile
    skill = profile.skills_set.get(id=id)
    form = SkillForm(instance=skill)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()

            return redirect('account')
        
    context = {'form': form}
    return render(request, 'users/skill-form.html', context=context)


@login_required(login_url='login')
def deleteSkill(request, id):
    profile = request.user.profile
    skill = profile.skills_set.get(id=id)
    if request.method == 'POST':
        skill.delete()
        return redirect('account')
    context = {'object': skill}
    return render(request, 'delete-form.html', context=context)