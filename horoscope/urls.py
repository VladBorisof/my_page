from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:sign_zodiac>/', views.get_info_zodiac_number),
    path('<str:sign_zodiac>/', views.get_info_zodiac, name='horoscope-name'),

]
