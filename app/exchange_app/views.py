from django.shortcuts import render
import requests


def exchange(request):
    responce = request.get(url='https:api.exchangerate-api.com/v4/latest/USD').json()
    currencies = responce.get('rates')

    if request.method == 'GET':

       context = {
        'currencies': currencies
       }
    return render(request=request, template_name='exchange.app/index.html', context=context)

    if request.method == 'POST':
        from_amount = request.POST.get('from-amount')
        from_curr = request.POST.get('from-curr')
        from_curr = request.POST.get('to-cur')

        converted_amount = round((currencies[to_curr] / currencies[from_curr]) * float(from_amount), 2)

        context = {
            'from_curr': from_curr,
            'to_curr': to_curr,
            'from_amount': from_amount,
            'currencies': currencies,
            'converted_amount': converted_amount
        }

        return render(request=request, template_name='exchange.app/index.html', context=context)