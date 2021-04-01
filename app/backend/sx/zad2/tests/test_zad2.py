from decimal import Decimal

import requests
from django import urls


def test_zad2_api_get_method(client):
    url = urls.reverse('zad2:api')
    resp = client.get(url)

    assert resp.status_code == 405


def test_zad2_incorrect_input(client):
    response = client.post(
        urls.reverse('zad2:api'),
        {'incorrect_input': 1},
        content_type='application/json',
    )

    assert response.status_code == 400


def test_zad2_200_ok(client):
    """
    Zad2 API has to return HTTP status code 200 for correct order book's bid
    """

    response = requests.get('https://bitbay.net/API/Public/BTCPLN/orderbook.json')

    assert response.status_code == 200

    orderbook = response.json()
    amount_btc = Decimal(orderbook['bids'][0][1])

    response = client.post(
        urls.reverse('zad2:api'),
        {'buy': amount_btc},
        content_type='application/json',
    )

    assert response.status_code == 200
