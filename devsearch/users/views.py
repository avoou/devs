from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from .models import Profile
from django.contrib import messages


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
            return redirect('profiles')
        
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
    profileObjs = Profile.objects.all()
    context = {'profiles': profileObjs}
    return render(request, 'users/profiles.html', context=context)


def userProfile(request, id):
    profile = Profile.objects.get(id=id)
    context = {'profile': profile}
    return render(request, 'users/user-profile.html', context=context)