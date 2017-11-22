
from django.core.urlresolvers import reverse
from django.test import TestCase


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
		'''
			The reason of why we use 404 because in the  update_post I am using the if statment 
			say if not request.user.is_staff or superuser than get 404 if I change the if statment to
			if request.user.is_staff or superuser than change the 404 to 200 the same for the delete method
		'''
		obj = self.create_post(title='Some new title for new test')
		obj.save()
		url = reverse('blogs:updated', kwargs={'slug': obj.slug})
		response = self.client.get(url)
		self.assertEqual(response.status_code, 404)


	def test_delete_views(self):
		obj = self.create_post(title='Some new title for new test')
		url = reverse('blogs:delete', kwargs={'slug': obj.slug})
		response = self.client.get(url)
		self.assertEqual(response.status_code, 404)


