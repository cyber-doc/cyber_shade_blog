from django.db import models
from users.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    reply_to = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
