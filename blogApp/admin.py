from django.contrib import admin
from .models import Post, Author, Catogory

#add models to admin interface
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Catogory)