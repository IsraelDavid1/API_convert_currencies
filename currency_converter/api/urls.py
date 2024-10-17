from django.urls import path
from .views import convert_currency, currencies

urlpatterns = [
    path('convert/', convert_currency, name='convert_currency'), 
    path('', currencies, name='currency converter')
]
