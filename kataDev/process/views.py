from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, Context
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def index(request):
    template = loader.get_template('process/index.html')
    formSignUp = CustomUserCreationForm
    formLogIn = CustomAuthenticationForm
    print(formLogIn)
    print(formSignUp)
    content = {
        'formSignUp' : formSignUp,
        'formLogIn' : formLogIn,
    }
    return HttpResponse(template.render(content, request))

def signupsuccess(request):
    template = loader.get_template('process/auth/test_signup.html')
    content = {
        'test' : 'test'
    }
    return HttpResponse(template.render(content, request))

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('signupsuccess')
        else:
            print(form.errors)
            return HttpResponse('Something went wrong' + str(form.errors))
    else:
        return HttpResponse('Wrong request')

def loginuser(request):
    if request.method == 'POST':
        print(request.POST['username'])
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        print(user)
        if user is not None:
            login(request, user)
            return redirect('overview')
        else:
            template = loader.get_template('process/auth/login_failed.html')
            content = {
                'test' : 'test'
            }
            return HttpResponse(template.render(content, request))
    else:
        return HttpResponse('Wrong request')

def logoutuser(request):
    logout(request)
    template = loader.get_template('process/auth/logout.html')
    content = {
        'test' : 'test'
    }
    return HttpResponse(template.render(content, request))

def overview(request):
    if request.user.is_authenticated:
        template = loader.get_template('process/overview.html')
        content = {
            'test' : 'test'
        }
        return HttpResponse(template.render(content, request))
    else:
        template = loader.get_template('process/auth/login_failed.html')
        content = {
            'test' : 'test'
        }
        return HttpResponse(template.render(content, request))
