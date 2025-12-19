from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from blog.models import Category, Location, Post


User = get_user_model()


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'pub_date',
        'category',
        'is_published',
    )
    list_editable = (
        'is_published',
    )
    search_fields = ('title', 'text')
    list_filter = ('category', 'is_published', 'pub_date')
    list_display_links = ('title', 'author')


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'is_published',
    )
    list_editable = (
        'is_published',
    )
    search_fields = ('title', 'slug')
    list_filter = ('is_published',)
    list_display_links = ('title',)


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_published',
    )
    list_editable = (
        'is_published',
    )
    search_fields = ('name',)
    list_filter = ('is_published',)
    list_display_links = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)


class UserAdmin(BaseUserAdmin):
    list_display = (
        'username',
        'email',
        'is_staff',
        'posts_count',
    )

    @admin.display(description='Кол-во постов у пользователя')
    def posts_count(self, obj):
        return obj.posts.count()


admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
