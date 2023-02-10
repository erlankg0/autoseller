from blog.models import Blog


def blogs(request):
    blog = Blog.objects.all()
    return {'blogs': blog}
