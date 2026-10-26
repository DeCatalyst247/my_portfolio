from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Post


def post_list(request):
    posts = Post.objects.filter(
        status="published",
        published_at__lte=timezone.now(),
    )

    context = {
        "posts": posts,
    }

    return render(request, "blog/post_list.html", context)


def post_detail(request, slug):
    post = get_object_or_404(
        Post,
        slug=slug,
        status="published",
        published_at__lte=timezone.now(),
    )

    context = {
        "post": post,
    }

    return render(request, "blog/post_detail.html", context)