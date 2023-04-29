from django import forms
from .models import *


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input'}
    ), label='Название поста')
    text = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'textarea', 'size': '40'}
    ), label='Текст поста')
    image = forms.ImageField(label='Картинка для поста', required=False)

    class Meta:
        model = Post
        fields = ['title', 'text', 'image']
