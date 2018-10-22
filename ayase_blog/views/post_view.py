import json

from django.views import View
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseNotFound, \
HttpResponseServerError, JsonResponse

from ..models.post import Post
from .. import ayaselibs as libs


class PostView(View):
    def get(self, request, post_id):
        try:
            post = Post.data_api.get_post_by_post_id(post_id)
        except:
            raise Http404
        if request.is_ajax():
            if 'application/json' in request.META['HTTP_ACCEPT']:
                post = post.get_post()
                res = json.dumps({
                    'postId': post['id'],
                    'title': post['title'],
                    'content': post['content']
                })
                return HttpResponse(res, content_type='application/json')


class PostsView(View):
    def get(self, request):
        queries = request.GET
        if 'from' in queries:
            from_uid = int(queries['from'])
        else:
            from_uid = None
        if 'maxPages' in queries:
            num_pages = int(queries['maxPages'])
        else:
            num_pages = 10
        try:
            posts = Post.data_api.get_posts_by_from(from_uid, num_pages)
        except:
            return HttpResponseServerError()

        posts = [post.get_post() for post in posts]

        res = {
            'numPages': len(posts),
            'pages': [{'postId': post['id'], 'title': post['title'], 'content': post['content'] } for post in posts]
        }

        return HttpResponse(json.dumps(res), content_type='application/json')
