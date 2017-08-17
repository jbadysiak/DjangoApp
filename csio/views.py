from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegistrationForm
from csio.forms import LoginForm
from .models import Profile

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Uwierzytelnienie zakończone sukcesem')
                else:
                    return HttpResponse('Konto zablokowne')
            else:
                return HttpResponse('Błędne dane uwierzytelniające')
    else:
        form = LoginForm()
    return render(request, 'csio/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'csio/dashboard.html', {'dashboard': 'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request, 'csio/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'csio/register.html', {'user_form': user_form})
