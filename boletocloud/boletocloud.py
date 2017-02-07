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

    def create(self, bank, agency, number, wallet, recipient_name, recipient_cprf, recipient_address_zip, recipient_address_uf, recipient_address_locale, recipient_address_neighborhood, recipient_address_street, recipient_address_number, recipient_address_complement, emission, pay, document, ticket_number, title, value, payer_name, payer_cprf, payer_address_zip, payer_address_uf, payer_address_locale, payer_address_neighborhood, payer_address_street, payer_address_number, payer_address_complement, instruction):
        '''Creates a ticket with b ase in the parameters of this method.'''
        payload = {
            'boleto.conta.banco': bank,
            'boleto.conta.agencia': agency, 
            'boleto.conta.numero': number, 
            'boleto.conta.carteira': wallet, 
            'boleto.beneficiario.nome': recipient_name, 
            'boleto.beneficiario.cprf': recipient_cprf, 
            'boleto.beneficiario.endereco.cep': recipient_address_zip, 
            'boleto.beneficiario.endereco.uf': recipient_address_uf,
            'boleto.beneficiario.endereco.localidade': recipient_address_locale, 
            'boleto.beneficiario.endereco.bairro': recipient_address_neighborhood, 
            'boleto.beneficiario.endereco.logradouro': recipient_address_street, 
            'boleto.beneficiario.endereco.numero': recipient_address_number,
            'boleto.beneficiario.endereco.complemento': recipient_address_complement, 
            'boleto.emissao': emission,
            'boleto.vencimento': pay, 
            'boleto.documento': document, 
            'boleto.numero': ticket_number, 
            'boleto.titulo': title,
            'boleto.valor': value, 
            'boleto.pagador.nome': payer_name, 
            'boleto.pagador.cprf': payer_cprf,
            'boleto.pagador.endereco.cep': payer_address_zip, 
            'boleto.pagador.endereco.uf': payer_address_uf,
            'boleto.pagador.endereco.localidade': payer_address_locale, 
            'boleto.pagador.endereco.bairro': payer_address_neighborhood,
            'boleto.pagador.endereco.logradouro': payer_address_street, 
            'boleto.pagador.endereco.numero': payer_address_number,
            'boleto.pagador.endereco.complemento': payer_address_complement, 
            'boleto.instrucao': instruction,
        }


        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'Accept': 'application/pdf, application/json'
        }

        with open('ticket.pdf', 'wb') as ticket:
            file = requests.post(self.get_url(), data=json.dumps(payload), headers=headers, auth=self.authenticate)
            ticket.write(file.content)

    def search(self, token_ticket):
        '''Returns the boleto especify in token_ticket.'''
        with open('ticket.pdf', 'wb') as ticket:
            file = requests.get(self.get_url(token_ticket), auth=self.authenticate)
            ticket.write(file.content)
