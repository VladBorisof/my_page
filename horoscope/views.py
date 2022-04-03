from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from zodiac_sign import get_zodiac_sign

# Create your views here.
zodiac_dict = {
    'aries': "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)",
    'taurus': "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)",
    'gemini': "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)",
    'cancer': "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)",
    'leo': "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)",
    'virgo': "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)",
    'libra': "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)",
    'scorpio': "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)",
    'sagittarius': "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)",
    'capricorn': "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января",
    'aquarius': "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)",
    'pisces': "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)"
}

tipes_dict = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}


def index(request):
    zodiacs = list(zodiac_dict)
    rez = ''
    for i in zodiacs:
        redirect_path = reverse('horoscope-name', args=[i])
        rez += f'<li> <a href={redirect_path}> {i.title()} </a> </li>'
    response = f"""
    <ol>
        {rez}
    </ol>
    """
    return HttpResponse(response)


def get_view_by_tipes(request):
    tipes = list(tipes_dict)
    rez = ''
    for i in tipes:
        redirect_path = reverse('horoscope-type', args=[i])
        rez += f'<li> <a href={redirect_path}> {i.title()} </a> </li>'

    response = f"""
            <ol>
                {rez}
            </ol>
            """
    return HttpResponse(response)


def get_zodiac_by_day(request, month: int, day: int):
    if (month < 1 or month > 12) or (day < 1 or day > 31):
        return HttpResponseNotFound("<h1> Перебор по дням </h1>")
    else:
        zodiac_by_day = get_zodiac_sign(day, month).lower()
        redirect_url = reverse('horoscope-name', args=(zodiac_by_day, ))
        return HttpResponseRedirect(redirect_url)


def get_info_by_tipes(request, tipe: str):
    tipes = list(tipes_dict)
    include_horoscope = tipes_dict.get(tipe)
    rez = ''
    for i in include_horoscope:
        redirect_path = reverse('horoscope-name', args=[i])
        rez += f'<li> <a href={redirect_path}> {i.title()} </a> </li>'

    response = f"""
        <ol>
            {rez}
        </ol>
        """
    return HttpResponse(response)


def get_info_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f"I dont know - {sign_zodiac}")


def get_info_zodiac_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Неправильный порядковый номер - {sign_zodiac}')
    name = zodiacs[sign_zodiac]
    redirect_url = reverse('horoscope-name', args=(name, ))
    return HttpResponseRedirect(redirect_url)
