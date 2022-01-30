import unittest

import port_scanner


class PortScannerTest(unittest.TestCase):
    def test_port_scanner_verbose_hostname_multiple_ports(self):
        string = port_scanner.get_open_ports("scanme.nmap.org", [20, 80], True)
        actual = string
        expected = "Open ports for scanme.nmap.org (45.33.32.156)\nPORT     SERVICE\n22       ssh\n80       http"
        self.assertEqual(
            actual, expected, "Expected 'Open ports for scanme.nmap.org (45.33.32.156)\nPORT     SERVICE\n22       ssh\n80       http'")


if __name__ == "__main__":
    unittest.main()
