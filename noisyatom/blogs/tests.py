
from django.test import TestCase

from blogs.models import Post

class PostModelTest(TestCase):

	def setUp(self):
		self.post = Post.objects.create(title='New title test', slug='first-new-title-test-created')


	def test_create_title(self):
		obj = Post.objects.get(slug='first-new-title-test-created')

		self.assertEqual(obj.title, 'New title test')
	
