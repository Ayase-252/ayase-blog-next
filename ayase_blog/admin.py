from django.contrib import admin

# Register your models here.
from .models.category import Category
from .models.post import Post, CallOut
from .models.site import Site

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Site)
admin.site.register(CallOut)