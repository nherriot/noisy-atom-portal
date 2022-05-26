from django import forms
#from django.forms import extras
#from pagedown.widgets import PagedownWidget
from pagedown.widgets import AdminPagedownWidget
from .models import Post


class PostForm(forms.ModelForm):
    #content = forms.CharField(widget=PagedownWidget(show_preview=False))
    #publish = forms.DateField(widget=forms.SelectDateWidget)
    publish = forms.DateField(widget=forms.widgets.SelectDateWidget())

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
            'draft',
            'publish',
        ]
