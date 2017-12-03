
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY


from blogs.models import Post


class BlogUpdateTest(TestCase):
    """
    This class will test all updates methods to a blog post for each of our users: normal, admin, staff and inactive.
    """
    fixtures = ['users', 'initial_data']

    def setUp(self):
        logged_in = self.client.session.has_key(SESSION_KEY)
        # We are making sure that the user is not logged in at the start of each test
        self.assertFalse(logged_in)

    def test_get_update_blog_post_as_staff_user(self):
        """
            Login our user, and try to view a blog post that can be updated from the edit page and make sure we get a http200.
            Only staff and admin can update blogs. So this should work fine.
            Note, this does not update a blog, just view the update page.
        """
        test_blog = Post.objects.get(title="test1")
        login = self.client.login(username='testuser_staff', password='password12345')

        if login:
            url = reverse('blogs:updated', kwargs={'slug': test_blog.slug})
            response = self.client.get(url)

            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'update.html')
            self.assertIn('test1', str(response.content))
            self.assertIn('this is content 1', str(response.content))
            self.client.logout()
        else:
            # TODO Make this dynamic rather than hard coded text string
            self.fail('Login Failed for testuser_staff')

    def test_get_update_blog_post_as_admin_user(self):
        """
            Login our user, and try to view a blog post that can be updated from the edit page and make sure we get a http200.
            Only staff and admin can update blogs. So this should work fine.
            Note, this does not update a blog, just view the update page.
        """
        test_blog = Post.objects.get(title="test1")
        login = self.client.login(username='testuser_admin', password='password12345')

        if login:
            url = reverse('blogs:updated', kwargs={'slug': test_blog.slug})
            print("***** We are looking up the URL: {}".format(url))
            response = self.client.get(url)

            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'update.html')
            self.assertIn('test1', str(response.content))
            self.assertIn('this is content 1', str(response.content))
            self.client.logout()
        else:
            # TODO Make this dynamic rather than hard coded text string
            self.fail('Login Failed for testuser_admin')

    def test_get_update_blog_post_user_logged_in(self):
        """
            An anonymous user tries to do a HTTP GET to the update a blog post URL. This should return a 403 (forbidden) and fail.
            Only a super user or staff user can update blogs!
        """
        test_blog = Post.objects.get(title="test1")
        login = self.client.login(username='testuser_normal', password='password12345')

        if login:
            url = reverse('blogs:updated', kwargs={'slug': test_blog.slug})
            response = self.client.get(url)

            self.assertEqual(response.status_code, 403)
            self.client.logout()

        else:
            # TODO Make this dynamic rather than hard coded text string
            self.fail('Login Failed for the testuser_normal')

    def test_get_update_blog_post_anonymous_user(self):
        """
            Login our user, and try create a blog post and make sure we get a http403 (forebidden). Only staff
            and admin can update blogs!
        """

        test_blog = Post.objects.get(title="test1")
        url = reverse('blogs:updated', kwargs={'slug': test_blog.slug})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 403)

    def test_post_update_blog_post_as_staff_user(self):
        """
            Login our user, and try to view a blog post that can be updated from the edit page and make sure we get a http200.
            Only staff and admin can update blogs. So this should work fine.
            Note, this does not update a blog, just view the update page.
        """
        test_blog = Post.objects.get(title="test1")
        print("***** test blog title is: {}".format(test_blog.title))

        print("***** test blog content is: {}".format(test_blog.content))
        login = self.client.login(username='testuser_staff', password='password12345')

        if login:
            url = reverse('blogs:updated', kwargs={'slug': test_blog.slug})
            data = {'title': 'this is a new title', 'content': 'this is new content by nicholas herriot'}
            response = self.client.post(url, data)

            new_blog = Post.objects.get(pk=1)
            print("*** New blog post has content of: {}".format(new_blog.slug))
            print("*** New blog post has content of: {}".format(new_blog.title))
            print("*** New blog post has content of: {}".format(new_blog.content))

            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'update.html')
            self.assertIn('this is a new title', str(response.content))
            self.assertIn('this is new content by nicholas herriot', str(response.content))
            self.client.logout()
        else:
            # TODO Make this dynamic rather than hard coded text string
            self.fail('Login Failed for testuser_staff')





class BlogCreateTest(TestCase):
    '''
    This class will test all creation methods of blog post for each of our users: normal, admin, staff and inactive.
    '''

    def setUp(self):
        self.client = Client()


class BlogDeleteTest(TestCase):
    '''
    This class will test all delete methods for a blog post for each of our users: normal, admin, staff and inactive.
    '''

    def setUp(self):
        self.client = Client()


class PostModelTest(TestCase):
    fixtures = ['users', 'initial_data']

    def setUp(self):
        self.client = Client()
        logged_in = self.client.session.has_key(SESSION_KEY)
        # We are making sure that the user is not logged in at the start of each test
        self.assertFalse(logged_in)

    def create_post(self, title='Post new blog'):
        return Post.objects.create(title=title)

    def test_list_views(self):
        '''
            This will request a list of all the blog titles to be rendered on the page. We need to check that all the
            blog titles created in SETUP get displayed on the page.
        '''
        url = reverse('blogs:list')
        response = self.client.get(url)
        #TODO you need to check that the tiles are present in the list Dilshad. You are only looking for the http200
        self.assertEqual(response.status_code, 200)


    def test_detail_views(self):
        '''
            This will display a blog post and it's contents. We need to check that a blog post can be displayed on
            a page. Blog title and description saved in setup should be present in the HTML rendered on the page.
        '''
        obj = self.create_post(title='Some new title for new test')
        response = self.client.get(obj.get_absolute_url())
        #TODO You need to check that the description and title are present in the html returned from the server Dilshad
        self.assertEqual(response.status_code, 200)








    # def test_delete_views(self):
    #     obj = self.create_post(title='Some new title for new test')
    #     url = reverse('blogs:delete', kwargs={'slug': obj.slug})
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 404)


