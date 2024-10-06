from django.db import models
from django.db.models import Model, PROTECT


# Create your models here.

class Currency(Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=20, db_index=True)
    symbol = models.CharField(max_length=10)


class Provider(Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=20, db_index=True)
    is_active = models.BooleanField(default=True)
    default = models.BooleanField(default=False)


class CurrencyExchangeRate(Model):
    source_currency = models.ForeignKey(Currency,related_name='exchanges',
    on_delete=models.CASCADE)
    exchanged_currency = models.ForeignKey(Currency,on_delete=models.CASCADE)
    valuation_date = models.DateField(db_index=True)
    rate_value = models.DecimalField(db_index=True,decimal_places=6,
    max_digits=18)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)


