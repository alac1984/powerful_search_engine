from django.db import models
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex


class Post(models.Model):
    blog_name = models.CharField(max_length=120)
    post_url = models.URLField()
    post_title = models.CharField(max_length=120)
    post_subtitle = models.TextField()
    post_text = models.TextField()
    vector_column = SearchVectorField(null=True)

    class Meta:
        indexes = (GinIndex(fields=['vector_column']),)
