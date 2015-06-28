# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from blog.models import Post

def index(request):
	all_posts = Post.objects.all()
	paginator = Paginator(all_posts, 5)
	page = request.GET.get('page')

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	return render(request, 'blog/blog_index.html', {'posts': posts})

def post(request, slug):
	post = get_object_or_404(Post, slug=slug)
	return render(request, 'blog/post.html', {'post': post})