"""
Port scanner

This tool will run a port scan in the given target and port range.

Author: Rai
"""


import socket
import common_ports
import re


def check_valid_ip(ip_address: str):
    """ Function to check if the given address is valid. """
    valid_ip = False
    error = None

    try:
        socket.inet_aton(ip_address)
        valid_ip = True

    except Exception:
        error = "Error: Invalid IP address"

    return valid_ip, error


def connection_check(target: str, port: str) -> bool:
    """ Function to test connection using socket library. """

    # Initialize the socket.
    socket.setdefaulttimeout(2)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    found = False

    try:
        sock.connect((target, port))
        found = True

    except ConnectionRefusedError:
        pass

    except socket.timeout:
        pass

    finally:
        sock.close()

    return found


def verbose_output(ip_address: str, hostname: str, open_ports: list) -> str:
    """ Function to dislay a nice open ports output."""

    # Header based on hostname
    if hostname != "":
        response = f"Open ports for {hostname} ({ip_address})"
    else:
        response = f"Open ports for {ip_address}"

    # Table header
    response += f"\nPORT     SERVICE"

    # Create a line for each port with the know services.
    # Specify the length of the port string to 5 (max 65535)

    for port in open_ports:
        try:
            response += f"\n{port:<5}    {common_ports.ports_and_services[port]}"
        except KeyError:
            response += f"\n{port:<5}"

    return response


def get_hostname_and_address(target: str):
    """ Function to retrieve the hostname and address of a given target. """

    regex = r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}"

    # Initialize the hostname and address
    ip_address = ""
    hostname = ""
    error = None

    # Check the target is IP or hostname
    if re.search(regex, target):

        # Use the validator for IP of socket
        valid_ip, error = check_valid_ip(target)

        if valid_ip:
            ip_address = target

            # Try to retrieve the hostname for the IP provided
            try:
                hostname = socket.gethostbyaddr(ip_address)[0]
            except socket.herror:
                pass

    else:
        try:
            ip_address = socket.gethostbyname(target)
            hostname = target

        except socket.gaierror:
            error = "Error: Invalid hostname"

    return ip_address, hostname, error


def get_open_ports(target: str, port_range: list, verbose=False):
    """ 
        Function to retrieve the list of open ports for a given target and list of ports. 
        Returns a list of open ports or string if verbose is True.
    """

    # Initialize open ports as empty list
    open_ports = []

    # Get hostname and address from target
    ip_address, hostname, error = get_hostname_and_address(target)

    if error:
        return error

    # Run the port scanner for port range
    for port in range(port_range[0], port_range[1]+1):

        # If successful append to open port list
        if connection_check(ip_address, port):
            open_ports.append(port)

    # Verbose to show the nice output
    if verbose:
        return verbose_output(ip_address, hostname, open_ports)
    else:
        return(open_ports)
