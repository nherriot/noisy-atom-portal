from django.shortcuts import render

# Create your views here.

def index_view(request):
	context = {}
	return render(request, 'index.html', context)


def dashboard_view(request):
	context = {}
	return render(request, 'dashboard.html', context)