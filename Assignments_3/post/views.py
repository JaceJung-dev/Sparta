from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.http import HttpResponse


def post_list(request):
    posts = Post.objects.all().order_by("-id")
    context = {"posts": posts}
    return render(request, "post/post_list.html", context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {"post": post}
    return render(request, "post/post_detail.html", context)


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect("post:detail", post.pk)
    else:
        form = PostForm()
    context = {"form": form}
    return render(request, "post/post_create.html", context)


def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("post:list")
    return redirect("post:detail", post.pk)


def post_update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect("post:detail", post.pk)
    else:
        form = PostForm(instance=post)
    context = {
        "form": form,
        "post": post,
    }
    return render(request, "post/post_update.html", context)
