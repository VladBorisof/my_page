from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
import numpy as np
from django.urls import reverse

# Create your views here.


def get_rectangle_area(request, width: int, height: int):
    return HttpResponse(f"Площадь прямоугольника размером {width}х{height} равна {width * height}")


def get_square_area(request, width: int):
    return HttpResponse(f"<font size='5' color='red' face='Arial'> Площадь квадрата размером {width}х{width} равна {width * width} </font>")


def get_circle_area(request, radius: int):
    s = np.pi * radius * radius
    return HttpResponse(f"Площадь круга с радиусом {radius} равна {s}")


def rectangle(request, width: int, height: int):
    redirect_url = reverse('rectangle-name', args=(width, height))
    return HttpResponseRedirect(redirect_url)


def square(request, width: int):
    redirect_url = reverse('square-name', args=(width, ))
    return HttpResponseRedirect(redirect_url)


def circle(request, radius: int):
    redirect_url = reverse('circle-name', args=(radius, ))
    return HttpResponseRedirect(redirect_url)
