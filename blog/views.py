from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import CommentForm

def detailview(request, category, slug):
    post = get_object_or_404(Post, slug = slug)

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
    posts = Post.objects.filter(category = category)
    return render(request, 'blog/category.html', {
        'category': category,
        'posts': posts
    })