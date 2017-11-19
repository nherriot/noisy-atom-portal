from django.test import TestCase
from django.core.urlresolvers import reverse
from cms.views import index_view
# Create your tests here.

# Make sure the index page is displayed and renders the correct template
class IndexTest(TestCase):

    #TODO Startup content goes here

    def test_index(self):

        url = reverse("cms:index")
        response = self.client.get(url)
        #print("*** Response is: {}".format(resp.content))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertTemplateUsed(response, 'landing-page.html')
        self.assertIn(b'Welcome to Noisy Atom', response.content)

# Make sure the about us page is displayed and renders the correct template
class AboutUs(TestCase):

    #TODO Startup content goes here

    def test_about_us(self):

        url = reverse("cms:about_us")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about-us.html')
        self.assertTemplateUsed(response, 'background-page.html')
        self.assertIn(b'About Us', response.content)



