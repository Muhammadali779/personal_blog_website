from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Course, Module, Lesson


def course_list_view(request):
    """
    List all published courses
    """
    courses = Course.objects.filter(is_published=True).select_related('instructor')
    
    # Filter by level
    level = request.GET.get('level')
    if level:
        courses = courses.filter(level=level)
    
    # Search
    search_query = request.GET.get('q')
    if search_query:
        courses = courses.filter(title__icontains=search_query)
    
    # Pagination
    paginator = Paginator(courses, 9)  # 9 courses per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'levels': Course.LEVEL_CHOICES,
    }
    
    return render(request, 'pages/courses/course_list.html', context)


def course_detail_view(request, slug):
    """
    Display course details with modules and lessons
    """
    course = get_object_or_404(
        Course.objects.prefetch_related('modules__lessons'),
        slug=slug,
        is_published=True
    )
    
    context = {
        'course': course,
    }
    
    return render(request, 'pages/courses/course_detail.html', context)


def lesson_view(request, course_slug, module_id, lesson_id):
    """
    Display individual lesson
    """
    course = get_object_or_404(Course, slug=course_slug, is_published=True)
    module = get_object_or_404(Module, id=module_id, course=course)
    lesson = get_object_or_404(Lesson, id=lesson_id, module=module)
    
    # Get next and previous lessons
    next_lesson = Lesson.objects.filter(
        module=module,
        order__gt=lesson.order
    ).order_by('order').first()
    
    prev_lesson = Lesson.objects.filter(
        module=module,
        order__lt=lesson.order
    ).order_by('-order').first()
    
    context = {
        'course': course,
        'module': module,
        'lesson': lesson,
        'next_lesson': next_lesson,
        'prev_lesson': prev_lesson,
    }
    
    return render(request, 'pages/courses/lesson_view.html', context)
