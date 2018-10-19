"""
Post

A single article
"""
import re
import json

import markdown
from django.db import models
from django.core.serializers.json import DjangoJSONEncoder

from .category import Category
from .. import ayaselibs as libs


class CallOut(models.Model):
    """
    Callout

    Tell viewers some extra information about your post.

    Attributes:
        level       Indicator of the severity of callout
        title       Title of the callout
        content     Content of the callout (Plain text)
    """
    CALLOUT_LEVEL = (('N', 'Common Notice'),
                     ('W', 'Warning'),
                     ('D', 'Danger'),
                     ('R', 'Recommend'))

    level = models.CharField(max_length=1, choices=CALLOUT_LEVEL)
    title = models.CharField(max_length=60)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_callout_info(self):
        """
        Get information about callout

        return:
            a dict containing information
        """
        return {
            'level': self.level,
            'title': self.title,
            'content': self.content
        }


class PostManager(models.Manager):
    """
    Data API for Post
    """
    def _get_queryset(self):
        """
        :return:
        """
        return super(PostManager, self).get_queryset().all()

    def get_posts_by_category(self, cat_url, limit=None):
        """
        Retrieve post list by category url.

        Arguments:
            cat_url     URL of category you want to search
        Options:
            limit       Default None
                        Maximum number of returning posts
        Return:
            List of posts in specified category
        """
        if limit is not None and limit < 0:
            raise ValueError('limit must be greater than 0, now it is {0}'
                             .format(limit))
        cat = Category.data_api.get_specific_category(cat_url)
        result = self._get_queryset().filter(category=cat).order_by('-date')
        if limit is not None:
            result = result[0:limit]
        return result

    def get_post_by_post_id(self, post_id):
        """
        Retrieve post by post ID

        Arguments:
            post_id     UID of post
        Return:
            Post if post indicated by post_id exists,
        """
        post = self._get_queryset().get(postId=post_id)
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
        if from_id:
            result.filter(postId__lte=from_id)
        return result[:min(len(result), limit)]

class Post(models.Model):
    """
    Post

    Attributes:
        postId      UID for post (Primary key)
        title       Title of post
        tags        Tags for the post, separated by ','
        category    Category to which the post belongs Foreign key to
                    Category
        date        Date time when the post is published
        content     Content in markdown notation

    """

    postId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    tags = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField()
    content = models.TextField()
    callout = models.ForeignKey(CallOut, on_delete=models.CASCADE,
                                null=True, blank=True)

    data_api = PostManager()

    class Meta:
        """
        Ordering the post by descending order of data
        """
        ordering = ["-date"]

    def __str__(self):
        return self.title

    def get_content(self):
        """
        Get post content converted to HTML

        return:
            Content converted to HTML
        """
        return markdown.markdown(self.content, output_format='html5')

    def get_plain_content(self):
        """
        Get post content whose HTML tags are stripped

        return:
            Plain content
        """
        return libs.strip_html_tags(self.get_content())

    def get_formatted_post(self):
        """
        Get all information regarding a post in a dict

        return:
            A dict containing information
            keywords:
            'title'     Post title
            'tags'      Tag list
            'date'      Date time when the post is published
            'category'  Name of category the post belongs to
            'content'   HTML document of content

        Note:   Deprecated
        """
        return {
            'title': self.title,
            'tags': str(self.tags).split(','),
            'date': self.date,
            'category': self.category.name,
            'content': self.get_content()
        }

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
            'id': self.postId,
            'title': self.title,
            'tags': str(self.tags).split(','),
            'date': self.date,
            'category': self.category.name,
            'content': self.get_content(),
            'callout': (self.callout.get_callout_info()
                        if self.callout is not None
                        else None)
        }

    def get_first_paragraph(self):
        """
        Get the content wrapped by first p tag

        return:
            Plain content wrapped by first p tag
        """
        paragraph = re.compile(r'<p>(?P<text>.*)</p>')
        raw_text = self.get_content()
        matched_text = paragraph.search(raw_text).group('text')
        return matched_text

    def get_json(self):
        """
        Get JSON of post for asynchorus request

        return: 
            JSON of post
        """
        return json.dumps(self.get_post(), cls = DjangoJSONEncoder)

