from .import models
from django import forms


class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Articles
        fields = ('title', 'author', 'body')