from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.

def index(request):
	# get the blog Post that r published
	posts = Post.objects.filter(published=True)

	#now return the rendered template
	return render(request, 'blog/index.html', {'posts': posts})

def post(request, slug):
	#get thPost object
	post = get_object_or_404(Post, slug=slug)

	#now return the rendered template
	return render (request, 'blog/post.html',{'post':post})
