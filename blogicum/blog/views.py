from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blog.models import Post, Category


def index(request):
    template = 'blog/index.html'
    posts_index_list = Post.objects.select_related(
        'category',
        'author',
        'location',
    ).filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
    )[:5]
    context = {'post_list': posts_index_list}
    return render(request, template, context)


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects.select_related(
            'location',
            'category'
        ).filter(
            is_published=True,
            pub_date__lte=timezone.now(),
            category__is_published=True,
        ),
        pk=post_id,
    )
    context = {'post': post}
    template = 'blog/detail.html'
    return render(request, template, context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category.objects.filter(
            slug=category_slug,
            is_published=True,
        )
    )

    post_list = Post.objects.select_related(
        'location',
        'category',
        'author'
    ).filter(
        is_published__exact=True,
        pub_date__lte=timezone.now(),
        category__slug=category_slug,
    )

    context = {
        'category': category,
        'post_list': post_list,
    }
    template = 'blog/category.html'
    return render(request, template, context)
