
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils.text import slugify


from blogs.models import Post


class PostModelTest(TestCase):

    def create_post(self, title='Post new blog'):
        return Post.objects.create(title=title)

    def test_lis_views(self):
        url = reverse('blogs:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_detail_views(self):
        obj = self.create_post(title='Some new title for new test')
        response = self.client.get(obj.get_absolute_url())
        self.assertEqual(response.status_code, 200)


    def test_update_views(self):
        obj = self.create_post(title='Some new title for new test')
        url = reverse('blogs:updated', kwargs={'slug': obj.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


    def test_delete_views(self):
        obj = self.create_post(title='Some new title for new test')
        url = reverse('blogs:delete', kwargs={'slug': obj.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


