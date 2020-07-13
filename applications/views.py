from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import *

def HomePage(request):
    return render(request, 'accounts/HomePage.html')

def AdminPage(request):
    return render(request, 'accounts/AdminPage.html')

def AddApp(request):
    AddApp = Apps.objects.all()
    return render(request, 'accounts/AddApp.html', {'Apps':Apps})

def User(request):
    User = Users.objects.all()
    return render(request, 'accounts/User.html', {'Users': User} )

def Profile(request):
    return render(request, 'accounts/Profile.html')