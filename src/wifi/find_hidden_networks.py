#!/usr/bin/env python3
"""
find_hidden_networks.py

Find hidden networks in the area with the SSID hidden.

Usage: sudo python3 find_hidden_networks.py

"""
import subprocess

from scapy import all as scapy

iface = "wlan0"

# Check if the packet is a probe request, response or association request.
def check_probe_request(packet):
    if packet.haslayer(scapy.Dot11ProbeReq) or packet.haslayer(scapy.Dot11AssoReq) or packet.haslayer(scapy.Dot11ProbeResp):
        return True
    else:
        return False

# Set the interface to monitor mode.
def set_monitor_mode(iface):
    subprocess.call(['ifconfig', iface, 'down'])
    subprocess.call(['ifconfig', iface, 'mode', 'monitor'])
    subprocess.call(['ifconfig', iface, 'up'])

# Sniff the packets.
def sniff_packets(iface):
    """ Sniff the packets using the given interface and return the list of hidden networks. """
    set_monitor_mode(iface)
    scapy.sniff(iface=iface, prn=check_probe_request, store=0)
