from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from blog.models import Post
from blog.forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def blog(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 2)
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    context = {'posts':posts}
    return render(request, 'blog/blog.html', context)


def post(request, id):
    post = get_object_or_404(Post, id=id)
    context = {'post': post}
    return render(request, 'blog/post.html', context)


@login_required()
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
        return redirect('blog')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})


@login_required()
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user == post.author:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
            messages.success(request, "Post successfully edited.")
            return redirect('blog')
        else:
            form = PostForm(instance=post)
    else:
        messages.error(request, "You are not a authenticated user.")
        return redirect('blog')
    return render(request, 'blog/edit_post.html', {'form': form})


@login_required()
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user == post.author:
        post.delete()
        messages.success(request, "Post successfully deleted.")
        return redirect('blog')
    else:
        messages.error(request, "You are not a authenticated user.")
        return redirect('post', id=post.id)

