# getting forms
from django import forms

# getting models
from .models import Post

# making a class objects
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
