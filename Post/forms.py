from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'mood', 'type', 'date_published']
        widgets = {
            'user': forms.HiddenInput(),
        }
