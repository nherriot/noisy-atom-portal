from django.contrib import admin

from .models import Post

'''
	https://docs.djangoproject.com/en/1.11/ref/contrib/admin/#modeladmin-options
'''

class PostModelAdmin(admin.ModelAdmin):
	
	list_display = ['title', 'publish', 'updated']
	list_display_links = ['updated']
	list_editable = ['title']
	list_filter = ['publish', 'title', 'updated']

	search_fields = ['title', 'publish', 'updated']
	
	# empty_value_display = 'unknown'

	class Meta:
		model = Post
		fields = ('content')


admin.site.register(Post, PostModelAdmin)

