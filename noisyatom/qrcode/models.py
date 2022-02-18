from django.db import models

# QR Code
# -----------------
#
# Has a creation date.
# Is unique.
# It contains a png of it's unique number.
# It has a unique slug.
# It maps to a single product.
# It has a primary mapped URL. (Where it routes to)
# It has a secondary mapped URL. (Where it routes when a trigger point happens)
# It has an active flag to indicate when to switch routing on.
# A trigger point in future time.


class QRcode(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, help_text='Unique value for product page URL, created from name.')
    description = models.TextField()
    # TODO A one-to-one relationship to a QR code object that is used to describe a generic product.
    image = models.ImageField(
        max_length=50,
        height_field=250,
        width_field=250,
        blank=True,
    )             # image of QR code
    is_active = models.BooleanField(default=True)                                           # turns on routing
    trigger = models.DateTimeField()                                                        # when to switch primary and secondary URL's
    primary_url = models.URLField(max_length=200)
    secondary_url = models.URLField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'QRCodes'
        ordering = ['-created_at']
        verbose_name_plural = 'QRCode'

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'QRCode', (), {'qrcode_slug': self.slug}
