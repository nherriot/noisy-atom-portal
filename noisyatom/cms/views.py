from django.shortcuts import render
from django.urls import reverse
# Create your views here.

def index_view(request):
	context = {}

	print (" ***** Index view ***** thre reverse URL lookup is: {}".format(reverse('cms:foo_bar_url')))

	return render(request, 'index.html', context)


def dashboard_view(request):
	context = {}
	return render(request, 'dashboard.html', context)