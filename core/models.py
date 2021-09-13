from django.db import models


class Post(models.Model):
    blog_name = models.CharField(max_length=120)
    post_url = models.URLField()
    post_title = models.CharField(max_length=120)
    post_subtitle = models.TextField()
    post_text = models.TextField()
