from django.db import models
from django.utils.text import slugify
from apps.core.models import TimeStampedModel
from apps.accounts.models import User


class Course(TimeStampedModel):
    """
    Course model
    """
    LEVEL_CHOICES = [
        ('BEGINNER', 'Beginner'),
        ('INTERMEDIATE', 'Intermediate'),
        ('ADVANCED', 'Advanced'),
    ]
    
    title = models.CharField(max_length=200, help_text='Course title')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(help_text='Course description')
    thumbnail = models.ImageField(
        upload_to='courses/thumbnails/',
        blank=True,
        null=True,
        help_text='Course thumbnail image'
    )
    
    instructor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='courses',
        help_text='Course instructor'
    )
    level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        default='BEGINNER',
        help_text='Course difficulty level'
    )
    
    is_published = models.BooleanField(
        default=False,
        help_text='Is course published?'
    )
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    @property
    def total_modules(self):
        """Get total number of modules"""
        return self.modules.count()
    
    @property
    def total_lessons(self):
        """Get total number of lessons"""
        return sum(module.lessons.count() for module in self.modules.all())
    
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['-created_at']


class Module(TimeStampedModel):
    """
    Course module model
    """
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='modules',
        help_text='Parent course'
    )
    title = models.CharField(max_length=200, help_text='Module title')
    description = models.TextField(blank=True, help_text='Module description')
    order = models.PositiveIntegerField(
        default=0,
        help_text='Module order in course'
    )
    
    def __str__(self):
        return f"{self.course.title} - {self.title}"
    
    @property
    def total_lessons(self):
        """Get total number of lessons in this module"""
        return self.lessons.count()
    
    class Meta:
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'
        ordering = ['course', 'order']
        unique_together = ['course', 'order']


class Lesson(TimeStampedModel):
    """
    Lesson model
    """
    LESSON_TYPE_CHOICES = [
        ('VIDEO', 'Video'),
        ('TEXT', 'Text'),
    ]
    
    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        related_name='lessons',
        help_text='Parent module'
    )
    title = models.CharField(max_length=200, help_text='Lesson title')
    lesson_type = models.CharField(
        max_length=10,
        choices=LESSON_TYPE_CHOICES,
        default='TEXT',
        help_text='Lesson type'
    )
    
    # For video lessons
    video_url = models.URLField(
        blank=True,
        null=True,
        help_text='YouTube or video URL'
    )
    
    # For text lessons
    content = models.TextField(
        blank=True,
        help_text='Lesson content (Markdown supported)'
    )
    
    order = models.PositiveIntegerField(
        default=0,
        help_text='Lesson order in module'
    )
    duration = models.PositiveIntegerField(
        default=0,
        help_text='Duration in minutes'
    )
    
    def __str__(self):
        return f"{self.module.title} - {self.title}"
    
    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
        ordering = ['module', 'order']
        unique_together = ['module', 'order']
