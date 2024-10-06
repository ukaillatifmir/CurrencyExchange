import requests
from CurrencyExchange.settings import CURRENCY_BEACON_APIKEY,CURRENCY_BEACON_API_LATEST,CURRENCY_BEACON_API_HISTORY


class CurrencyBeacon:

    def fetch_rate(self,base,symbols,date=None):
        if date:
            url = CURRENCY_BEACON_API_HISTORY.format(api_key=CURRENCY_BEACON_APIKEY, base=base, symbols=symbols,date = date)
        else:
            url = CURRENCY_BEACON_API_LATEST.format(api_key = CURRENCY_BEACON_APIKEY, base = base, symbols = symbols)
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
