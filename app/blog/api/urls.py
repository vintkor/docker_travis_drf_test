from django.urls import path
from .views import (
    CategoryListApiView,
    CategoryDetailApiView,
    PostListApiView,
    PostDetailApiView,
    blog_root,
)

urlpatterns = [
    path(r'', blog_root),
    path('category/', CategoryListApiView.as_view(), name='category-list'),
    path('category/<str:pk>/', CategoryDetailApiView.as_view(), name='category-detail'),

    path('post/', PostListApiView.as_view(), name='post-list'),
    path('post/<str:pk>/', PostDetailApiView.as_view(), name='post-detail'),
]
