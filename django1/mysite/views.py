from mysite.models import mysite
from django.shortcuts import render, redirect, get_object_or_404

#from .forms import UserRegistrationForm
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

import io

#from .forms import UserRegistrationForm
#from django.contrib.auth.models import User

#Create your views here.
def home_view(request):
    return render(request, 'registration/home.html')


def login_user(request):
    return render(request, 'registration/login.html')

def login_home_view(request):
    return render(request, 'registration/login_home.html')   

def query_page(request):
    return render(request, 'registration/query_page.html')

def register(request):
    return render(request, 'registration/register.html')

