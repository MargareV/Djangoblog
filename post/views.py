from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
# Create your views here.
def index(request):
	#return HttpResponse('Hello From Post!')

	posts = Posts.objects.all()[:10]

	context = {
	'title' : 'Latest Posts',
	'posts' : posts
	}

	return render(request, 'posts/index.html', context)

def detail(request, id):
		post = Posts.objects.get(id=id)

		context = {
		'post' : post
		}
		return render(request, 'posts/detail.html', context)

	