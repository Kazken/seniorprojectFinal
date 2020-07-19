from django.urls import path
from . import views
from . views import search



urlpatterns = [
    path('login/', views.login, name="login"),
    path('dash/', views.dash, name="dash"),
    path('app_page/', views.app_page, name="apps"),
    path('user_page/', views.user_page, name="users"),
    path('profile/<str:pk>/', views.profile, name="profile"),
    path('audit/', views.audit, name="audit"),
    path('search/', views.search, name="search")


]