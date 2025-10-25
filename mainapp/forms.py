from django import forms
from .models import Comment

class CommentForm(Comment):
    class Meta:
        model = Comment
        fields = ('content')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Leave your name'}),
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Leave your comment'})
        }
        labels = {
            'name': 'Name',
            'comment': 'Comment'
        }