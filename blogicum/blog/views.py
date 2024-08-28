from django.shortcuts import get_object_or_404, render  # type: ignore

from blog.models import Post, Category

from django.utils import timezone


def index(request):
    template = "blog/index.html"
    post_list = (
        Post.objects.select_related('author', 'location', 'category')
        .filter(
            pub_date__lte=timezone.now(), is_published=True,
            category__is_published=True
        )[:5]
    )
    context = {
        "post_list": post_list,
    }
    return render(request, template, context)


def post_detail(request, post_id):
    template = "blog/detail.html"
    post = get_object_or_404(
        Post.objects.filter(
            pub_date__lt=timezone.now(), is_published=True,
            category__is_published=True
        ),
        id=post_id,
    )
    context = {"post": post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = "blog/category.html"
    category = get_object_or_404(
        Category.objects.filter(is_published=True),
        slug=category_slug,
    )
    post_list = Post.objects.all().filter(
        category=category, is_published=True, pub_date__lte=timezone.now()
    )
    context = {"category": category, "post_list": post_list}
    return render(request, template, context)
