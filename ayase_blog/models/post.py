"""
Post

A single article
"""
import re
import json

import markdown
from django.db import models
from django.core.serializers.json import DjangoJSONEncoder
        
class Post(models.Model):
    """
    Post

    Attributes:
        post_id     UID for post (Primary key)
        title       Title of post
        tags        Tags for the post, separated by ','
        category    Category to which the post belongs Foreign key to
                    Category
        date        Date time when the post is published
        content     Content in markdown notation

    """

    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    tags = models.CharField(max_length=100)
    date = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return self.title
