# -*- coding: utf-8 -*-

import unittest
from boletocloud import Boleto


class TestBoleto(unittest.TestCase):

    def setUp(self):
        self.boleto = Boleto('12345')
        self.url = 'https://sandbox.boletocloud.com/api/v1/'

    def test_token(self):
        self.assertTrue(isinstance(self.boleto, Boleto))
        self.assertEqual(self.boleto.token, '12345')

    def test_url(self):
    	self.assertEqual(self.boleto.get_url('boleto/1'), '{0}{1}'.format(self.url, 'boleto/1'))


if __name__ == '__main__':
    unittest.main()
