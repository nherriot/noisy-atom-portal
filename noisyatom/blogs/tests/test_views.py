
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User


from blogs.models import Post


class PostModelTest(TestCase):

    def setUp(self):
        self.client = Client()
        test_user_normal = User.objects.create_user(username='testuser_normal', password='12345')
        test_user_staff = User.objects.create_user(username='testuser_staff', password='12345', is_staff=True)
        test_user_admin = User.objects.create_user(username='testuser_admin', password='12345', is_superuser=True)
        test_user_inactive = User.objects.create_user(username='testuser_inactive', password='12345', is_active=False, is_staff=True, is_superuser=True)
        test_user_normal.save()
        test_user_staff.save()
        test_user_admin.save()
        test_user_inactive.save()

    def create_post(self, title='Post new blog'):
        return Post.objects.create(title=title)

    def test_list_views(self):
        '''
            This will request a list of all the blog titles to be rendered on the page. We need to check that all the
            blog titles created in SETUP get displayed on the page.
        '''
        url = reverse('blogs:list')
        response = self.client.get(url)
        #TODO YOu need to check that the tiles are present in the list Dilshad. You are only looking for the http200
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


    def test_update_blog_post_anonymous_user(self):
        '''
            An anonymous user tries to update a blog post. This should return a 404 and fail. Only a super user
            or staff user can update blogs!
        '''
        obj = self.create_post(title='Some new title for new test')
        url = reverse('blogs:updated', kwargs={'slug': obj.slug})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 404)

    def test_update_blog_post_user_logged_in(self):
        '''
            Login our user, and try create a blog post and make sure we get a http404. Only staff and admin
            can update blogs!
        '''
        obj = self.create_post(title='Some new title for new test')     # This should go in the setup function
        print("***** We have the following users: {}".format(User.objects.all()))  # returns []
        login = self.client.login(username='testuser_normal', password='12345')
        if login:
            url = reverse('blogs:updated', kwargs={'slug': obj.slug})
            response = self.client.get(url)

            self.assertEqual(response.status_code, 404)
            self.client.logout()
        else:
            self.assertRaises('login failed')

    def test_update_blog_post_as_staff_user(self):
        '''
            Login our user, and try create a blog post and make sure we get a http404. Only staff and admin
            can update blogs!
        '''
        obj = self.create_post(title='Some new title for new test')     # This should go in the setup function
        print("***** We have the following users: {}".format(User.objects.all()))  # returns []
        login = self.client.login(username='testuser_staff', password='12345')
        if login:
            url = reverse('blogs:updated', kwargs={'slug': obj.slug})
            print("***** We are looking up the URL: {}".format(url))
            response = self.client.get(url)

            self.assertEqual(response.status_code, 200)
            self.client.logout()
        else:
            self.assertRaises('login failed')

    # def test_update_blog_post_as_admin_user(self):
    #     '''
    #         Login our user, and try create a blog post and make sure we get a http404. Only staff and admin
    #         can update blogs!
    #     '''
    #     obj = self.create_post(title='Some new title for new test')     # This should go in the setup function
    #     print("***** We have the following users: {}".format(User.objects.all()))  # returns []
    #     login = self.client.login(username='testuser_normal', password='12345')
    #
    #     print("The login object is: {}".format(login))
    #
    #
    #     url = reverse('blogs:updated', kwargs={'slug': obj.slug})
    #     print("***** We are looking up the URL: {}".format(url))
    #     response = self.client.get(url)
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.client.logout()
    #
    # def test_update_blog_post_as_inactive_user(self):
    #     '''
    #         Login our user, and try create a blog post and make sure we get a http404. Even if the user is
    #         staff or admin or both! They must be active to be able to use the system. Hence the can't update blogs!
    #     '''
    #     obj = self.create_post(title='Some new title for new test')     # This should go in the setup function
    #     print("***** We have the following users: {}".format(User.objects.all()))  # returns []
    #     login = self.client.login(username='testuser_inactive', password='12345')
    #
    #     print("The login object is: {}".format(login))
    #     print("***** We have logged in now and have the following users: {}".format(User.objects.all()))  # returns one user
    #     print("******The first index user has a login state of: {}".format(User.objects.all()[0].is_authenticated()))  # returns True
    #
    #
    #     url = reverse('blogs:updated', kwargs={'slug': obj.slug})
    #     print("***** We are looking up the URL: {}".format(url))
    #     response = self.client.get(url)
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.client.logout()



    def test_delete_views(self):
        obj = self.create_post(title='Some new title for new test')
        url = reverse('blogs:delete', kwargs={'slug': obj.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


