# -*- coding: utf-8 -*-

import requests
import json
from requests.auth import HTTPBasicAuth
from .exception import ConnectionError, AuthenticationError


class Ticket(object):

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

    @property
    def authenticate(self):
        '''Authenticate all requests.'''
        return HTTPBasicAuth(self.token, 'token') 

    def search(self, token_ticket):
        '''Returns the boleto especify in token_ticket.'''
        with open('ticket.pdf', 'wb') as ticket:
            file = requests.get(self.get_url(token_ticket), auth=self.authenticate)
            ticket.write(file.content)
