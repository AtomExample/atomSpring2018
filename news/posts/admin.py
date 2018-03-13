from django.contrib import admin
from posts.models import Article


class ArticleAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', )


admin.site.register(Article, ArticleAdmin)
