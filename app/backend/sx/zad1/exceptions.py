from django.utils.translation import gettext_lazy as _

from rest_framework import status
from rest_framework.exceptions import APIException


class DataListNotFound(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Datalist not found in the request.')
    default_code = 'parse_error'
