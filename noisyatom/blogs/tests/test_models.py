
from django.test import TestCase
from django.utils.text import slugify

from blogs.models import Post


class PostModelTest(TestCase):
    '''
        The setUp function will send test data to test database not to original database, which is real data
        but saved in test database not the real one.
    '''
    def setUp(self):
        self.post = Post.objects.create(title='New title test', slug='first-new-title-test-created')

    def create_post(self, title='Post new blog'):
        return Post.objects.create(title=title)

    def test_post_title(self):
        obj = Post.objects.get(slug='first-new-title-test-created')

        self.assertEqual(obj.title, 'New title test')
        self.assertEqual(obj.slug, 'first-new-title-test-created')
        self.assertTrue(obj.content == '')
    
    def test_post_slug(self):
        """
            Ensure that if a slug is the same another slug, the system will create a new slug by appending
            an index number to the slug. Here we create the blog posts with the same title on blog 1 and blog 2.
            This should cause the system to create it's own random slug
        """
        title_one = 'The new title for slug'
        title_two = 'The new title for example with more char'
        title_three = 'The new title for slug'

        slug_one = slugify(title_one)
        slug_two = slugify(title_two)
        slug_three = slugify(title_three)

        obj1 = self.create_post(title=title_one)
        # print("my object 1 has slug {} and titel {}".format(obj1.slug, obj1.title))
        obj2 = self.create_post(title=title_two)
        # print("my object 2 has slug {} and titel {}".format(obj2.slug, obj2.title))
        obj3 = self.create_post(title=title_three)
        # print("my object 3 has slug {} and titel {}".format(obj3.slug, obj3.title))
        obj4 = self.create_post(title=title_three)
        obj5 = self.create_post(title=title_three)

        self.assertEqual(obj1.slug, slug_one)
        self.assertEqual(obj2.slug, slug_two)
        self.assertNotEqual(obj3.slug, slug_three)

    def test_blog_queryset(self):
        '''
            Count how many title in total and how many title in one object
        '''
        title = 'The new title for example with more char'

        obj1 = self.create_post(title=title)
        obj2 = self.create_post(title=title)
        obj3 = self.create_post(title=title)

        query_set = Post.objects.filter(title=title)
        self.assertEqual(query_set.count(), 3)

        query_set_1 = Post.objects.filter(slug=obj1.slug)
        self.assertEqual(query_set_1.count(), 1)
