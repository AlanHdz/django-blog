from django.shortcuts import render

from app_blog.models import Post

def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'core/frontpage.html', { 'posts': posts })

def about(request):
    return render(request, 'core/about.html')