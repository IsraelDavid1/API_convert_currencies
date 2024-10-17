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

def currencies(request):
    currencies = [
        "AFN", "EUR", "ALL", "DZD", "USD", "AOA", "XCD", "ARS", "AMD", "AWG",
        "AUD", "AZN", "BSD", "BHD", "BDT", "BBD", "BYN", "BZD", "XOF", "BMD",
        "INR", "BTN", "BOB", "BOV", "BAM", "BWP", "NOK", "BRL", "BND", "BGN",
        "BIF", "CVE", "KHR", "XAF", "CAD", "KYD", "CLP", "CLF", "CNY", "COP",
        "COU", "KMF", "CDF", "NZD", "CRC", "HRK", "CUP", "CUC", "ANG", "CZK",
        "DKK", "DJF", "DOP", "EGP", "SVC", "ERN", "SZL", "ETB", "FKP", "FJD",
        "XPF", "GMD", "GEL", "GHS", "GIP", "GTQ", "GBP", "GNF", "GYD", "HTG",
        "HNL", "HKD", "HUF", "ISK", "IDR", "XDR", "IRR", "IQD", "ILS", "JMD",
        "JPY", "JOD", "KZT", "KES", "KPW", "KRW", "KWD", "KGS", "LAK", "LBP",
        "LSL", "ZAR", "LRD", "LYD", "CHF", "MOP", "MKD", "MGA", "MWK", "MYR",
        "MVR", "MRU", "MUR", "XUA", "MXN", "MXV", "MDL", "MNT", "MAD", "MZN",
        "MMK", "NAD", "NPR", "NIO", "NGN", "OMR", "PKR", "PAB", "PGK", "PYG",
        "PEN", "PHP", "PLN", "QAR", "RON", "RUB", "RWF", "SHP", "WST", "STN",
        "SAR", "RSD", "SCR", "SLL", "SGD", "XSU", "SBD", "SOS", "SSP", "LKR",
        "SDG", "SRD", "NOK", "SEK", "CHE", "CHW", "SYP", "TWD", "TJS", "TZS",
        "THB", "TOP", "TTD", "TND", "TRY", "TMT", "UGX", "UAH", "AED", "UYU",
        "UYI", "UYW", "UZS", "VUV", "VES", "VND", "YER", "ZMW", "ZWL"
    ]
    return render(request, 'home.html', {'currencies': currencies})

