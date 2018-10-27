import json

from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseNotFound, \
HttpResponseServerError, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from ..models.post import Post
from ..serializers.post_serializer import PostSerializer

class PostsPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'

class PostView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'post_id'
        # try:
        #     post = Post.data_api.get_post_by_post_id(post_id)
        # except:
        #     raise Http404
        # if request.is_ajax():
        #     if 'application/json' in request.META['HTTP_ACCEPT']:
        #         post = post.get_post()
        #         res = json.dumps({
        #             'postId': post['id'],
        #             'title': post['title'],
        #             'content': post['content']
        #         })
        #         return HttpResponse(res, content_type='application/json')


class PostsView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-post_id')
    serializer_class = PostSerializer
    pagination_class = PostsPageNumberPagination
        # queries = request.GET
        # if 'from' in queries:
        #     from_uid = int(queries['from'])
        # else:
        #     from_uid = None
        # if 'maxPages' in queries:
        #     max_pages = int(queries['maxPages'])
        # else:
        #     max_pages = 10
        # try:
        #     posts = Post.data_api.get_posts_by_from(from_uid, max_pages)
        # except:
        #     return HttpResponseServerError()

        # posts = [post.get_post() for post in posts]

        # res = {
        #     'numPages': len(posts),
        #     'pages': [{'postId': post['id'], 'title': post['title'], 'content': post['content'] } for post in posts]
        # }
        # return HttpResponse(json.dumps(res), content_type='application/json')
