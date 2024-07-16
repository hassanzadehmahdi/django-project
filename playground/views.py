from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "index.html")


def say_hello(request):
    return render(request, "hello.html", {"name": "Mahdi"})
