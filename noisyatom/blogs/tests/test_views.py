
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY
from blogs.models import Post
import datetime


class BlogUpdateTest(TestCase):
    """
    This class will test all updates methods to a blog post for each of our users: normal, admin, staff and inactive.
    """
    fixtures = ['users', 'initial_data']
    # TODO Make this dynamic so that main_title and descriptions are pulled from a table in the database.
    main_title = 'Blogs At Noisy Atom'
    description1 = 'Read all about the latest thought, what we are working on and how we are progressing! A brain dump of where we are at!'
    description2 = 'We hope you enjoy our thoughts...'
    description3 = ' '

    def setUp(self):
        logged_in = self.client.session.has_key(SESSION_KEY)
        # We are making sure that the user is not logged in at the start of each test
        self.assertFalse(logged_in)



    def test_get_update_blog_post_as_staff_user_check_main_title_and_descriptions(self):
        """
            Login our user, and try to view a blog post that can be updated from the edit page and make sure we get a http200.
            Also check that we can render a title, description which is displayed in the background page.
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
            self.assertIn(self.main_title, str(response.content) )
            self.assertIn(self.description1, str(response.content))
            self.assertIn(self.description2, str(response.content))
            self.assertIn('this is content 1', str(response.content))
            self.client.logout()
        else:
            # TODO Make this dynamic rather than hard coded text string
            self.fail('Login Failed for testuser_staff')


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
            Login our user, and try create a blog post and make sure we get a http403 (forbidden). Only staff
            and admin can update blogs!
        """

        test_blog = Post.objects.get(title="test1")
        url = reverse('blogs:updated', kwargs={'slug': test_blog.slug})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 403)

    def test_post_update_blog_post_as_staff_user(self):
        """
            Login our user, and try to update a blog post and make sure we get a http302 to redirect to the list page.
            Only staff and admin can update blogs. So this should work fine.
            Note, this does not update a blog, just view the update page.
        """
        test_blog = Post.objects.get(title="test1")
        login = self.client.login(username='testuser_staff', password='password12345')

        if login:
            url = reverse('blogs:updated', kwargs={'slug': test_blog.slug})
            new_title = "this is a new title"
            new_content = "this is new content by nicholas herriot"
            new_published_date = "2017-01-01"
            data = {'title': new_title, 'slug':test_blog.slug, 'content': new_content, 'publish': new_published_date}
            response = self.client.post(url, data)

            # After our post has been sent our original slug should have a new title and new content
            new_blog = Post.objects.get(pk=1)

            self.assertEqual(response.status_code, 302)
            self.assertTrue(new_blog.title, new_title)
            self.assertTrue(new_blog.content, new_content)
            self.assertTrue(new_blog.publish, new_published_date)
            self.client.logout()
        else:
            # TODO Make this dynamic rather than hard coded text string
            self.fail('Login Failed for testuser_staff')


    def test_post_update_blog_post_as_user_logged_in(self):
        """
            Login our normal user, and try to update a blog post and make sure we get a http403.
            Only staff and admin can update blogs. So this should work fine.
            Note, this does not update a blog, just view the update page.
        """
        test_blog = Post.objects.get(title="test1")
        login = self.client.login(username='testuser_normal', password='password12345')

        if login:
            url = reverse('blogs:updated', kwargs={'slug': test_blog.slug})
            new_title = "this is a new title"
            new_content = "this is new content by nicholas herriot"
            new_published_date = "2017-01-01"
            data = {'title': new_title, 'slug':test_blog.slug, 'content': new_content, 'publish': new_published_date}
            response = self.client.post(url, data)

            # After our post has been sent our original slug should still be the same
            new_blog = Post.objects.get(slug=test_blog.slug)

            self.assertTrue(new_blog.title, 'test1')
            self.assertTrue(new_blog.content, 'this is content 1')
            self.assertEqual(response.status_code, 403)
            self.client.logout()
        else:
            # TODO Make this dynamic rather than hard coded text string
            self.fail('Login Failed for testuser_normal')


    def test_post_update_blog_post_as_super_user(self):
        """
            Login our user, and try to update a blog post and make sure we get a http302 to redirect to the list page.
            Only staff and admin can update blogs. So this should work fine.
            Note, this does not update a blog, just view the update page.
        """
        test_blog = Post.objects.get(title="test1")
        login = self.client.login(username='testuser_admin', password='password12345')

        if login:
            url = reverse('blogs:updated', kwargs={'slug': test_blog.slug})
            new_title = "this is a new title"
            new_content = "this is new content by nicholas herriot"
            new_published_date = "2017-01-01"
            data = {'title': new_title, 'slug':test_blog.slug, 'content': new_content, 'publish': new_published_date}
            response = self.client.post(url, data)

            # After our post has been sent our original slug should have a new title and new content
            new_blog = Post.objects.get(slug=test_blog.slug)

            self.assertEqual(response.status_code, 302)
            self.assertTrue(new_blog.title, new_title)
            self.assertTrue(new_blog.content, new_content)
            self.assertTrue(new_blog.publish, new_published_date)
            self.client.logout()
        else:
            # TODO Make this dynamic rather than hard coded text string
            self.fail('Login Failed for testuser_staff')


    def test_post_update_blog_post_as_anonymous_user(self):
        """
            Try to update a blog post make sure we get a http403 if we are not a super user or staff user.
            Only staff and admin can update blogs. So this should work fine.
            Note, this does not update a blog, just view the update page.
        """

        test_blog = Post.objects.get(title="test1")
        url = reverse('blogs:updated', kwargs={'slug': test_blog.slug})
        new_title = "this is a new title"
        new_content = "this is new content by nicholas herriot"
        new_published_date = "2017-01-01"
        data = {'title': new_title, 'slug': test_blog.slug, 'content': new_content, 'publish': new_published_date}

        response = self.client.post(url, data)

        # After our post has been sent our original slug should still be the same
        new_blog = Post.objects.get(slug=test_blog.slug)

        self.assertTrue(new_blog.title, 'test1')
        self.assertTrue(new_blog.content, 'this is content 1')

        self.assertEqual(response.status_code, 403)



