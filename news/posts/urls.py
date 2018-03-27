from django.urls import path
from posts.views import post_detail, author_detail, post_create


urlpatterns = [
    path('<int:post_id>/', post_detail, name='post_detail'),
    path('author/<int:author_id>/', author_detail, name='author_detail'),
    path('post_create/', post_create, name='post_create')
]
