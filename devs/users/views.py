from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, ProfileForm, SkillForm, MessageForm
from .models import Profile, Skills
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utils import searchProfiles, custom_pagination, getProfile


def registerUser(request):
    """View for register user"""

    page = 'register'
    form = CustomUserCreationForm()
    context = {'page': page, 'form': form}
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            return redirect('edit-profile')
        
        else:
            messages.error(request, 'Something went wrong')

    return render(request, 'users/login-register.html', context=context)


def logoutUser(request):
    """View for logout"""

    logout(request)
    messages.success(request, "Sucssefully logout!)")
    return redirect('login')


def loginUser(request):
    """Login user already exist"""

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
    """View to get list of user profiles"""

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
    """View to get user profile by id"""

    profile = Profile.objects.get(id=id)
    context = {'profile': profile}
    return render(request, 'users/user-profile.html', context=context)


@login_required(login_url='login')
def getUserAccount(request):
    """View to get user account"""

    profile = request.user.profile
    projects = profile.project_set.all()
    context = {'profile': profile, 'projects': projects}
    return render(request, 'users/account.html', context=context)


@login_required(login_url='login')
def editAccount(request):
    """View to edit user account"""

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
    """View to add some skill to user profile"""

    profile = request.user.profile
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save()
            profile.skills_set.add(skill) 
            profile.save()
            return redirect('account')
        
    context = {'form': form}
    return render(request, 'users/skill-form.html', context=context)


@login_required(login_url='login')
def updateSkill(request, id):
    """View to update a skill which already exist"""

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
    """View to delete some skill from profile"""

    profile = request.user.profile
    skill = profile.skills_set.get(id=id)
    if request.method == 'POST':
        skill.delete()
        return redirect('account')
    context = {'object': skill}
    return render(request, 'delete-form.html', context=context)


@login_required(login_url='login')
def inbox(request):
    """View to get list of inbox messages"""

    profile = request.user.profile
    recipient_messages = profile.messages.all()
    unread_count = recipient_messages.filter(is_read=False).count()
    context = {
        'messages': recipient_messages,
        'unread_count': unread_count,
    }
    return render(request, 'users/inbox.html', context=context)


@login_required(login_url='login')
def message(request, id):
    """View to read a message and udate status"""
    profile = request.user.profile
    message = profile.messages.get(id=id)
    
    if not message.is_read:
        message.is_read = True
        message.save()

    context = {'message': message}
    return render(request, 'users/message.html', context=context)


@login_required(login_url='login')
def create_message(request, id):
    """View to send a message to somebody"""

    sender_profile = request.user.profile
    recipient_profile = getProfile(id)
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender_profile
            message.sender_name = sender_profile.name
            message.recipient = recipient_profile
            message.sender_email = sender_profile.email
            message.save()

        return redirect('user-profile', id=recipient_profile.id)

    context = {'form': form}
    return render(request, 'users/create-message.html', context=context)