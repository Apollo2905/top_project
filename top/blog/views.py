from django.shortcuts import render, redirect
from .models import *  # импортирование модели
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q


@login_required(login_url='/users/log_in')
def home(request):
    search = request.GET.get('search')
    posts = Post.objects.all()  # запрос в базу данных
    if search:
        posts = Post.objects.filter(Q(title__icontains=search) | Q(text__icontains=search))
    return render(request, 'home.html', {'posts': posts})  # отправка в html


@login_required(login_url='/users/log_in')
def post(request, slug):
    post_detail = Post.objects.get(slug=slug)
    form = CommentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.post = post_detail
        instance.save()
        return redirect('blog:post', slug=slug)
    return render(request, 'post.html', {'post': post_detail, 'form': form})

@login_required(login_url='/users/log_in')
def myposts(request):
    mypost = Post.objects.filter(author=request.user)
    return render(request, 'myposts.html', {'posts': mypost})

@login_required(login_url='/users/log_in')
def create(request):
    print(request.POST)
    print(request.FILES)
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)
        if Post.objects.last():
            instance.slug = request.POST.get('title') + str(Post.objects.last().pk + 1)
        else:
            instance.slug = request.POST.get('title')

        instance.author = request.user
        instance.save()
        return redirect('blog:home')
    return render(request, 'create.html', {'form': form})


@login_required(login_url='/users/log_in')
def delete_post(request, slug):
    post_data = Post.objects.get(slug=slug)
    if request.method == 'POST':
        post_data.delete()
        return redirect('blog:home')
    return render(request, 'delete_post.html', {'post': post_data})


@login_required(login_url='/users/log_in')
def edit_post(request, slug):
    post_data = Post.objects.get(slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post_data)
    if form.is_valid():
        form.save()
        return redirect('blog:post', slug=slug)
    return render(request, 'edit_post.html', {'form': form, 'post': post_data})


@login_required(login_url='/users/log_in')
def like(request, slug):
    post_data = Post.objects.get(slug=slug)

    if request.user not in post_data.likes.all():
        post_data.likes.add(request.user)
        post_data.dislikes.remove(request.user)
    elif request.user in post_data.likes.all():
        post_data.likes.remove(request.user)
    return redirect('blog:post', slug=slug)


@login_required(login_url='/users/log_in')
def dislike(request, slug):
    post_data = Post.objects.get(slug=slug)

    if request.user not in post_data.dislikes.all():
        post_data.dislikes.add(request.user)
        post_data.likes.remove(request.user)
    elif request.user in post_data.dislikes.all():
        post_data.dislikes.remove(request.user)
    return redirect('blog:post', slug=slug)


@login_required(login_url='/users/log_in')
def comment_delete(request, pk):
    comment = Comment.objects.get(pk=pk)

    if request.method == 'POST':
        comment.delete()
        return redirect('blog:post', slug=comment.post.slug)
    return render(request, 'comment_delete.html', {'post': comment.post})


@login_required(login_url='/users/log_in')
def comment_edit(request, pk):
    comment = Comment.objects.get(pk=pk)
    form = CommentForm(request.POST or None, instance=comment)

    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('blog:post', slug=comment.post.slug)
    return render(request, 'comment_edit.html', {'form': form, 'post': comment.post})
