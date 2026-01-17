from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from apps.accounts.permissions import admin_required
from .models import Blog, Category, Tag
from .forms import BlogForm


def blog_list_view(request):
    """
    List all published blogs with filtering and pagination
    """
    blogs = Blog.objects.filter(status='PUBLISHED').select_related('author', 'category')
    
    # Filter by category
    category_slug = request.GET.get('category')
    if category_slug:
        blogs = blogs.filter(category__slug=category_slug)
    
    # Filter by tag
    tag_slug = request.GET.get('tag')
    if tag_slug:
        blogs = blogs.filter(tags__slug=tag_slug)
    
    # Search
    search_query = request.GET.get('q')
    if search_query:
        blogs = blogs.filter(title__icontains=search_query)
    
    # Pagination
    paginator = Paginator(blogs, 9)  # 9 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
    }
    
    return render(request, 'pages/blogs/blog_list.html', context)


def blog_detail_view(request, slug):
    """
    Display single blog post
    """
    blog = get_object_or_404(Blog, slug=slug, status='PUBLISHED')
    
    # Increment view count
    blog.increment_views()
    
    # Get related blogs
    related_blogs = Blog.objects.filter(
        category=blog.category,
        status='PUBLISHED'
    ).exclude(id=blog.id)[:3]
    
    context = {
        'blog': blog,
        'related_blogs': related_blogs,
    }
    
    return render(request, 'pages/blogs/blog_detail.html', context)


@admin_required
def blog_create_view(request):
    """
    Create new blog post (admin only)
    """
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            form.save_m2m()  # Save many-to-many relationships (tags)
            messages.success(request, 'Blog post created successfully!')
            return redirect('blogs:blog_detail', slug=blog.slug)
    else:
        form = BlogForm()
    
    return render(request, 'pages/blogs/blog_create.html', {'form': form})


@admin_required
def blog_edit_view(request, slug):
    """
    Edit existing blog post (admin only)
    """
    blog = get_object_or_404(Blog, slug=slug)
    
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog post updated successfully!')
            return redirect('blogs:blog_detail', slug=blog.slug)
    else:
        form = BlogForm(instance=blog)
    
    return render(request, 'pages/blogs/blog_edit.html', {'form': form, 'blog': blog})


@admin_required
def blog_delete_view(request, slug):
    """
    Delete blog post (admin only)
    """
    blog = get_object_or_404(Blog, slug=slug)
    
    if request.method == 'POST':
        blog.delete()
        messages.success(request, 'Blog post deleted successfully!')
        return redirect('blogs:blog_list')
    
    return render(request, 'pages/blogs/blog_delete.html', {'blog': blog})
