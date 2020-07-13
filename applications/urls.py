from django.urls import path
from . import views



urlpatterns = [
    path('HomePage/', views.HomePage),
    path('AdminPage/', views.AdminPage),
    path('AddApp/', views.AddApp),
    path('User/', views.User),
    path('Profile/', views.Profile),

]