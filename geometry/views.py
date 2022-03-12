from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
import numpy as np


# Create your views here.


def get_rectangle_area(request, width: int, height: int):
    return HttpResponse(f"Площадь прямоугольника размером {width}х{height} равна {width * height}")


def get_square_area(request, width: int):
    return HttpResponse(f"<font size='5' color='red' face='Arial'> Площадь квадрата размером {width}х{width} равна {width * width} </font>")


def get_circle_area(request, radius: int):
    s = np.pi * radius * radius
    return HttpResponse(f"Площадь круга с радиусом {radius} равна {s}")


def rectangle(request, width: int, height: int):
    return HttpResponseRedirect(f'/calculate_geometry/rectangle/{width}/{height}')


def square(request, width: int):
    return HttpResponseRedirect(f'/calculate_geometry/square/{width}')


def circle(request, radius: int):
    return HttpResponseRedirect(f'/calculate_geometry/circle/{radius}')
