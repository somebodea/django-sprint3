from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now

from .constants import N_POSTS_PER_PAGE
from .models import Post, Category


def filter_published_posts(queryset):
    """Фильтрует переданный QuerySet и делает select_related."""
    return queryset.select_related(
        'category', 'location', 'author'
    ).filter(
        pub_date__lte=now(),
        is_published=True,
        category__is_published=True,
    )


def index(request):
    """
    Функция, которая выводит страницу "Главная" с сортировкой постов.
    От самого нового к старому.
    """
    posts_list = filter_published_posts(Post.objects)[:N_POSTS_PER_PAGE]
    return render(request, 'blog/index.html', {'post_list': posts_list})


def post_detail(request, post_id):
    """Функция, которая выводит страницу полного поста."""
    post = get_object_or_404(
        filter_published_posts(Post.objects),
        id=post_id,
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    """Функция, которая выводит страницу постов по определенной категории."""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = filter_published_posts(category.posts)

    return render(
        request,
        'blog/category.html',
        {'category': category, 'post_list': post_list}
    )
