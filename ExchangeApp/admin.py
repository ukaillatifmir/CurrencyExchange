from django.contrib import admin

# Register your models here.
from .models import Currency,CurrencyExchangeRate,Provider

admin.site.register(Currency)
admin.site.register(CurrencyExchangeRate)
admin.site.register(Provider)