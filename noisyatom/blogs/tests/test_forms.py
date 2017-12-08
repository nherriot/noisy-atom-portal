from django.test import TestCase
from django.utils.text import slugify
from django.utils import timezone

from blogs.forms import PostForm
from blogs.models import Post


'''
the content and publish are required is different so we need to import timezone first
'''
class PostFormTest(TestCase):
    def test_valid_form(self):
        title = 'New title in the form'
        slug  = 'new-slug-in-the-new-forms'
        content = 'hello worlds'
        obj   = Post.objects.create(title=title, slug=slug, content=content, publish=timezone.now())
        #print('The object: ', obj)
        data  = {'title': obj.title, 'slug': obj.slug, 'content': obj.content, 'publish': obj.publish}

        form  = PostForm(data=data) # is like to say PostForm(request.POST)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data.get('title'), obj.title)
        self.assertNotEqual(form.cleaned_data.get('content'), 'Another new content')

    def test_publish_field_missing_in_form(self):
        title = 'New title in the form'
        slug  = 'new-slug-in-the-new-forms'
        content = 'hello worlds'
        obj   = Post.objects.create(title=title, slug=slug, content=content, publish=timezone.now())
        #print('The object: ', obj)
        data  = {'title': obj.title, 'slug': obj.slug, 'content': obj.content, 'publish': ''}

        form  = PostForm(data=data) # is like to say PostForm(request.POST)
        self.assertFalse(form.is_valid())
        #print('The content mut not be empty: ', form.errors)
        self.assertTrue(form.errors)

