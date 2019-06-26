from django.contrib import admin
from .models import (
    Category,
    Post,
)


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = (
        'title',
        'created',
    )
    readonly_fields = (
        'id',
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'created',
    )
    readonly_fields = (
        'id',
    )
