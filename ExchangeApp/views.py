from django.shortcuts import render , redirect, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view

from .adapters import CurrencyBeaconAdapter
from .models import Currency

from .forms import CurrencyForm

@api_view(['POST'])
def currency_view(request):
    adapter = CurrencyBeaconAdapter()
    users = adapter.get_users()
    user_data = [{'name': user.name, 'email': user.email} for user in users]
    return JsonResponse(user_data, safe=False)

@api_view(['POST'])
def currency_rates_list(request):
    source_currency = request.data['source_currency']
    date_from = request.data['date_from']
    date_to = request.data['date_to']
    adapter = CurrencyBeaconAdapter()
    currency_rates_list_data = adapter.get_currency_rates(source_currency,date_from,date_to)
    return JsonResponse(currency_rates_list_data, safe=False) 

@api_view(['POST'])
def convert_amount(request):
    source_currency = request.data['source_currency']
    amount = request.data['amount']
    exchanged_currency = request.data['exchanged_currency']
    adapter = CurrencyBeaconAdapter()
    currency_rates_list_data = adapter.convert_currency(source_currency,exchanged_currency,amount)
    return JsonResponse(currency_rates_list_data, safe=False)


# List View
def currency_list(request):
    currencies = Currency.objects.all()
    return render(request, 'currency_list.html', {'currencies': currencies})

# Create View
def currency_create(request):
    if request.method == 'POST':
        form = CurrencyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('currency_list')
    else:
        form = CurrencyForm()
    return render(request, 'currency_form.html', {'form': form})

# Update View
def currency_update(request, pk):
    currency = get_object_or_404(Currency, pk=pk)
    if request.method == 'POST':
        form = CurrencyForm(request.POST, instance=currency)
        if form.is_valid():
            form.save()
            return redirect('currency_list')
    else:
        form = CurrencyForm(instance=currency)
    return render(request, 'currency_form.html', {'form': form})

# Delete View
def currency_delete(request, pk):
    currency = get_object_or_404(Currency, pk=pk)
    if request.method == 'POST':
        currency.delete()
        return redirect('currency_list')
    return render(request, 'currency_confirm_delete.html', {'currency': currency})
