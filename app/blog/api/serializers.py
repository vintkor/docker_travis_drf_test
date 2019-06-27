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
    author_username = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id',
            'category',
            'title',
            'author_username',
            'created',
            'link',
        )
        read_only_fields = (
            'id',
        )

    def get_author_username(self, obj):
        return obj.author.username if obj.author else None

    def update(self, instance, validated_data):
        if not instance.author:
            instance.author = self.context['request'].user
        return super(PostSerializer, self).update(instance, validated_data)
