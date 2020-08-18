from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects
    posts_list=Post.objects.all()
    paginator = Paginator(posts_list,3)
    page = request.GET.get('page')
    posts_num = paginator.get_page(page)

    return render(request, 'home.html', {'posts' : posts_num, 'blogs': posts})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post': post_detail})

def new(request):
    return render(request, 'post/new.html')

def create(request):
    post = Post()
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect('/blog/' + str(post.id))

def delete(request, post_id):
    post_nim = get_object_or_404(Post, pk=post_id)
    post_num.delete()
    return redirect('/')