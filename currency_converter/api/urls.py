from django.urls import path
from .views import convert_currency, home

urlpatterns = [
    path('', home, name='home'),
    path('convert/', convert_currency, name='convert_currency'),
]
