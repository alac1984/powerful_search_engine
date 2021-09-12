from django.db import models


class Post(models.Model):
    blog_name = models.CharField(max_length=120)
    post_title = models.CharField(max_length=200)
    post_subtitle = models.CharField(max_length=200)
    post_text = models.TextField()
