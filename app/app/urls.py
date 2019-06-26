from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('auth/', include('rest_framework.urls')),
        path('blog/', include('blog.api.urls')),
    ]))
]
