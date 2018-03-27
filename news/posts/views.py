from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Article
from posts.forms import PostForm


def post_detail(request, post_id):
    return HttpResponse()


def author_detail(request, author_id):
    articles = Article.objects.filter(author_id=author_id)
    return render(
        request, 'posts/author_detail.html',
        {'articles': articles}
    )


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = PostForm()
    return render(
        request, 'post_create.html',
        {'form': form }
    )
