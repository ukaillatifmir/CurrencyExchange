from celery import shared_task

from CurrencyExchange.ExchangeApp.adapters import CurrencyBeaconAdapter


@shared_task
def add_historical_data(source_currency, date_from, date_to):
    adapter = CurrencyBeaconAdapter()
    adapter.get_currency_rates(source_currency, date_from, date_to)
