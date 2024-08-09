from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from blog_app.models import Post


def post_list(request):
    posts = Post.objects.filter(published_at__isnull=False)
    return render(
        request,
        "post_list.html",
        {"posts": posts},
    )


def post_detail(request, pk):
    post = Post.objects.get(pk=pk, published_at__isnull=False)
    return render(
        request,
        "post_detail.html",
        {"post": post},
    )


@login_required
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect("post-list")


@login_required
def draft_list(request):
    posts = Post.objects.filter(published_at__isnull=True)
    return render(
        request,
        "draft_list.html",
        {"posts": posts},
    )


@login_required
def draft_detail(request, pk):
    post = Post.objects.get(pk=pk, published_at__isnull=True)
    return render(
        request,
        "draft_detail.html",
        {"post": post},
    )
