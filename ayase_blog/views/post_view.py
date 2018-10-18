import json

from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.views import View

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
        queries = request.GET.get_dict()
        if queries == "POST":
            from_uid = queries['from']
            num_pages = queries['pages']
        else:
            num_pages = 10
        
           