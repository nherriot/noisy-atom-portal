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
	context = {
		'title': 'Alfa Aesar Ltd'
	}
	return render(request, template_name, context)