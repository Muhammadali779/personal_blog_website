from django.shortcuts import render
from django.db.models import Count
from apps.accounts.permissions import admin_required
from apps.accounts.models import User
from apps.blogs.models import Blog
from apps.courses.models import Course


@admin_required
def dashboard_home_view(request):
    """
    Admin dashboard home with statistics
    """
    # Get statistics
    total_users = User.objects.count()
    total_blogs = Blog.objects.count()
    published_blogs = Blog.objects.filter(status='PUBLISHED').count()
    draft_blogs = Blog.objects.filter(status='DRAFT').count()
    total_courses = Course.objects.count()
    published_courses = Course.objects.filter(is_published=True).count()
    
    # Recent blogs
    recent_blogs = Blog.objects.select_related('author', 'category').order_by('-created_at')[:5]
    
    # Recent courses
    recent_courses = Course.objects.select_related('instructor').order_by('-created_at')[:5]
    
    context = {
        'total_users': total_users,
        'total_blogs': total_blogs,
        'published_blogs': published_blogs,
        'draft_blogs': draft_blogs,
        'total_courses': total_courses,
        'published_courses': published_courses,
        'recent_blogs': recent_blogs,
        'recent_courses': recent_courses,
    }
    
    return render(request, 'dashboard/index.html', context)


@admin_required
def manage_blogs_view(request):
    """
    Manage all blogs (admin only)
    """
    blogs = Blog.objects.select_related('author', 'category').order_by('-created_at')
    
    context = {
        'blogs': blogs,
    }
    
    return render(request, 'dashboard/blog_manage.html', context)


@admin_required
def manage_courses_view(request):
    """
    Manage all courses (admin only)
    """
    courses = Course.objects.select_related('instructor').order_by('-created_at')
    
    context = {
        'courses': courses,
    }
    
    return render(request, 'dashboard/course_manage.html', context)


@admin_required
def manage_users_view(request):
    """
    Manage all users (admin only)
    """
    users = User.objects.annotate(
        blog_count=Count('blogs'),
        course_count=Count('courses')
    ).order_by('-date_joined')
    
    context = {
        'users': users,
    }
    
    return render(request, 'dashboard/user_manage.html', context)
