from django.contrib import admin
from blog.models import Tag, Category, Page, Post

@admin.register(Tag)
class AdminTag(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name',)
    search_fields = ('id', 'name', 'slug',)
    list_per_page = 10
    ordering = ('-id',)
    prepopulated_fields = {"slug": ('name',)}

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug',)
    list_display_links = ('name',)
    search_fields = ('id', 'name', 'slug',)
    list_per_page = 10
    ordering = ('-id',)
    prepopulated_fields = {"slug": ('name',)}

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'is_published')
    list_display_links = ('title',)
    search_fields = ('id', 'title', 'slug',)
    list_per_page = 50
    list_filter = ('is_published',)
    list_editable = ('is_published',)
    ordering = ('-id',)
    prepopulated_fields = {"slug": ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'is_published')
    list_display_links = ('title',)
    search_fields = ('id', 'title', 'slug',)
    list_per_page = 50
    list_filter = ('category', 'is_published',)
    list_editable = ('is_published',)
    ordering = ('-id',)
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by', )
    prepopulated_fields = {"slug": ('title',)}
