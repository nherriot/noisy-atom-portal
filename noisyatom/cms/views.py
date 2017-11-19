from django.shortcuts import render
from django.urls import reverse
# Create your views here.

def index_view(request):
    context = {}

    return render(request, 'index.html', context)


def coming_soon(request):
    context={'title': 'Coming Soon',
                'paragraph1': 'We are working hard!',
                'paragraph2': 'Stay tuned for our QR codes!',
                'paragraph3': ''}

    return render(request, 'sub-header.html', context)

def dashboard_view(request):
    context = {}
    return render(request, 'dashboard.html', context)


def about_us(request):
    #TODO Make this dynamic content from a data base.
    context={'title':'About Us',
                'paragraph1': 'We have been active for 4 years. A dynamic tech focussed company. We love technology. Our core competences are in Python and Python web frameworks.',
                'paragraph2': 'Check back soon for our open source products centred around QR Code generation and mapping with OAuth2 services.',
                'paragraph3': 'For now - read more to meet the team.'}
    return render(request, 'about-us.html', context)

