from django.db import models
from django.utils.text import slugify
from apps.core.models import TimeStampedModel
from apps.accounts.models import User


class Category(TimeStampedModel):
    """
    Blog category model
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']


class Tag(TimeStampedModel):
    """
    Blog tag model
    """
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['name']


class Blog(TimeStampedModel):
    """
    Blog post model
    """
    STATUS_CHOICES = [
        ('DRAFT', 'Draft'),
        ('PUBLISHED', 'Published'),
    ]
    
    title = models.CharField(max_length=200, help_text='Blog post title')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField(help_text='Blog content in Markdown format')
    excerpt = models.TextField(
        max_length=300,
        blank=True,
        help_text='Short description for preview'
    )
    image = models.ImageField(
        upload_to='blogs/images/',
        blank=True,
        null=True,
        help_text='Featured image'
    )
    
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blogs',
        help_text='Blog author'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='blogs',
        help_text='Blog category'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='blogs',
        blank=True,
        help_text='Blog tags'
    )
    
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='DRAFT',
        help_text='Publication status'
    )
    views = models.PositiveIntegerField(default=0, help_text='View count')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    @property
    def is_published(self):
        """Check if blog is published"""
        return self.status == 'PUBLISHED'
    
    def increment_views(self):
        """Increment view count"""
        self.views += 1
        self.save(update_fields=['views'])
    
    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
        ordering = ['-created_at']
