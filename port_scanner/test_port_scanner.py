#!/usr/bin/env python3

import unittest
import src.port_scanner as port_scanner

print("*** Tests Port Scanner ***")


class UnitTests(unittest.TestCase):

    def test_port_scanner_url(self):
        actual = port_scanner.get_open_ports(
            "www.stackoverflow.com", [79, 82], False)
        expected = [80]
        self.assertEqual(
            actual, expected, 'Expected scanning ports of URL address to return [80].')

    def test_port_scanner_url_multiple_ports(self):
        actual = port_scanner.get_open_ports(
            "scanme.nmap.org", [20, 80], False)
        expected = [22, 80]
        self.assertEqual(
            actual, expected, 'Expected scanning ports of URL address to return [22, 80].')

    def test_port_scanner_verbose_hostname_multiple_ports(self):
        actual = port_scanner.get_open_ports("scanme.nmap.org", [20, 80], True)
        expected = "Open ports for scanme.nmap.org (45.33.32.156)\nPORT     SERVICE\n22       ssh\n80       http"
        self.assertEqual(
            actual, expected, "Expected 'Open ports for scanme.nmap.org (45.33.32.156)\nPORT     SERVICE\n22       ssh\n80       http'")

    def test_port_scanner_invalid_hostname(self):
        actual = port_scanner.get_open_ports("scanme.nmap", [22, 42], False)
        expected = "Error: Invalid hostname"
        self.assertEqual(actual, expected,
                         "Expected 'Error: Invalid hostname'")

    def test_port_scanner_invalid_ip_address(self):
        actual = port_scanner.get_open_ports("266.255.9.10", [22, 42], False)
        expected = "Error: Invalid IP address"
        self.assertEqual(actual, expected,
                         "Expected 'Error: Invalid IP address'")


if __name__ == "__main__":
    unittest.main()
