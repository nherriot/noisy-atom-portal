
from django.test import TestCase
from django.utils.text import slugify

from blogs.models import Post


class PostModelTest(TestCase):

	def setUp(self):
		self.post = Post.objects.create(title='New title test', slug='first-new-title-test-created')

	def create_post(self, title='Post new blog'):
		return Post.objects.create(title=title)

	def test_create_title(self):
		obj = Post.objects.get(slug='first-new-title-test-created')

		self.assertEqual(obj.title, 'New title test')
		self.assertTrue(obj.content == '')
	
	def test_create_slug(self):
		title_one = 'The new title for slug'
		title_two = 'The new title for example with more char'
		'''
		The test three is only to show that if we have two title is the same or duplicate will give an error
		because we said in the slug unique=true 
		'''
		title_three = 'The new title for slug'

		slug_one = slugify(title_one)
		slug_two = slugify(title_two)
		slug_three = slugify(title_three)

		obj1 = self.create_post(title=title_one)
		obj2 = self.create_post(title=title_two)
		obj3 = self.create_post(title=title_three)

		self.assertEqual(obj1.slug, slug_one)
		self.assertEqual(obj2.slug, slug_two)
		self.assertNotEqual(obj3.slug, slug_three)

	def test_blog_qs(self):
		title = 'The new title for example with more char'

		obj1 = self.create_post(title=title)
		obj2 = self.create_post(title=title)
		obj3 = self.create_post(title=title)

		query_set = Post.objects.filter(title=title)
		self.assertEqual(query_set.count(), 3)

		query_set_1 = Post.objects.filter(slug=obj1.slug)
		self.assertEqual(query_set_1.count(), 1)


