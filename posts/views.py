from django.shortcuts import render, redirect 
# Post 모델을 import
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,

    }
    return render(request, 'index.html', context)

def detail(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post,
    }
    return render(request, 'detail.html', context )
    
def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    # 새로운 게시물을 만들 때 
    post = Post()
    post.title = title # 변수 할당 
    post.conten = content
    post.save()

    return redirect(f'/posts/{post.id}')

def delete(request, id):
    post = Post.objects.get(id=id) # 찾는 코드
    post.delete()

    return redirect('/index/')
def edit(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post,
    }
    # render는 html을 보여주기 위한 것 
    return render(request,'edit.html', context)

def update(request, id):
    

    # 방금 수정한 데이터
    title = request.GET.get('title')
    content = request.GET.get('content')

    # post = Post() -> 새로운 게시물 만들 때 
    # 기존데이터
    post = Post.objects.get(id=id)
    post.title = title
    post.conten = content
    post.save()

    return redirect(f'/posts/{post.id}')
