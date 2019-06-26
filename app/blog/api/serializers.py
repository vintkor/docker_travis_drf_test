from rest_framework import serializers
from ..models import (
    Category,
    Post,
)


class CategorySerializer(serializers.ModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name='category-detail')

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'created',
            'link',
        )
        read_only_fields = (
            'id',
        )


class PostSerializer(serializers.ModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name='post-detail')

    class Meta:
        model = Post
        fields = (
            'id',
            'category_id',
            'title',
            'created',
            'link',
        )
        read_only_fields = (
            'id',
        )
