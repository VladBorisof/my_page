from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.


def get_week_day(request, week_day: str):
    if week_day == 'monday':
        return HttpResponse("1. Спать\n"
                            "2. Спать")
    elif week_day == 'tuesday':
        return HttpResponse("1. Спать\n"
                            "2. Спать Больше")
    else:
        return HttpResponseNotFound(f'{week_day} - такого не знаю')


def get_week_day_int(request, week_day: int):
    if week_day <= 7:
        return HttpResponse(f"Сегодня {week_day} день недели")
    else:
        return HttpResponseNotFound(f'Неверный номер дня - {week_day}')