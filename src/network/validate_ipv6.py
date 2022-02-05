#!/usr/bin/env python3

import ipaddress

import ipaddress

address = input('Please enter an IP address: ')

try:
    addr = ipaddress.IPv6Address(address)
except ipaddress.AddressValueError:
    print(address, 'is not a valid IPv6 address')
else:
    if addr.is_multicast:
        print(address, 'is an IPv6 multicast address')
    if addr.is_private:
        print(address, 'is an IPv6 private address')
    if addr.is_global:
        print(address, 'is an IPv6 global address')
    if addr.is_link_local:
        print(address, 'is an IPv6 link-local address')
    if addr.is_site_local:
        print(address, 'is an IPv6 site-local address')
    if addr.is_reserved:
        print(address, 'is an IPv6 reserved address')
    if addr.is_loopback:
        print(address, 'is an IPv6 loopback address')
    if addr.ipv4_mapped:
        print(address, 'is an IPv6 mapped IPv4 address')
    if addr.sixtofour:
        print(address, 'is an IPv6 RFC 3056 address')
    if addr.teredo:
        print(address, 'is an IPv6 RFC 4380 address')