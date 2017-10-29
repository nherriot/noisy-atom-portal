from django.test import TestCase
from django.core.urlresolvers import reverse
from cms.views import index_view
# Create your tests here.

class InterestCalculatorTest(TestCase):

    #TODO Startup content goes here


    # Test a value of £0 entered.
    def test_zero(self):
        url = reverse("ee_test:ee_calculated_value")
        response = self.client.post(url, {'ee_calculate': '0'})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'eetest-interest-rate.html')
        self.assertEqual(response.context['interest'], '0.0')
        self.assertEqual(response.context['interest_rate'], '0')


    # Test a value of £1000 entered.
    def test_1000(self):
        url = reverse("ee_test:ee_calculated_value")
        response = self.client.post(url, {'ee_calculate': '1000'})

        self.assertTemplateUsed(response, 'eetest-interest-rate.html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['interest'], '10.0')
        self.assertEqual(response.context['interest_rate'], '1')


    # Test a value of £5000 entered.
    def test_5000(self):
        url = reverse("ee_test:ee_calculated_value")
        response = self.client.post(url, {'ee_calculate': '5000'})

        self.assertTemplateUsed(response, 'eetest-interest-rate.html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['interest'], '100.0')
        self.assertEqual(response.context['interest_rate'], '2')


    # Test a maxium value entered.
    def test_max_value(self):
        url = reverse("ee_test:ee_calculated_value")
        response = self.client.post(url, {'ee_calculate': '10000000'})

        self.assertTemplateUsed(response, 'eetest-interest-rate.html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['interest'], '300000.0')
        self.assertEqual(response.context['interest_rate'], '3')


    # Test a maxium value entered.
    def test_too_big_value(self):
        url = reverse("ee_test:ee_calculated_value")
        response = self.client.post(url, {'ee_calculate': '10000001'})

        self.assertTemplateUsed(response, 'eetest-landing-page.html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['error'], 'You can only deposit a maximum of £ 10000000')



    # Test a value that is not a number
    def test_not_a_number(self):
        url = reverse("ee_test:ee_calculated_value")
        response = self.client.post(url, {'ee_calculate': 'error'})
        #print("********** Response context: {}".format(response.context))

        self.assertTemplateUsed(response, 'eetest-landing-page.html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['error'], 'Please only type a number between 0 and 10,000,000 and then press the calculate button')


    # Test a value that is negative
    def test_negative(self):
        url = reverse("ee_test:ee_calculated_value")
        response = self.client.post(url, {'ee_calculate': '-1'})
        #print("********** Response context: {}".format(response.context))

        self.assertTemplateUsed(response, 'eetest-interest-rate.html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['interest'], '0.0')
        self.assertEqual(response.context['interest_rate'], '0')







