from django.contrib import admin

# Register your models here.
from .models import About, Team

'''
	https://docs.djangoproject.com/en/1.11/ref/contrib/admin/#modeladmin-options
'''
admin.site.register(About)
admin.site.register(Team)
