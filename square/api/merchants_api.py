# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from square.http.auth.o_auth_2 import OAuth2


class MerchantsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""

    def __init__(self, config, call_back=None):
        super(MerchantsApi, self).__init__(config, call_back)

    def list_merchants(self,
                       cursor=None):
        """Does a GET request to /v2/merchants.

        Returns `Merchant` information for a given access token.
        If you don't know a `Merchant` ID, you can use this endpoint to
        retrieve the merchant ID for an access token.
        You can specify your personal access token to get your own merchant
        information or specify an OAuth token
        to get the information for the  merchant that granted you access.
        If you know the merchant ID, you can also use the
        [RetrieveMerchant](#endpoint-merchants-retrievemerchant)
        endpoint to get the merchant information.

        Args:
            cursor (int, optional): The cursor generated by the previous
                response.

        Returns:
            ListMerchantsResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/merchants'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'cursor': cursor
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters
        )
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def retrieve_merchant(self,
                          merchant_id):
        """Does a GET request to /v2/merchants/{merchant_id}.

        Retrieve a `Merchant` object for the given `merchant_id`.

        Args:
            merchant_id (string): The ID of the merchant to retrieve.

        Returns:
            RetrieveMerchantResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/merchants/{merchant_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'merchant_id': merchant_id
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result
