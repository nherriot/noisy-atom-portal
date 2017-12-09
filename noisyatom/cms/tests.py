from django.test import TestCase
from django.core.urlresolvers import reverse
from cms.views import index_view
# Create your tests here.

# Make sure the index page is displayed and renders the correct template
class IndexTest(TestCase):

    #TODO Startup content goes here

    # Check we at least have a title
    def test_index_title(self):
        url = reverse("cms:index")
        resp = self.client.get(url)
        print("*** Doing HTTP Get to Main Index page: {}".format(url))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'landing-page.html')
        self.assertIn(b'Welcome to Noisy Atom', resp.content)

    # Check that the navbar contains our Noisy Atom logo
    def test_navbar(self):
        url = reverse("cms:index")
        resp = self.client.get(url)
        print("*** Doing HTTP Get to Main Index page: {}".format(url))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'navbar.html')
        self.assertInHTML('<img src="/static/assets/img/na_icon.png" alt="Noisy Atom Logo">', str(resp.content))

    # Check that the header has the landing page title at least
    def test_header(self):
        url = reverse("cms:index")
        resp = self.client.get(url)
        print("*** Doing HTTP Get to Main Index page: {}".format(url))
        self.assertEqual(resp.status_code, 200)
        self.assertInHTML('<title>Landing Page - Noisy Atom web portal</title>', str(resp.content))
        self.assertTemplateUsed(resp, 'header.html')

    # Check that we have the by noisy atom footer comment.
    def test_footer(self):
        url = reverse("cms:index")
        resp = self.client.get(url)
        print("*** Doing HTTP Get to Main Index page: {}".format(url))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'footer.html')
        self.assertIn(b'by Noisy Atom', resp.content)


class AlfaProjectTest(TestCase):

    # Check that we have the main page title and that the template is correct for this URL route
    def test_alfa_title(self):
        url = reverse("cms:alfa")
        response = self.client.get(url)
        print("*** Doing HTTP Get to Alfa page: {}".format(url))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'alfa.html')
        self.assertIn(b'Alfa Aesar Ltd', response.content)

class VodafoneProjectTest(TestCase):
    # Check that we have the main page title and that the template is correct for this URL route
    def test_alfa_title(self):
        url = reverse("cms:vodafone")
        response = self.client.get(url)
        print("*** Doing HTTP Get to Vodafone page: {}".format(url))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vodafone.html')
        self.assertIn(b'QR Codes & Patents', response.content)


# Make sure the about us page is displayed and renders the correct template
class AboutUs(TestCase):

    #TODO Startup content goes here

    # Check that we have an about us title at least
    def test_about_us(self):
        url = reverse("cms:about_us")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about-us.html')
        self.assertTemplateUsed(response, 'background-page.html')
        self.assertIn(b'About Us', response.content)

    # TODO add some test cases to verify that images are 800px in size
