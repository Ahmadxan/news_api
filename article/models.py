from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False, null=False)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Commit(models.Model):
    full_name = models.CharField(max_length=100)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.article