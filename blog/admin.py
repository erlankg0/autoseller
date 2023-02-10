from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    list_filter = ('pub_date',)
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title', )}
