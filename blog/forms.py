from django import forms
from .models import Comment, Post


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

