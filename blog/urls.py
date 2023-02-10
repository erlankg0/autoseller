from django.urls import path
from blog.views import BlogsListView, BlogDetailView

urlpatterns = [
    path('', BlogsListView.as_view(), name='blogs'),
    path('<str:slug>/', BlogDetailView.as_view(), name='blog'),
]
