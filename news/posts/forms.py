from django import forms
from posts.models import Article

class PostForm(forms.ModelForm):
    
    class Meta:
        fields = ('title', 'text', 'author')
        model = Article
