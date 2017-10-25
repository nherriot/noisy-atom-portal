from django.test import TestCase
from django.core.urlresolvers import reverse
from cms.views import index_view
# Create your tests here.

class WhateverTest(TestCase):

    def test_index(self):

        url = reverse("cms.views.index_view")
        resp = self.client.get(url)

        print ("*** Response is: {}".format(resp))

        self.assertEqual(resp.status_code, 200)
        #self.assertIn(w.title, resp.content)

