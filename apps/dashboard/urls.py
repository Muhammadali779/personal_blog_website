from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_home_view, name='home'),
    path('blogs/', views.manage_blogs_view, name='manage_blogs'),
    path('courses/', views.manage_courses_view, name='manage_courses'),
    path('users/', views.manage_users_view, name='manage_users'),
]
