from django.shortcuts import render
from django.http import JsonResponse
import requests

def convert_currency(request):
    from_currency = request.GET.get('from')
    to_currency = request.GET.get('to')
    amount = float(request.GET.get('amount'))

    response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{from_currency}')
    data = response.json()
    rate = data['rates'][to_currency]
    converted_amount = amount * rate

    return JsonResponse({
        'from_currency': from_currency,
        'to_currency': to_currency,
        'amount': amount,
        'converted_amount': converted_amount,
        'rate': rate
    })