class BlogCreateTest(TestCase):
    """
    This class will test all creation methods to a blog post for each of our users: normal, admin, and staff.
    """
    fixtures = ['users', 'initial_data']

    def setUp(self):
        logged_in = self.client.session.has_key(SESSION_KEY)
        # We are making sure that the user is not logged in at the start of each test
        self.assertFalse(logged_in)

    def test_get_create_post_as_anonymous_user(self):
        """
            Try to do a Http GET to the create blog post page when you are not logged in. In real life the 'ADD' button
            is not on the screen but we can still send the GET request to create the user to the server. This should fail
            with a Http 403 - Forbidden
        """

        url = reverse('blogs:create')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 403)


    def test_get_create_post_as_user_logged_in(self):
        """
            Try to do a Http GET to the create blog post page when you are logged in as a normal user. In real life the
            'ADD' button is not on the screen but we can still send the GET request to create the user to the server.
            This should fail with a Http 403 - Forbidden
        """

        login = self.client.login(username='testuser_normal', password='password12345')

        if login:
            url = reverse('blogs:create')
            response = self.client.get(url)

            self.assertEqual(response.status_code, 403)
            self.client.logout()

        else:
            # TODO Make this dynamic rather than hard coded text string
            self.fail('Login Failed for the testuser_normal')


    def test_get_create_post_as_staff_user(self):
        """
            Try to do a Http GET to the create blog post page when you are logged in as a staff user. You should get
            a rendered create.html template for the user to populate with a new blog post.
        """

        login = self.client.login(username='testuser_staff', password='password12345')

        if login:
            url = reverse('blogs:create')
            response = self.client.get(url)

            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'create.html')
            self.client.logout()
        else:
            # TODO Make this dynamic rather than hard coded text string
            self.fail('Login Failed for testuser_staff')


    def test_get_create_post_as_admin_user(self):
        """
            Try to do a Http GET to the create blog post page when you are logged in as a admin user. You should get
            a rendered create.html template for the user to populate with a new blog post.

        """
        login = self.client.login(username='testuser_admin', password='password12345')

        if login:
            url = reverse('blogs:create')
            response = self.client.get(url)

            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'create.html')
            self.client.logout()
        else:
            # TODO Make this dynamic rather than hard coded text string
            self.fail('Login Failed for testuser_staff')


    def test_post_create_post_as_anonymous_user(self):
        """
            Try to do a Http POST to the create blog post page when you are not logged in. You should get a Http 403
            - Forbidden.

        """

        url = reverse('blogs:create')
        new_title = "this is a new title for create"
        new_content = "this is new content for create by nicholas herriot"
        new_published_date = "2017-01-01"
        data = {'title': new_title, 'content': new_content, 'publish': new_published_date}
        response = self.client.post(url, data)

        # There should not be a new blog create with this title, so check that it does not exist
        with self.assertRaises(Post.DoesNotExist):
            new_blog = Post.objects.get(title=new_title)
        self.assertEqual(response.status_code, 403)


    def test_post_create_post_as_user_logged_in(self):
        """
            Try to do a Http POST to the create blog post page when you are logged in as a user with no privileges.
            You should get a Http 403 - Forbidden.

        """

        login = self.client.login(username='testuser_normal', password='password12345')

        if login:

            new_title = "this is a new title for create"
            new_content = "this is new content for create by nicholas herriot"
            new_published_date = "2017-01-01"
            data = {'title': new_title, 'content': new_content, 'publish': new_published_date}
            url = reverse('blogs:create')
            response = self.client.post(url, data)

            # There should not be a new blog create with this title, so check that it does not exist
            with self.assertRaises(Post.DoesNotExist):
                new_blog = Post.objects.get(title=new_title)
            self.assertEqual(response.status_code, 403)
            self.client.logout()
        else:
            # TODO Make this dynamic rather than hard coded text string
            self.fail('Login Failed for testuser_staff')


    def test_post_create_post_as_staff_user(self):
        """
            Try to do a Http POST to the create blog post page when you are logged in as a staff user with write
            privileges. You should get a Http 302 - Redirect to view a list of blogs. The DB should contain the new
            blog title you created.

        """
        login = self.client.login(username='testuser_staff', password='password12345')

        if login:

            new_title = "this is a new title for create"
            new_content = "this is new content for create by nicholas herriot"
            new_published_date = datetime.date(2018, 3, 3)
            data = {'title': new_title, 'content': new_content, 'publish': new_published_date}

            url = reverse('blogs:create')
            response = self.client.post(url, data)

            # There should now be a new blog create with this title and content, so check that it does exist
            new_blog = Post.objects.get(title='this is a new title for create')
            #print("*** New blog created as a slug of: {}".format(new_blog.slug))
            #print("*** New blog created as a titel of: {}".format(new_blog.title))
            #print("*** New blog created as content of: {}".format(new_blog.content))
            #print("*** New blog created as a published date of: {}".format(new_blog.publish))

            self.assertEqual(new_blog.title, new_title)
            self.assertEqual(new_blog.content, new_content)
            # TODO Get the publish date check working correctly
            #self.assertEqual(new_blog.publish, new_published_date)

            self.assertEqual(response.status_code, 302)
            self.client.logout()
        else:
            # TODO Make this dynamic rather than hard coded text string
            self.fail('Login Failed for testuser_staff')


    def test_post_create_post_as_admin_user(self):
        """
            Try to do a Http POST to the create blog post page when you are logged in as a admin user with write
            privileges. You should get a Http 302 - Redirect to view a list of blogs. The DB should contain the new
            blog title you created.

        """
        login = self.client.login(username='testuser_admin', password='password12345')

        if login:

            new_title = "this is a new title for create"
            new_content = "this is new content for create by nicholas herriot"
            new_published_date = datetime.date(2018, 3, 3)
            data = {'title': new_title, 'content': new_content, 'publish': new_published_date}

            url = reverse('blogs:create')
            response = self.client.post(url, data)

            # There should now be a new blog create with this title and content, so check that it does exist
            new_blog = Post.objects.get(title='this is a new title for create')

            self.assertEqual(new_blog.title, new_title)
            self.assertEqual(new_blog.content, new_content)
            # TODO Get the publish date check working correclty
            #self.assertEqual(new_blog.publish, new_published_date)

            self.assertEqual(response.status_code, 302)
            self.client.logout()
        else:
            # TODO Make this dynamic rather than hard coded text string
            self.fail('Login Failed for testuser_staff')


    # TODO Chcek the slug works correctly and write a test case for checking it.
    # TODO Check that you can create multiple blogs with the same title.




