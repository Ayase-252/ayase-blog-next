import json

from django.test import TestCase, Client
from django.urls import reverse

from . import util


class TestPostAPI(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = util.create_post(
            'hello world', '[hello, world]', 'Hello world')

    def test_AJAX_GET(self):
        client = util.create_AJAX_client()
        res = client.get(reverse('ayase_blog:post', kwargs={'post_id': 1}))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res['Content-Type'], 'application/json')
        response = json.loads(res.content)
        self.assertEqual(response['title'], 'hello world')
        self.assertEqual(response['postId'], 1)

        # if no page with requested post id
        res = client.get(reverse('ayase_blog:post', kwargs={'post_id': 2}))
        self.assertEqual(res.status_code, 404)
