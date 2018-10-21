"""
Post

A single article
"""
import re
import json

import markdown
from django.db import models
from django.core.serializers.json import DjangoJSONEncoder

from .. import ayaselibs as libs

class PostManager(models.Manager):
    """
    Data API for Post
    """
    def _get_queryset(self):
        """
        :return:
        """
        return super(PostManager, self).get_queryset().all()

    def get_post_by_post_id(self, post_id):
        """
        Retrieve post by post ID

        Arguments:
            post_id     UID of post
        Return:
            Post if post indicated by post_id exists,
        """
        post = self._get_queryset().get(post_id=post_id)
        return post

    def get_posts(self, limit=None):
        """
        Retrieve posts descending by date

        Options:
            limit   Default None indicating for all
                    Maximum number of returning posts
        Return:
            List of posts
        """
        if limit is not None and limit < 0:
            raise ValueError('limit must be greater than 0, now it is {0}'
                             .format(limit))
        result = self._get_queryset()
        if limit is not None:
            result = result[0:limit]
        return result

    def get_posts_by_from(self, from_id, limit=10):
        """Get posts by from idx limiting by limit
        
        Arguments:
            from_id {[integer]} -- [id to fetch from]
            limit {[integer]} -- [maximun number of returning posts]
        """
        result = self._get_queryset()
        if from_id is not None:
            result = result.filter(post_id__lte=from_id).order_by('-post_id')
        return result[:min(len(result), limit)]

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

    data_api = PostManager()

    def __str__(self):
        return self.title

    def _get_content(self):
        """
        Get post content converted to HTML

        return:
            Content converted to HTML
        """
        return markdown.markdown(self.content, output_format='html5')

    def get_post(self):
        """
        Get all information regarding a post in a dict

        return:
            A dict containing information
            keywords:
            'id'        UID of post
            'title'     Post title
            'tags'      Tag list
            'date'      Date time when the post is published
            'category'  Name of category the post belongs to
            'content'   HTML document of content
            'callout'   Callout attached to the post
        """
        return {
            'id': self.post_id,
            'title': self.title,
            'tags': str(self.tags).split(','),
            'date': self.date.strftime('%Y-%m-%d %H:%M'),
            'content': self._get_content()
        }
