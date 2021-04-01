from django.utils.translation import gettext_lazy as _

from rest_framework import status
from rest_framework.exceptions import APIException


class BitcoinAmountNotFound(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Bitcoin quantity not found in the request.')
    default_code = 'parse_error'


class BidsError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = _('Bids error - incorrect json content.')
    default_code = 'bids_error'


class BidNotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _('Bid not found for that bitcoin amount.')
    default_code = 'bids_not_found'
