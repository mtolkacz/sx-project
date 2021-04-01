from rest_framework import views, permissions
from rest_framework.response import Response

from . import mixins


class BitcoinBIDPriceAPI(mixins.BitcoinBIDPriceMixin, views.APIView):
    http_method_names = ['post', ]
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):

        self.set_amount_to_buy()
        self.set_orderbook()
        self.set_price()

        return Response(data={'price': self.price.amount})
