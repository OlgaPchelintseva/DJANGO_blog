from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {
        'posts': posts,
        'page_title': 'Все посты блога'
    }
    return render(request, 'post/post_list.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post,
        'page_title': post.title
    }
    return render(request, 'post/post_details.html', context)
