from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

week_days_dict = {
    'monday': 'В понедельник я <br> Спать <br> Спать',
    'tuesday': 'Во вторник я <br> Спать <br> Спать',
    'wednesday': 'В среду я <br> Спать <br> Спать',
    'thursday': 'В четверг я <br> Спать <br> Спать',
    'friday': 'В пятницу я <br> Спать <br> Спать',
    'saturday': 'В субботу я <br> Спать <br> Спать',
    'sunday': 'В воскресенье я <br> Спать <br> Спать',

}


def index(request):
    week_days = list(week_days_dict)
    day = ''
    for i in week_days:
        redirect_path = reverse('week_day-name', args=[i])
        day += f'<li> <a href={redirect_path}> {i.title()} </a> </li>'
    response = f"""
    <center> 
        <h1> Day of week </h1> </center>
        <ul>
            {day}
        </ul>
    """

    return HttpResponse(response)


def get_week_day(request, week_day: str):
    to_do = week_days_dict.get(week_day)
    if to_do:
        return HttpResponse(to_do)
    else:
        return HttpResponseNotFound(f'{week_day} - такого не знаю')


def get_week_day_int(request, week_day: int):
    week_days = list(week_days_dict)
    if week_day < len(week_days):
        name = week_days[week_day-1]
        redirect_url = reverse('week_day-name', args=(name,))
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f'Неверный номер дня - {week_day}')
