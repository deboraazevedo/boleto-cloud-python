# -*- coding: utf-8 -*-

import requests
from requests.auth import HTTPBasicAuth
from .exception import ConnectionError, AuthenticationError


class Boleto(object):

    def __init__(self, token):
        self.__token = token
        self.__url = 'https://sandbox.boletocloud.com/api/v1/'

    @property
    def token(self):
        return self.__token

    def get_url(self, resource):
        return '{0}{1}'.format(self.__url, resource)
