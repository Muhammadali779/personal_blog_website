from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.blog_list_view, name='blog_list'),
    path('create/', views.blog_create_view, name='blog_create'),
    path('<slug:slug>/', views.blog_detail_view, name='blog_detail'),
    path('<slug:slug>/edit/', views.blog_edit_view, name='blog_edit'),
    path('<slug:slug>/delete/', views.blog_delete_view, name='blog_delete'),
]
