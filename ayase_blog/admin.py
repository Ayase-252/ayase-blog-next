from django.contrib import admin

# Register your models here.
from .models.post import Post
from .models.site import Site

admin.site.register(Post)
admin.site.register(Site)