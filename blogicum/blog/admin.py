from django.contrib import admin
from blog.models import Category, Location, Post


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


admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Post, PostAdmin)
