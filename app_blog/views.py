from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CommentForm
from .models import Post, Category

def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=slug)
    else:
        comment_form = CommentForm()

    return render(request, 'app_blog/detail.html', { 'post': post, 'comment_form': comment_form })

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)

    return render(request, 'app_blog/category.html', {'category': category, 'posts': posts})


def search(request):
    query = request.GET.get('query', '')

    posts = Post.objects.filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))

    return render(request, 'app_blog/search.html', { 'posts': posts, 'query': query })