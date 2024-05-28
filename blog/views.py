from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import CommentForm

def detailview(request, category, slug):
    post = get_object_or_404(Post, slug = slug, status=Post.ACTIVE)

    if request.method == "POST":
        form = CommentForm(request.POST)        
        if form.is_valid():

            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect('detailpage', slug=slug)     

    form = CommentForm()
    
    return render(request, 'blog/detail.html', {
        'post' : post,
        'form': form
    })

def categoryview(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category = category, status = Post.ACTIVE)
    return render(request, 'blog/category.html', {
        'category': category,
        'posts': posts
    })

def search(request):
    query = request.GET.get('query', '')
    posts = Post.objects.filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query), status=Post.ACTIVE)
    # posts = Post.objects.filter(title__icontains=query, status=Post.ACTIVE)
    return render(request, 'blog/search.html', {'posts': posts, 'query': query})