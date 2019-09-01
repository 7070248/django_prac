from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    content = models.TextField()
    writer = models.CharField(max_length=200)