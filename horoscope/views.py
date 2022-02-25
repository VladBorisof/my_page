from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def leo(request):
    return HttpResponse("Знак зодиака - лев")


def scorpio(request):
    return HttpResponse("Знак зодиака - скорпион")


def aries(request):
    return HttpResponse("Знак зодиака - овен")


def taurus(request):
    return HttpResponse("Знак зодиака - телец")
