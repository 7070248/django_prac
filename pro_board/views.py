from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Comment


def index(request):
    return HttpResponse('보드에 오신것을 환영합니다!')


def post_list(request):
    posts = Post.objects.all().order_by('-pub_date')
    context = {
        'posts': posts
    }
    return render(request, 'pro_board/index.html', context=context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post,
        'comments': post.comment_set.all()
    }
    return render(request, 'pro_board/detail.html', context=context)


def create_post(request):
    # 저장하는거
    if request.method == 'POST':
        post_data = request.POST
        title = post_data.get('title')
        content = post_data.get('content')
        post = Post.objects.create(title=title, content=content)
        return redirect('post_detail', post_id=post.id)
    # get --> 작성하기 페이지로 가는거
    else:
        return render(request, 'pro_board/create_post.html')


def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('post_list')


def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':  # 수정하는거
        post_data = request.POST

        post.title = post_data.get('title')
        post.content = post_data.get('content')
        post.save()
        return redirect('post_detail', post_id=post.id)

    else:  # 수정하는 페이지로 가기
        context = {
            'post': post,
        }
        return render(request, 'pro_board/update_post.html', context=context)


def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    data = request.POST
    content = data.get('content')
    writer = data.get('writer')
    Comment.objects.create(post=post, content=content, writer=writer)
    return redirect('post_detail', post_id)
