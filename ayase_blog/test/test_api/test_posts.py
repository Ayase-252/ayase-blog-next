from datetime import datetime

from django.test import TestCase, Client
from django.urls import reverse

from ...models.post import Post


def create_post(title, tags, content):
    return Post.data_api.create(title=title, tags=tags,
                               date=datetime.now(), content=content)


class TestPostsApi(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.posts = [create_post('post' + str(i), '', 'content post') for i in range(1, 11)]

    def test_ajax_api(self):
        c = Client()
        response = c.get(reverse('ayase_blog:posts'), {'from': 3, 'max_pages': 2})
        self.assertEqual(response.status_code, 200)
        res = response.json()
        self.assertEqual(res['num_page'],
                         2, 'num_page field in response is wrong.')
        self.assertEqual([page['postId'] for page in res['pages']], [3, 2])
