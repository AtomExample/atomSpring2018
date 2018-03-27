from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Article


def post_detail(request, post_id):
    return HttpResponse()


def author_detail(request, author_id):
    articles = Article.objects.filter(author_id=author_id)
    return render(
        request, 'posts/author_detail.html',
        {'articles': articles}
    )
