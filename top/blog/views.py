from django.shortcuts import render, redirect
from .models import *  # импортирование модели
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/users/log_in')
def home(request):
    posts = Post.objects.all()  # запрос в базу данных
    # print(courses[0].description)
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
