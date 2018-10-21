"""
Test cases for models in post.py

This file contains test cases for models in post.py.
"""
from datetime import datetime, timedelta
import unittest

from django.test import TestCase

from ..models.category import Category
from ..models.post import Post, CallOut


class PostManagerTests(TestCase):
    """
    Test class for Post manager
    """

    @classmethod
    def setUpTestData(cls):
        cls.time = datetime.now()
        cls.post_1 = Post(title='title1',
                          tags='tag1,tag2',
                          date=cls.time  - timedelta(days=1),
                          content='test content')
        cls.post_2 = Post(title='title2',
                          tags='tag1',
                          date=cls.time,
                          content='test content')
        cls.post_1.save()
        cls.post_2.save()

    def test_get_post_by_post_id(self):
        """
        get_post_by_post_id should return the post whose id is given
        """
        post = Post.data_api.get_post_by_post_id(1)
        self.assertEqual(post, self.post_1)

    def test_get_posts_all_posts(self):
        """
        get_posts should return all posts in database in order of descending
        date in condition that limit karg is not given.
        """
        posts = Post.data_api.get_posts()
        self.assertQuerysetEqual(posts, [self.post_2, self.post_1])

    def test_get_posts_limited_posts(self):
        """
        get_posts should return posts up to limit specified.
        """
        posts = Post.data_api.get_posts(limit=1)
        self.assertQuerysetEqual(posts, [self.post_2])

    def test_get_posts_given_by_from_id_with_limit(self):
        posts = Post.data_api.get_posts_by_from(2, 1)
        self.assertQuerysetEqual(posts, [self.post_2])

        posts = Post.data_api.get_posts_by_from(2, 2)
        self.assertQuerysetEqual(posts, [self.post_2, self.post_1])

        posts = Post.data_api.get_posts_by_from(2, 3)
        self.assertQuerysetEqual(posts, [self.post_2, self.post_1])
