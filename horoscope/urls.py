from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:month>/<int:day>', views.get_zodiac_by_day),
    path('tipes/', views.get_view_by_tipes),
    path('tipes/<str:tipe>', views.get_info_by_tipes, name='horoscope-type'),
    path('<int:sign_zodiac>/', views.get_info_zodiac_number),
    path('<str:sign_zodiac>/', views.get_info_zodiac, name='horoscope-name'),

]
