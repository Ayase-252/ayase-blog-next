"""
URL dispatcher of package
"""

from django.conf.urls import re_path
from django.urls import path
from .views.post_view import PostView, PostsView
from . import views_legacy

app_name = 'ayase-blog'
urlpatterns = [
    re_path(r'^$', views_legacy.home_page, name='index'),
    re_path(r'^category/(?P<category_url>[\w]+)/$', views_legacy.category, name='category'),
    re_path(r'^about/$', views_legacy.about, name='about'),
    re_path(r'^post/(?P<post_id>[0-9]+)/$', PostView.as_view(), name='post'),
    path('posts/', PostsView.as_view(), name='posts'),
    re_path(r'^expr/', views_legacy.expr),
]
