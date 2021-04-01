from django.urls import path
from .apiv1 import views as apiv1_views

urlpatterns = [
    path(
        route='zadanie2/',
        view=apiv1_views.BitcoinBIDPriceAPI.as_view(),
        name='zad2',
    ),
]
