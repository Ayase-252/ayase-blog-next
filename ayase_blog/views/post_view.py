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
            if request.is_ajax():
                return HttpResponseNotFound(json.dumps({'error': 'Page not found'}))
            else:
                raise Http404
        if request.is_ajax():
            return HttpResponse(post.get_json())
        else:
            context = libs.get_common_context(post.title)
            context.update({
                'post': post.get_post(),
            })

            return render(request, 'post_new.html', context)


class PostsView(View):
    def get(self, request):
        queries = request.GET
        if 'from' in queries:
            from_uid = int(queries['from'])
        else:
            from_uid = None
        if 'max_pages' in queries:
            num_pages = int(queries['max_pages'])
        else:
            num_pages = 10
        try:
            posts = Post.data_api.get_posts_by_from(from_uid, num_pages)
        except:
            return HttpResponseServerError()

        res = {
            'num_page': len(posts),
            'pages': posts
        }

        return HttpResponse(res)
