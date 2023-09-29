from django.contrib import admin
from .models import *

# Register your models here.

class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'id_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('id_published',)
    list_filter = ('id_published', 'time_create')

admin.site.register(Women, WomenAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)