from datetime import datetime

from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from ...models.post import Post
from .util import create_post, create_AJAX_client


class TestPostsAPI(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.posts = [create_post('post' + str(i), '', 'content post')
                     for i in range(1, 11)]

    def test_ajax_get(self):
        c = create_AJAX_client()
        response = c.get(reverse('ayase_blog:posts'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        res = response.json()
        self.assertEqual([page['post_id'] for page in res['results']], [10, 9, 8, 7, 6])

        response = c.get(reverse('ayase_blog:posts'), {'page': 2})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        res = response.json()
        self.assertEqual([page['post_id'] for page in res['results']], [5, 4, 3, 2, 1])
