from django.shortcuts import render


def index(request):
    template = 'blog/index.html'
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    return render(request, template, context)
