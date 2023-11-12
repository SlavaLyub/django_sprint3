from django.shortcuts import render, get_object_or_404

from blog.constants import NUMBER_OF_POSTS

from .models import Post, Category


def index(request):
    template = 'blog/index.html'
    posts_index_list = Post.published.get_queryset().order_by(
        '-pub_date'
    )[:NUMBER_OF_POSTS]
    context = {'post_list': posts_index_list}
    return render(request, template, context)


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.published,
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
    post_list = Post.published.get_queryset().filter(
        category__slug=category_slug,
    )

    context = {
        'category': category,
        'post_list': post_list,
    }
    template = 'blog/category.html'
    return render(request, template, context)
