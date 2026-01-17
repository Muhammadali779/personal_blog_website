from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.course_list_view, name='course_list'),
    path('<slug:slug>/', views.course_detail_view, name='course_detail'),
    path('<slug:course_slug>/module/<int:module_id>/lesson/<int:lesson_id>/', 
         views.lesson_view, name='lesson_view'),
]
