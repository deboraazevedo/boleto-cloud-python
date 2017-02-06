# -*- coding: utf-8 -*-

import unittest
from boletocloud import Ticket
from requests.auth import HTTPBasicAuth


class TestTicket(unittest.TestCase):

    def setUp(self):
        self.ticket = Ticket('api-key_v0gj_lQvs0tuXgjaMHT-ebSOVsE95a3T5xbBzIIRFYE=')
        self.url = 'https://sandbox.boletocloud.com/api/v1/boletos/'

    def test_token(self):
        self.assertTrue(isinstance(self.ticket, Ticket))
        self.assertEqual(self.ticket.token, 'api-key_v0gj_lQvs0tuXgjaMHT-ebSOVsE95a3T5xbBzIIRFYE=')

    def test_url(self):
    	self.assertEqual(self.ticket.get_url('vBwIcWOwGg8rteR_-n84t3PA4HCRk45IGtzRE9ulw7c='), '{0}{1}'.format(self.url, 'vBwIcWOwGg8rteR_-n84t3PA4HCRk45IGtzRE9ulw7c='))

    def test_authenticate(self):
        self.assertTrue(isinstance(self.ticket.authenticate, HTTPBasicAuth))
 
if __name__ == '__main__':
    unittest.main()
