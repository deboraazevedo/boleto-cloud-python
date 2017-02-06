# -*- coding: utf-8 -*-

import requests
from requests.auth import HTTPBasicAuth
from .exception import ConnectionError, AuthenticationError


class Boleto(object):

    def __init__(self, token):
        self.__token = token
        self.__url = 'https://sandbox.boletocloud.com/api/v1/boletos/'

    @property
    def token(self):
    	'''Returns the token for access API.'''
    	return self.__token

    def get_url(self, resource=''):
    	'''Returns the url.'''
    	return '{0}{1}'.format(self.__url, resource)

    def authenticate(self, resource=''):
    	'''Authenticates all requests.'''
    	return requests.get(self.get_url(resource), auth=HTTPBasicAuth(self.token, 'token'))

