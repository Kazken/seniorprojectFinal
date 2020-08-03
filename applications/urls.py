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
    path('search/', views.search, name="search"),
    path('add_app/', views.add_app, name="add_app"),
    path('add_user/', views.add_user, name="add_user"),
    path('update/<str:pk>/', views.update, name="update"),
    path('delete/<str:pk>/', views.delete, name="delete"),
    path('delete_user/<str:pk>/', views.delete_user, name="delete_user"),
    path('delete_assign/<str:pk>/', views.delete_assign, name="delete_assign"),
]