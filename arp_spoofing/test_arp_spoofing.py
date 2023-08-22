#!/usr/bin/env python3
"""
test_arp_spoofing.py - Test ARP Spoofing module

"""

import unittest
from src import arp_spoofing as arp_spoofing


class UnitTests(unittest.TestCase):
    def test_if_mac_is_valid(self):
        """ Check if a MAC address is valid. """
        actual = arp_spoofing.request_mac_address('192.168.1.134')
        expected = '20:f4:78:6e:ae:40'
        self.assertEqual(
            actual, expected,
            'Expected function to return 20:f4:78:6e:ae:40 from 192.168.1.134".'
        )

if __name__ == "__main__":
    unittest.main()
