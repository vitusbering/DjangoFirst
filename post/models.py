from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE,)
    body = models.TextField()

    def __str__(self):
        return self.title