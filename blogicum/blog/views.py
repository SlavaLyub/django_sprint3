from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post, Category


def get_posts():
    return Post.objects.select_related(
        'location',
        'category',
        'author',
    ).filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
    )


def index(request):
    template = 'blog/index.html'
    posts_index_list = get_posts()[:5]
    context = {'post_list': posts_index_list}
    return render(request, template, context)


def post_detail(request, post_id):
    post = get_object_or_404(
        get_posts(),
        pk=post_id,
    )
    context = {'post': post}
    template = 'blog/detail.html'
    return render(request, template, context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category.objects.filter(
            is_published=True
        ),
        slug=category_slug,
    )
    post_list = get_posts().filter(
        category__slug=category_slug,
    )

    context = {
        'category': category,
        'post_list': post_list,
    }
    template = 'blog/category.html'
    return render(request, template, context)
