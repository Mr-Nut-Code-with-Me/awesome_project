from django.shortcuts import render

from blog.models import Post

def frontpage(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'core/frontpage.html', {
        'posts' : posts
    })

def aboutpage(request):
    return render(request, 'core/about.html')