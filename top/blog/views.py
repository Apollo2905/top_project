from django.shortcuts import render, redirect
from .models import *  # импортирование модели
from .models import Post
from .forms import PostForm


def home(request):
    posts = Post.objects.all()  # запрос в базу данных
    # print(courses[0].description)
    return render(request, 'home.html', {'posts': posts})  # отправка в html


def post(request, slug):
    post_detail = Post.objects.get(slug=slug)
    # print(post_detail.title)
    # print(post_detail.text)
    # print(post_detail.image)
    return render(request, 'post.html', {'post': post_detail})


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


def delete_post(request, slug):
    post_data = Post.objects.get(slug=slug)
    if request.method == 'POST':
        post_data.delete()
        return redirect('blog:home')
    return render(request, 'delete_post.html', {'post': post_data})


def edit_post(request, slug):
    post_data = Post.objects.get(slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post_data)
    if form.is_valid():
        form.save()
        return redirect('blog:post', slug=slug)
    return render(request, 'edit_post.html', {'form': form, 'post': post_data})
