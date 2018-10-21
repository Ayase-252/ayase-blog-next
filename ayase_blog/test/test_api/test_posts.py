from datetime import datetime

from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from ...models.post import Post
from . util import create_post, create_AJAX_client


class TestPostsAPI(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.posts = [create_post('post' + str(i), '', 'content post')
                     for i in range(1, 11)]

    def test_ajax_get(self):
        c = create_AJAX_client()
        response = c.get(reverse('ayase_blog:posts'),
                         {'from': 3, 'max_pages': 2})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        res = response.json()
        self.assertEqual(res['num_page'],
                         2, 'num_page field in response is wrong.')
        self.assertEqual([page['postId'] for page in res['pages']], [3, 2])

        response = c.get(reverse('ayase_blog:posts'),
                         {'from': 3, 'max_pages': 4})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        res = response.json()
        self.assertEqual(res['num_page'],
                         3, 'num_page field in response is wrong.')
        self.assertEqual([page['postId'] for page in res['pages']], [3, 2, 1])