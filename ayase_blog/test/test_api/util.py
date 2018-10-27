from django.test import Client
from django.utils import timezone

from ...models.post import Post

def create_post(title, tags, content):
    return Post.objects.create(title=title, tags=tags,
                               date=timezone.now(), content=content)

def create_AJAX_client():
    return Client(HTTP_ACCEPT='application/json', HTTP_X_REQUESTED_WITH='XMLHttpRequest')
