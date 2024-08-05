from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("rango says mango")


def about(request):
    return HttpResponse("rango says about")
