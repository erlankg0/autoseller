from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Blog


class BlogsListView(ListView):
    model = Blog
    template_name = 'blog/blogs.html'
    context_object_name = 'blog_list'

    def get_queryset(self):
        return Blog.objects.all().order_by('-pub_date')  # сортировка по дате публикации


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blog'

    # get blog by slug
    def get_object(self, queryset=None):
        return Blog.objects.get(slug=self.kwargs['slug'])
