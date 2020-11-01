from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .models import Post
from .forms import PostForm


 # render page using index.html as template and load all posts into a list
def index(request):
    posts = Post.objects.all().order_by('create_date')



    return render(request, 'blogApp/index.html', {'posts':posts})

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
      messages.success(request,'Post added successfully!')
   return render(request, 'blogApp/newPost.html', {'form':form})

 # render page using update.html as template; updates existing posts
def update_post(request, post_id):
   post = Post.objects.get(pk = post_id)
   data ={'title': post.title, 'create_date':post.create_date, 'author': post.author, 'category':post.catogory,'description':post.description, 'body':post.body, 'image_url':post.image_url}
   
   if request.method == 'POST':
      form = PostForm(request.POST, instance = post)
      if form.is_valid():
         form.save()
         messages.success(request,'Post updated successfully!')
   else:
      
      form = PostForm(initial = data)
   return render(request, 'blogApp/update.html', {'form':form})
