from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from .forms import PostForm

 # render page using index.html as template and load all posts into a list
def index(request):
    posts = Post.objects.all().order_by('create_date')

    form = PostForm(request.POST or None)
    if form.is_valid():
       form.save()

    return render(request, 'blogApp/index.html', {'posts':posts, 'form':form})

 # render page using post.html as template and load the post of interest, lists by categoty and lists by author
def detail(request, post_id):
   post = Post.objects.get(pk = post_id)
   posts_by_category = Post.objects.filter(catogory = post.catogory)
   posts_by_author = Post.objects.filter(author = post.author)


   return render(request, 'blogApp/post.html', {'post':post, 'post_by_category':posts_by_category, 'post_by_author':posts_by_author})

 # render page using newPost.html as template and load the form
def create_post(request):
   form = PostForm(request.POST or None)
   if form.is_valid():
      form.save()
   return render(request, 'blogApp/newPost.html', {'form':form})
