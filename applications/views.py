from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q


# Create your views here.
from .models import *

def login(request):
    return render(request, 'accounts/HomePage.html')

def dash(request):
    return render(request, 'accounts/AdminPage.html')

def app_page(request):

    apps = App.objects.all()

    return render(request, 'accounts/AddApp.html', {'app_page': apps})

def user_page(request):
    users = User.objects.all()

    return render(request, 'accounts/User.html', {'user_page': users} )

def profile(request, pk):
    users = User.objects.get(id=pk)

    apps= users.app_set.all()

    context = {'users': users, 'apps': apps}

    return render(request, 'accounts/Profile.html', context)

def audit(request):
    return render(request, 'accounts/AuditLog.html')

def search(request):
    template = 'AddApp.html'

    query = request.GET.get('q')

    results = App.objects.filter(Q(body__icontains=query))

    return render(request, template)