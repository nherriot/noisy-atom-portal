from django.db import models
from django.core.validators import EmailValidator, ValidationError, URLValidator
from django.utils.translation import ugettext_lazy as _
from utils.lists import (
    COUNTRY_CHOICES
)

# A company model which will be bound to products and categories. Hence a category can only belong to one company.
# And a product can only belong to one company. However product items only belong to one product.

class CustomerAddress(models.Model):
    name = models.CharField(_('Name'), help_text=_('Enter the name you would like to give this address.'), max_length=255, blank=False, null=False, db_index=True)
    # For MVP a user can have a single company which can have 1 registered address, so we are removing any code which
    # allows multiple address. This simplifies the design and DB complexity for our demo application
    #type = models.CharField(_('Address type'), help_text=_('Enter the type of address this is'), choices=ADDRESS_CHOICES, max_length=50, null=True, blank=True)
    #is_default = models.BooleanField(_('Is default address'), default=False, help_text=_('Set this address as the default for all orders'), db_index=True)

    address_line1 = models.CharField(_('Address 1'), help_text=_('Enter your the address (line 1 of 4)'), max_length=250, null=True, blank=True)
    address_line2 = models.CharField(_('Address 2'), help_text=_('Enter your the address (line 2 of 4)'), max_length=250, null=True, blank=True)
    address_line3 = models.CharField(_('Address 3'), help_text=_('Enter your the address (line 3 of 4)'), max_length=250, null=True, blank=True)
    address_line4 = models.CharField(_('Address 4'), help_text=_('Enter your the address (line 4 of 4)'), max_length=250, null=True, blank=True)
    postal_code = models.CharField(_('Postal code'), help_text=_('Enter your the Postal or Zip Code '), max_length=25, null=True, blank=True)
    city = models.CharField(_('City'), help_text=_('Enter the name of the city you are based'), max_length=250, null=True, blank=True)
    state = models.CharField(_('State/Province'), help_text=_('Enter your  State / Province'), max_length=250, null=True, blank=True)
    country = models.CharField(_('Country'), help_text=_('Enter your Country '), max_length=2, choices=COUNTRY_CHOICES, null=True, blank=True)
    phone = models.CharField(_('Phone'), help_text=_('Enter the your phone number'), max_length=250, null=True, blank=True)
    created_date = models.DateTimeField(verbose_name=_('Created Date'), auto_now_add=True, db_index=True, null=True)
    modified_date = models.DateTimeField(verbose_name=_('Last Modified'), auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Customer Addresses'

    def __unicode__(self):
        return self.name





class Company(models.Model):
    name = models.CharField(_('Name'), help_text=_('Enter the name you would like to give this address.'), max_length=255, blank=False, null=False, db_index=True)
    description = models.TextField(_('Description'), help_text=_('Please provide any extra description for this company.'), null=True, blank=True)

    vat = models.CharField(_('VAT Registration'), help_text=_('VAT Registration'), max_length=250, null=True, blank=True)
    company_number = models.CharField(_('Company Number'), help_text=_('Government allocated company number - e.g. HMRC Company Number'), max_length=250, null=True, blank=True)

    # Removing admin and user fields. Once the 'user' model is integrated with registration we can add/bind our company
    # model to the user model with a 1-2-1 link. i.e. a user can create a single company for MVP
    #admins = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='admins_company_set')
    #users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='users_company_set')
    addresses = models.ManyToManyField('account.CustomerAddress', related_name='addresses_company_set')

    company_url = models.URLField(max_length=254, help_text="This is a unique URI to describe the callback used by the OAuth2 server", validators=[URLValidator], default="http://www.example.com")

    # Removed contact name, email and phone number as we will bind this to a single account - so for a MVP we will only
    # allow a user to create a single company. We also want to make this as simple as possible to fill in forms
    #contact_name = models.CharField(_('Contact Name'), help_text=_('Enter the name you would like to give this address.'), max_length=255, blank=False, null=False)
    #contact_email = models.CharField(_('Contact email'), help_text=_('Enter the name you would like to give this address.'), max_length=255, blank=False, null=False)
    #contact_phone = models.CharField(_('Contact phone'), help_text=_('Enter the name you would like to give this address.'), max_length=255, blank=False, null=False)


    created_date = models.DateTimeField(verbose_name=_('Created Date'), auto_now_add=True, db_index=True)
    modified_date = models.DateTimeField(verbose_name=_('Last Modified'), auto_now=True)

    def __unicode__(self):
        return self.name
