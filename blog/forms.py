from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    """Form for creating and editing a blog post."""
    class Meta:
        model = BlogPost
        fields = ['title', 'content']
