import pytest
import requests


@pytest.fixture
def bitbay_request():
    return requests.get('https://bitbay.net/API/Public/BTCPLN/orderbook.json')


def test_bitbay_availibility(bitbay_request):
    assert bitbay_request.status_code == 200


def test_bitbay_orderbook_structure(bitbay_request):
    orderbook = bitbay_request.json()

    assert 'bids' in orderbook
    assert 'asks' in orderbook



