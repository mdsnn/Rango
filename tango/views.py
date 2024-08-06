from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context={
        'boldMessage' : "crunchy, creamy, cookiey, candy, cupcake"
    }
    return render(request, "index.html", context)


def about(request):
    return HttpResponse("rango says about")
