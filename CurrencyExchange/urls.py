"""
URL configuration for CurrencyExchange project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ExchangeApp.views import currency_rates_list,convert_amount, currency_list, currency_create, currency_update, currency_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('currency_rates_list/', currency_rates_list),
    path('convert_amount/', convert_amount),
    path('convert_amount/', convert_amount),
    path('', currency_list, name='currency_list'),
    path('currency/create/', currency_create, name='currency_create'),
    path('currency/update/<int:pk>/', currency_update, name='currency_update'),
    path('currency/delete/<int:pk>/', currency_delete, name='currency_delete'),

]
