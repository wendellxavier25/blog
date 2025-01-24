from django.db import models
from utils.rands import slugify_new
from django.contrib.auth.models import User
from utils.images import  resize_image
from django_summernote.models import AbstractAttachment
from django.urls import reverse



class PostAttachment(AbstractAttachment):
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.file.name
        current_file_name = str(self.file.name)
        super_save = super().save(*args, **kwargs)
        file_changed = False
        if self.file:
            file_changed = current_file_name != self.file.name
        if file_changed:
            resize_image(self.file, 900, True, 70)
        return super_save





class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, default=None, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name, 4)
        return super().save(*args, **kwargs)
    

    def __str__(self):
        return self.name
    



class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, default=None, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name, 4)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name




class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, default="", null=False, blank=True, max_length=255)
    is_published = models.BooleanField(default=False)
    content = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title, 4)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    

class PostManager(models.Manager):
    def get_published(self):
        return self.filter(is_published=True).order_by('-pk')



class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    objects = PostManager()

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, default="", null=False, blank=True, max_length=150)
    excerpt = models.CharField(max_length=150)
    is_published = models.BooleanField(default=False)
    content = models.TextField()
    cover = models.ImageField(upload_to='posts/%Y/%m/', blank=True, default='')
    cover_in_post_content = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='post_created_by')
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='post_updated_by')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    tags = models.ManyToManyField(Tag, blank=True, default='')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        if not self.is_published:
            return reverse('blog:index')
        return reverse('blog:post', args=(self.slug,))
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title, 4)

        current_favicon_name = str(self.cover.name)
        super_save = super().save(*args, **kwargs)
        favicon_changed = False

        if self.cover:
            favicon_changed = current_favicon_name != self.cover.name

        if favicon_changed:
            resize_image(self.cover, 900, True, 90)

        return super_save
