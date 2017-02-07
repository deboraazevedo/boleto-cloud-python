# Boleto Cloud Python

[![Build Status](https://travis-ci.org/hudsonbrendon/boleto-cloud-python.svg?branch=master)](https://travis-ci.org/hudsonbrendon/boleto-cloud-python)

Library of integration with the API of [boletocloud.com](http://www.boletocloud.com)

![Logo](logo.png)


# Quick Start

```bash
$ pip install boleto-cloud-python
```
or

```bash
$ python setup.py install
```

# Usage


To access an API, you first have to create an account and generate a token in: [app.boletocloud.com/api](https://app.boletocloud.com/api)

With the token properly generated, pass as a string parameter in the instantiation of your object as shown in the code below:

```python
>>> from boletocloud import Ticket

>>> ticket = Ticket('your_token')
```

# Create a ticket

```python
>>> ticket.create(self, bank, agency, number, wallet, recipient_name, recipient_cprf, recipient_address_zip, recipient_address_uf, recipient_address_locale, recipient_address_neighborhood, recipient_address_street, recipient_address_number, recipient_address_complement, emission, pay, document, ticket_number, title, value, payer_name, payer_cprf, payer_address_zip, payer_address_uf, payer_address_locale, payer_address_neighborhood, payer_address_street, payer_address_number, payer_address_complement, instruction)
```

A good option to inform the parameters in a simpler way is to create a dictionary with the data in this way:

```python
params = {
	'boleto.conta.banco': 237,
	'boleto.conta.agencia': '1234-5', 
	'boleto.conta.numero': '123456-0', 
	'boleto.conta.carteira': 12, 
	'boleto.beneficiario.nome': 'DevAware Solutions', 
	'boleto.beneficiario.cprf': '15.719.277/0001-46', 
	'boleto.beneficiario.endereco.cep': '59020-000', 
	'boleto.beneficiario.endereco.uf': 'RN',
	'boleto.beneficiario.endereco.localidade': 'Natal', 
	'boleto.beneficiario.endereco.bairro': 'Petrópolis', 
	'boleto.beneficiario.endereco.logradouro': 'Avenida Hermes da Fonseca', 
	'boleto.beneficiario.endereco.numero': 384,
	'boleto.beneficiario.endereco.complemento': 'Sala 2A, segundo andar', 
	'boleto.emissao': '2014-07-11',
	'boleto.vencimento': '2020-05-30', 
	'boleto.documento': 'EX1', 
	'boleto.numero': '12345678901-P', 
	'boleto.titulo': 'DM',
	'boleto.valor': '1250.43', 
	'boleto.pagador.nome': 'Alberto Santos Dumont', 
	'boleto.pagador.cprf': '111.111.111-11',
	'boleto.pagador.endereco.cep': '36240-000', 
	'boleto.pagador.endereco.uf': 'MG',
	'boleto.pagador.endereco.localidade': 'Santos Dumont', 
	'boleto.pagador.endereco.bairro': 'Casa Natal',
	'boleto.pagador.endereco.logradouro': 'BR-499', 
	'boleto.pagador.endereco.numero': 's/n',
	'boleto.pagador.endereco.complemento': 'Sítio - Subindo a serra da Mantiqueira', 
	'boleto.instrucao': 'Atenção! NÃO RECEBER ESTE BOLETO.',   
}
```
And pass as a dictionary to the create method as shown in the example below:

```python
>>> ticket.create(**params)
```

This method creates the ticket in the system and returns the ticket in PDF format with the data entered in the parameters.

# Search a ticket

The **Ticket** class has the **search()** method, this method receives as a parameter the ticket token that will allow you to access the ticket. Go to the administrative panel [app.boletocloud.com/api](https://app.boletocloud.com/api]) and in the information about the desired ticket you will find the token, pass the token as a parameter to the method and you will have the Download automatic file as PDF is shown in the code below:

```python
>>> ticket.search('token_ticket')
```

Lib also relies on aid methods that return important information that may be needed as well.

# token

The lib has a property that returns the token entered in the creation of the object, see an example in the code below:

```python
>>> ticket.token
>>> 'your_token'
```

# get_url()

If you need the API endpoint url, we have **get_url()** at your disposal, see an example below:

```python
>>> ticket.get_url()
>>> 'https://sandbox.boletocloud.com/api/v1/boletos/'
```

# Future implementations

Noting that the [boletocloud.com] API (http://www.boletocloud.com) is still on BETA, as the company updates it, we will be implementing the new features.
For more information regarding API, access: [www.boletocloud.com/app/dev/api](https://www.boletocloud.com/app/dev/api)

# Bugs and improvements

Did you find a bug or have any suggestions for implementation? Feel free to send us a [issue](https://github.com/hudsonbrendon/boleto-cloud-python/issues)