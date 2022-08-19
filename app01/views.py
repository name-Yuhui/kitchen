from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def login(request):
    return render(request, "login.html")


def category(request):
    return render(request, "category.html")


def works(request):
    return render(request, "works.html")


def menu(request):
    return render(request, "menu.html")
