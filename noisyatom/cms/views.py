from django.shortcuts import render
from django.urls import reverse


def index_view(request):
	context = {}

	return render(request, 'index.html', context)


def coming_soon(request):
    context = {}

    return render(request, 'coming-soon.html', context)

def dashboard_view(request):
	context = {}
	return render(request, 'dashboard.html', context)

def alfa_view(request):
	template_name = 'alfa.html'
	#TODO Make this dynamic data from a table in our database
	context = {
		'title': 'Ecommerce Platform for Alfa Aesar Ltd',
		'description1':'This project encompassed the migration of a legacy "Websmart" system into a modern python Django web platform. The platform was deployed onto a hosted server running with Redhat SE Linux 6.2 on an IBM PowerPC platform.',
		'description2':'Read on to find out more about the specifics...',
		'description3':''
	}
	return render(request, template_name, context)