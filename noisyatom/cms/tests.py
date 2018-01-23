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

    # TODO Make this dynamic so that main_title and descriptions are pulled from a table in the database.
    main_title = 'Ecommerce Platform for Alfa Aesar Ltd'
    description1 = 'This project encompassed the migration of a legacy Websmart system into a modern python Django web platform. The platform was deployed onto a hosted server running with Redhat SE Linux 6.2 on an IBM PowerPC platform.'
    description2 = 'Read on to find out more about the specifics...'
    description3 = ' '


    def test_alfa_title(self):
        url = reverse("cms:alfa")
        response = self.client.get(url)
        print("*** Doing HTTP Get to Alfa page: {}".format(url))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.main_title, str(response.content))
        self.assertIn(self.description1, str(response.content))
        self.assertIn(self.description2, str(response.content))
        self.assertTemplateUsed(response, 'alfa.html')
        self.assertIn(b'Alfa Aesar Ltd', response.content)

class VodafoneProjectTest(TestCase):
    # Check that we have the main page title and that the template is correct for this URL route

    # TODO Make this dynamic so that main_title and descriptions are pulled from a table in the database.
    main_title = 'Vodafone Patent Wall'
    description1 = 'Noisy Atom provided consultancy in creating a QR code and URL mapping system for the Vodafone Patent Wall'
    description2 = 'It allows static QR codes to be created and etched onto perspex, but still allow dynamic routing to a CMS system to visualise information about Vodafones inventors, technology ant patents'
    description3 = 'For now - read more and see the end results of our innovation.'

    def test_vodafone_title(self):
        url = reverse("cms:vodafone")
        response = self.client.get(url)
        print("*** Doing HTTP Get to Vodafone page: {}".format(url))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.main_title, str(response.content))
        self.assertIn(self.description1, str(response.content))
        self.assertIn(self.description2, str(response.content))
        self.assertIn(self.description3, str(response.content))
        self.assertTemplateUsed(response, 'vodafone.html')
        self.assertIn(b'QR Codes & Patents', response.content)


# Make sure the about us page is displayed and renders the correct template
class AboutUs(TestCase):
    # TODO Startup content goes here

    # TODO Make this dynamic so that main_title and descriptions are pulled from a table in the database.
    main_title = 'Vodafone Patent Wall'
    description1 = 'We have been active for 4 years. A dynamic tech focussed company. We love technology. Our core competences are in Python and Python web frameworks.'
    description2 = 'Check back soon for our open source products centred around QR Code generation and mapping with OAuth2 services.'
    description3 = ' '


    # Check that we have an about us title at least
    def test_about_us(self):
        url = reverse("cms:about_us")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about-us.html')
        self.assertTemplateUsed(response, 'background-page.html')
        self.assertIn(b'About Us', response.content)

    # TODO add some test cases to verify that images are 800px in size
