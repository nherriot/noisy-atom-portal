from django import forms
from pagedown.widgets import PagedownWidget
from .models import Post


class PostForm(forms.ModelForm):
    # content = forms.CharField(widget=PagedownWidget())
    #publish = forms.DateField(widget=forms.SelectDateWidget)
    publish = forms.DateField(widget=forms.widgets.SelectDateWidget())

    class Meta:
        model = Post
        fields = '__all__'
