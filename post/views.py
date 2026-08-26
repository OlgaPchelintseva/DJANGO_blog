from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment
from .forms import PostCreateForm, CommentForm

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {
        'posts': posts,
        'page_title': 'Все посты блога'
    }
    return render(request, 'post/post_list.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.all().order_by('-created_at')
    if request.method == 'POST':
        # проверка на авторизацию свойство is_authenticated
        if not request.user.is_authenticated:
            messages.warning(request, 'Авторизуйтесь, чтобы оставить комментарий')
            return redirect('login')
        
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) # commit сщхраняет данные в БД, если поставить False, то не сохранит
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Комментарий добавлен')
            return redirect('post:post_detail', post_id = post.id)
        else:
            messages.error(request, 'Ошибка при добавлении комментария')
    else:
        form = CommentForm()
    
    context = {
        'post': post,
        'comments': comments,
        'form': form,
        'page_title': post.title
    }
    return render(request, 'post/post_details.html', context)

