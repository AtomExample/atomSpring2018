from django.db import models
from django.conf import settings


class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    preview = models.TextField(blank=True, null=True)
    author = models.ForeignKey(
        on_delete=models.CASCADE, to=settings.AUTH_USER_MODEL
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
