from django.test import TestCase
from django.core.urlresolvers import reverse
from cms.views import index_view
# Create your tests here.

class WhateverTest(TestCase):

    def test_index(self):

        url = reverse("cms:index")
        resp = self.client.get(url)
        #print("*** Response is: {}".format(resp.content))

        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Welcome to Noisy Atom', resp.content)

