from datetime import datetime, timedelta
from locale import currency

from .external_api import CurrencyBeacon
from .models import CurrencyExchangeRate, Currency, Provider
from .mock_generator import MockGenerator
import pandas


class CurrencyBeaconAdapter:
    def __init__(self):
        self.client = CurrencyBeacon()

    def get_exchange_rate_data(self,source_currency, exchanged_currency, valuation_date,
                              provider):
        data = CurrencyExchangeRate.objects.filter(source_currency = source_currency,
                                                   exchanged_currency = exchanged_currency,
                                                   valuation_date = valuation_date,
                                                   provider = provider)
        if data:
            return list(data.values())[0]
        else:
            rate = 1
            if provider.code == 'MCK':
                rate = MockGenerator().generate()
                currency_rate = CurrencyExchangeRate.objects.create(
                    source_currency=source_currency,
                    exchanged_currency=exchanged_currency,
                    valuation_date=valuation_date,
                    provider=provider,
                    rate_value=rate
                )
            if provider.code == 'CBN':
                exchanged_currency_data = self.client.fetch_rate(source_currency.code,exchanged_currency.code,valuation_date)
                rate = exchanged_currency_data['response']['rates'][exchanged_currency.code]
                currency_rate = CurrencyExchangeRate.objects.create(
                    source_currency = source_currency,
                    exchanged_currency=exchanged_currency,
                    valuation_date=valuation_date,
                    provider=provider,
                    rate_value = rate
                )
            res = list(CurrencyExchangeRate.objects.filter(id=currency_rate.id).values())[0] #convert queryset to dict
            return res

    def get_currency_rates(self,source_currency, from_date, to_date):
        res = []
        dates = self.get_date_list(from_date,to_date)
        provider = Provider.objects.get(default=True)
        source_currency_obj = Currency.objects.get(code=source_currency)
        destination_currency = Currency.objects.exclude(code=source_currency)
        for valuation_date in dates:
            for exchanged_currency in destination_currency:
                temp = self.get_exchange_rate_data(source_currency_obj,exchanged_currency,valuation_date,provider)
                res.append(temp)
        return res

    def get_date_list(self,start_date_str, end_date_str):
        # Convert the date strings to datetime objects
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

        # Generate the list of date strings
        date_list = []
        current_date = start_date

        while current_date <= end_date:
            date_list.append(current_date.strftime('%Y-%m-%d'))
            current_date += timedelta(days=1)

        return date_list

    def convert_currency(self,source_currency, exchanged_currency ,amount):
        today = datetime.today().strftime('%Y-%m-%d')
        provider = Provider.objects.get(default=True)
        source_currency = Currency.objects.get(code=source_currency)
        exchanged_currency = Currency.objects.get(code=exchanged_currency)
        temp = self.get_exchange_rate_data(source_currency,exchanged_currency,today,provider)
        rate = temp['rate_value']

        temp['amount'] = amount
        temp['exchanged_amount'] = str(float(str(amount))*float(str(rate)))
        return temp
