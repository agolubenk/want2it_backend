from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': '4', 'class': 'form-control', 'placeholder':'Ваш комментарий'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ваше имя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'E-mail'}))

    class Meta:
        model = Comment
        fields = ('author', 'email', 'text')