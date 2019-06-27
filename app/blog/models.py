import uuid
from django.db import models
from django.contrib.auth import get_user_model


user_model = get_user_model()

def get_default_user():
    return user_model.objects.first()


class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    author = models.ForeignKey(user_model, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title