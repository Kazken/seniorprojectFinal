from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.db.models import Q
from .forms import AppForm
from .forms import UserForm


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

def add_app(request):

    form = AppForm()
    if request.method == 'POST':
        #print('Printing POST:' ,request.POST)
        form = AppForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/app_page/')

    context = {'form':form}
    return render(request, 'accounts/AddForm.html', context)

def add_user(request):

    form = UserForm()
    if request.method == 'POST':
        #print('Printing POST:' ,request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user_page/')

    context = {'form':form}
    return render(request, 'accounts/UserForm.html', context)

def update(request, pk):

    apps = App.objects.get(id=pk)
    form = AppForm(instance=apps)

    if request.method == 'POST':
            form = AppForm(request.POST, instance=apps)
            if form.is_valid():
                form.save()
                return redirect('/app_page/')
    context = {'form':form, 'apps':apps}
    return render(request, 'accounts/AddForm.html', context)

def delete(request, pk):

    apps = App.objects.get(id=pk)
    if request.method == "POST":
        apps.delete()
        return redirect ('/user_page/')


    context = {'apps':apps}
    return render(request, 'accounts/delete.html', context)

def delete_user(request, pk):

    users = User.objects.get(id=pk)
    if request.method == "POST":
        users.delete()
        return redirect ('/user_page/')


    context = {'users':users}
    return render(request, 'accounts/DeleteProfile.html', context)

def delete_assign(request, pk):

    apps= users.app_set.all(id=pk)

    if request.method == "POST":
        users.delete()
        return redirect ('/user_page/')


    context = {'apps':apps, 'users':users}
    return render(request, 'accounts/DeleteAssign.html', context)