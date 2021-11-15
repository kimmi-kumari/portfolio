from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.

def allBlogs(request):
    blogs = Blog.objects.all
    return render(request, 'blogs/allblog.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/blog.html', {'blog': blog})
