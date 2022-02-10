from django import forms

from pagedown.widgets import AdminPagedownWidget

from .models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget)
    publish = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
            'draft',
            'publish',
        ]
