from django import forms
from .models import Blog, Comment


class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']


class UpdateBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']

class CreateComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'body']