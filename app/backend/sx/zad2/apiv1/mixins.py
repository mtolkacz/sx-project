from decimal import Decimal, InvalidOperation

from money import Money
from rest_framework.exceptions import ParseError

from ..exceptions import BitcoinAmountNotFound, BidsError, BidNotFound
from ...core.utils import response


class OrderbookManager(object):
    url = 'https://bitbay.net/API/Public/BTCPLN/orderbook.json'

    def get_latest(self):
        resp = response.get(url=self.url)
        orderbook = response.deserialize(resp)

        if 'bids' not in orderbook:
            raise BidsError

        return orderbook


class BitcoinBIDPriceMixin(OrderbookManager):
    amount_to_buy = None
    price = None
    orderbook = None

    def __init__(self):
        self.orderbook_manager = OrderbookManager()

    def get_buy_parameter(self):
        buy = self.request.data.get("buy", "")

        if not buy:
            raise BitcoinAmountNotFound

        return buy

    def set_amount_to_buy(self):
        try:
            buy = self.get_buy_parameter()
            self.amount_to_buy = Decimal(buy)

        except InvalidOperation as ex:
            raise ParseError

    def set_orderbook(self):
        self.orderbook = self.orderbook_manager.get_latest()

    def get_price(self):
        price = None
        for order in self.orderbook['bids']:
            exchange_rate = Decimal(order[0])
            amount_btc = Decimal(order[1])

            if amount_btc == self.amount_to_buy:
                price = round(exchange_rate * self.amount_to_buy, 2)
                price = Money(amount=price, currency='PLN')

        if not price:
            raise BidNotFound

        return price

    def set_price(self):
        self.price = self.get_price()

