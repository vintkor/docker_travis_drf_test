from rest_framework import generics, permissions
from ..models import (
    Category,
    Post,
)
from .serializers import (
    PostSerializer,
    CategorySerializer,
)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def blog_root(request, format=None):
    return Response({
        'post': reverse('post-list', request=request, format=format),
        'category': reverse('category-list', request=request, format=format),
    })


class CategoryListApiView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]


class CategoryDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]


class PostListApiView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [permissions.AllowAny]


class PostDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [permissions.AllowAny]
