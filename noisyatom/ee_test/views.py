from django.shortcuts import render
from django.urls import reverse


# Create your views here.

def ee_index_view(request):
    context = {}

    return render(request, 'eetest-landing-page.html', context)


def ee_calculated_interest(request):
    context = {}

    print("***** Calculated interest view hit *****")

    return render(request, 'eetest-interest-rate.html', context)
