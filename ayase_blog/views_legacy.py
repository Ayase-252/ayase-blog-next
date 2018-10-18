import json

from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.views import View

from .models.category import Category
from .models.post import Post
from .models.site import Site
from . import ayaselibs as libs


def home_page(request):
    """
    Render home page
    """
    posts = Post.data_api.get_posts()
    posts_list = []
    for post in posts:
        post_instance = post.get_post()
        post_instance['short_description'] = post.get_first_paragraph()
        posts_list.append(post_instance)
    context = libs.get_common_context('Home Page')
    context.update({
        'posts_list': posts_list,
    })
    return render(request, 'index_new.html', context)

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

def category(request, category_url):
    try:
        posts = Post.data_api.get_posts_by_category(category_url)
    except:
        raise Http404
    posts_list = []
    cat = Category.data_api.get_specific_category(category_url)
    for post in posts:
        post_instance = post.get_post()
        post_instance['short_description'] = post.get_first_paragraph()
        posts_list.append(post_instance)
    context = libs.get_common_context(cat.name)
    context.update({
        'post_list': posts_list
    })
    return render(request, 'index_new.html', context)


def about(request):
    post = {
        'title': 'About me',
        'content': Site.get_about()
    }
    context = libs.get_common_context()
    context.update({
        'post': post
    })
    return render(request, 'post_new.html', context)


def expr(request):
    return render(request, "post_style.html")
