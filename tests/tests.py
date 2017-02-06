# -*- coding: utf-8 -*-

import unittest
from boletocloud import Boleto


class TestBoleto(unittest.TestCase):

    def setUp(self):
        self.boleto = Boleto('api-key_v0gj_lQvs0tuXgjaMHT-ebSOVsE95a3T5xbBzIIRFYE=')
        self.url = 'https://sandbox.boletocloud.com/api/v1/boletos/'

    def test_token(self):
        self.assertTrue(isinstance(self.boleto, Boleto))
        self.assertEqual(self.boleto.token, 'api-key_v0gj_lQvs0tuXgjaMHT-ebSOVsE95a3T5xbBzIIRFYE=')

    def test_url(self):
    	self.assertEqual(self.boleto.get_url('vBwIcWOwGg8rteR_-n84t3PA4HCRk45IGtzRE9ulw7c='), '{0}{1}'.format(self.url, 'vBwIcWOwGg8rteR_-n84t3PA4HCRk45IGtzRE9ulw7c='))

    def test_authenticate(self):
        self.assertTrue(self.boleto.authenticate('vBwIcWOwGg8rteR_-n84t3PA4HCRk45IGtzRE9ulw7c=').status_code, 200)
        self.assertTrue(self.boleto.authenticate('vBwIcWOwGg8rteR_-n84t3PA4HCRk45IGtzRE9ulw7c=').headers['Content-Type'], 'application/pdf; charset=UTF-8')


if __name__ == '__main__':
    unittest.main()
