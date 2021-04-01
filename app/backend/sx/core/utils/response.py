import logging

import requests

from ..exceptions import GetResponseError, ResponseDeserializationError

# Get an instance of a logger
logger = logging.getLogger(__name__)


def get(url, headers={'content-type': 'application/json'}):
    response = None
    try:

        response = requests.get(url=url, headers=headers)
        # Raise Exception if response is not successful
        response.raise_for_status()
        return response
    except requests.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except Exception as err:
        logger.error(f"Unknown exception: {err}")
    finally:
        if not response:
            raise GetResponseError


def deserialize(response):
    """
    Return deserialized response or raise ResponseDeserializationError
    """
    try:
        deserialized_response = response.json()
        return deserialized_response
    except TypeError as type_err:
        logger.error(f"Type error occurred during deserialization: {type_err}")
    except ValueError as value_err:
        logger.error(f"Value error occurred during deserialization: {value_err}")
    finally:
        if not deserialized_response:
            raise ResponseDeserializationError