class BlogDeleteTest(TestCase):
    '''
    This class will test all delete methods for a blog post for each of our users: normal, admin, staff and inactive.
    '''

    fixtures = ['users', 'initial_data']

    def setUp(self):
        logged_in = self.client.session.has_key(SESSION_KEY)
        # We are making sure that the user is not logged in at the start of each test
        self.assertFalse(logged_in)

    def test_post_delete_post_as_anonymous_user(self):
        """
            Try to do a Http GET to delete a blog post page when you are an anonymous user. You should get a Http 403
            - Forbidden as only an admin or staff user can delete posts.

        """
        last_post = Post.objects.get(title="test3")
        url = reverse('blogs:delete', kwargs={'slug': last_post.slug})
        response = self.client.get(url)

        # There should still be a blog post with this title. Hence we should still be able to find the blog post
        check_post = Post.objects.get(slug=last_post.slug)
        self.assertEqual(check_post.title, last_post.title)
        self.assertEqual(check_post.content, last_post.content)
        self.assertEqual(check_post.pk, last_post.pk)
        self.assertEqual(response.status_code, 403)


    def test_post_delete_post_as_logged_in_user(self):
        """
            Try to do a Http GET to delete a blog post page when you are a normal user. You should get a Http 403
            - Forbidden as only an admin or staff user can delete posts.

        """
        login = self.client.login(username='testuser_normal', password='password12345')

        if login:

            last_post = Post.objects.get(title="test3")
            url = reverse('blogs:delete', kwargs={'slug': last_post.slug})
            response = self.client.get(url)

            # There should still be a blog post with this title. Hence we should still be able to find the blog post
            check_post = Post.objects.get(slug=last_post.slug)
            self.assertEqual(check_post.title, last_post.title)
            self.assertEqual(check_post.content, last_post.content)
            self.assertEqual(check_post.pk, last_post.pk)
            self.assertEqual(response.status_code, 403)
            self.client.logout()
        else:
            # TODO Make this dynamic rather than hard coded text string
            self.fail('Login Failed for testuser_staff')


    def test_post_delete_post_as_staff_user(self):
        """
            Try to do a Http GET to delete a blog post page when you are a staff user. You should get a Http 302
            - You should be redirected to the blogs URL.

        """
        login = self.client.login(username='testuser_staff', password='password12345')

        if login:

            last_post = Post.objects.get(title="test3")
            url = reverse('blogs:delete', kwargs={'slug': last_post.slug})
            response = self.client.get(url)

            # There should not be a blog post with this title. It should have been deleted.
            with self.assertRaises(Post.DoesNotExist):
                check_blog = Post.objects.get(slug=last_post.slug)
            self.assertEqual(response.status_code, 302)
            # TODO make the /blogs/ URL for the redirect dynamic
            self.assertRedirects(response, '/blogs/', 302)
            self.client.logout()

        else:
            # TODO Make this dynamic rather than hard coded text string
            self.fail('Login Failed for testuser_staff')


    def test_post_delete_post_as_admin_user(self):
        """
            Try to do a Http GET to delete a blog post page when you are an admin user. You should get a Http 302
            - You should be redirected to the blogs URL.

        """
        login = self.client.login(username='testuser_admin', password='password12345')

        if login:

            last_post = Post.objects.get(title="test3")
            url = reverse('blogs:delete', kwargs={'slug': last_post.slug})
            response = self.client.get(url)

            # There should not be a blog post with this title. It should have been deleted.
            with self.assertRaises(Post.DoesNotExist):
                check_blog = Post.objects.get(slug=last_post.slug)
            self.assertEqual(response.status_code, 302)
            # TODO make the /blogs/ URL for the redirect dynamic
            self.assertRedirects(response, '/blogs/', 302)
            self.client.logout()

        else:
            # TODO Make this dynamic rather than hard coded text string
            self.fail('Login Failed for testuser_staff')



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


