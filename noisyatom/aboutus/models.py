from django.db import models


# Create your models here.

class About(models.Model):
    main_title = models.CharField(max_length=200)
    description1 = models.TextField()
    description2 = models.TextField()
    description3 = models.TextField()

    def __str__(self):
        return self.main_title


class Team(models.Model):
    card_title = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    card_description = models.TextField()
    linkedIn = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)
    google = models.CharField(max_length=300)
    picture = models.ImageField(upload_to='profile/', default="RP2040_Pico.png", height_field=None, width_field=None)
    project_date = models.DateTimeField('date published')

    def __str__(self):
        return self.card_title
