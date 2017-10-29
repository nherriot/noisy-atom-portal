from django.shortcuts import render
from django.urls import reverse
# Create your views here.

def index_view(request):
	context = {}

	return render(request, 'index.html', context)


def coming_soon(request):
    context = {}

    return render(request, 'coming-soon.html', context)

def dashboard_view(request):
	context = {}
	return render(request, 'dashboard.html', context)