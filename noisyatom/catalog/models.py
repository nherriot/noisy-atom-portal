from django.db import models
from django.urls import reverse
from account.models import Company
from qrcode.models import QRcode

# A simple model to describe a vanilla catalog. This will allow a catalog to have multiple products. And products to be
# part of multiple catalogs.


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, help_text='Unique value for category page URL, created from name.')
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField("Meta Keywords", max_length=255,
                                     help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField(max_length=255, help_text='Content for description of meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'
        ordering = ['-created_at']
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name

def get_absolute_url(self):
    return reverse('catalog_category', (), {'category_slug': self.slug})

class Product(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, help_text='Unique value for product page URL, created from name.')
    brand = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    old_price = models.DecimalField(max_digits=9, decimal_places=2)
    two_d_bar_code = models.OneToOneField(
        QRcode,
        on_delete=models.CASCADE,
        primary_key=True,
        null=False,
        blank=True,
        default=0,
    )
    image = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    company_name = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    description = models.TextField()
    meta_keywords = models.CharField("Meta Keywords", max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField(max_length=255, help_text='Content for description of meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)

    class Meta:
        db_table = 'products'
        ordering = ['-created_at']
        verbose_name_plural = 'Product'

    def __unicode__(self):
        return self.name

def get_absolute_url(self):
    return reverse('catalog_product', (), {'product_slug': self.slug})


    # Make sure that if the current price is smaller than the old price we use as a sale price. If not then we don't
    # have a special sale price.
    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None


class ProductItem(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, help_text='Unique value for product page URL, created from name.')
    brand = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    sale_price = models.DecimalField(max_digits=9, decimal_places=2)        # The item can only be sold at a specific price
    two_d_bar_code = models.OneToOneField(
        QRcode,
        on_delete=models.CASCADE,
        primary_key=True,
        null=False,
        blank=True,
        default=0,
    )
    #TODO A one-to-one relationship with an order or customer
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_item'
        ordering = ['-created_at']
        verbose_name_plural = 'Product Item'

    def __unicode__(self):
        return self.name

def get_absolute_url(self):
    return reverse('catalog_productitem', (), {'productitem_slug': self.slug})

