from django.test import TestCase
from django.core.urlresolvers import reverse
from cms.views import index_view
# Create your tests here.

class InterestCalculatorTest(TestCase):

    def test_zero(self):

        url = reverse("ee_test:ee_calculated_value")
        response = self.client.post(url, {'ee_calculate': '0'})
        #resp = self.client.get(url)
        print("*** Response is: {}".format(response.content))

        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Welcome to Noisy Atom', response.content)


    def test_1000(self):

        url = reverse("ee_test:ee_calculated_value")
        response = self.client.post(url, {'ee_calculate': '0'})
        #resp = self.client.get(url)
        print("*** Response is: {}".format(response.content))

        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Welcome to Noisy Atom', response.content)

    def test_5000(self):

        url = reverse("ee_test:ee_calculated_value")
        response = self.client.post(url, {'ee_calculate': '0'})
        #resp = self.client.get(url)
        print("*** Response is: {}".format(response.content))

        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Welcome to Noisy Atom', response.content)

    def test_max_value(self):

        url = reverse("ee_test:ee_calculated_value")
        response = self.client.post(url, {'ee_calculate': '0'})
        #resp = self.client.get(url)
        print("*** Response is: {}".format(response.content))

        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Welcome to Noisy Atom', response.content)

    def test_not_a_number(self):

        url = reverse("ee_test:ee_calculated_value")
        response = self.client.post(url, {'ee_calculate': '0'})
        #resp = self.client.get(url)
        print("*** Response is: {}".format(response.content))

        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Welcome to Noisy Atom', response.content)

    def test_negative(self):

        url = reverse("ee_test:ee_calculated_value")
        response = self.client.post(url, {'ee_calculate': '0'})
        #resp = self.client.get(url)
        print("*** Response is: {}".format(response.content))

        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Welcome to Noisy Atom', response.content)





