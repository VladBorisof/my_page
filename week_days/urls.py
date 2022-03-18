from django.urls import path
from . import views

urlpatterns = [
    path('<int:week_day>/', views.get_week_day_int),
    path('<str:week_day>/', views.get_week_day, name='week_day-name'),

]
