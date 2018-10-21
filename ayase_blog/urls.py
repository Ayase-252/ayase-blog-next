"""
URL dispatcher of package
"""

from django.conf.urls import re_path
from django.urls import path
from .views.post_view import PostView, PostsView
from . import views_legacy

app_name = 'ayase-blog'
urlpatterns = [
    path('post/<int:post_id>', PostView.as_view(), name='post'),
    path('posts/', PostsView.as_view(), name='posts'),
]
