from django.shortcuts import render
from .models import About, Team

# Create your views here.
from django.http import HttpResponse


# def index(request):
#    return HttpResponse("Hello, world. You're at the products index.")

def aboutus(request):
    template_name = 'aboutus.html'
    aboutus = About.objects.all()
    team = Team.objects.all()

    for item in aboutus:
        print(item)
        print(item.main_title)
    context = {
        'main_title': item.main_title,
        'description1': item.description1,
        'description2': item.description2,
        'description3': item.description3,
        'team': team,
    }
    return render(request, template_name, context)


def team(request):
    template_name = 'aboutus.html'
    team = Team.objects.all()

    return render(request, template_name, {'team': team})
