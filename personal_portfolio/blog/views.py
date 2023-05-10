from django.shortcuts import render, redirect
from blog.models import Post, Comment

from .forms import CommentForm, CreateBlogForm

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data["author"],
                body = form.cleaned_data["body"],
                post=post
            )
            comment.save()


    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form":form,
    }
    return render(request, "blog_detail.html", context)

def create_blog(request):
    if request.method == 'GET':
        context = {'form': CreateBlogForm()}
        return render(request, 'create_blog.html', context)
    elif request.method == 'POST':
        form = CreateBlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_index')
        else:
            return render(request, 'create_blog.html', {'form': form})