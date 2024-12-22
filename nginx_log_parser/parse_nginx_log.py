#!/usr/bin/env python3
"""
NGINX log parser

This script allows you to parse a file from an NGINX or Apache using NGINX (CLF combined) format syntax.

Usage:
    
    python3 parse_nginx_log.py -f <path>

Options:

    -o  Create a csv file containing the output of the parser.
    -v  Extended verbose mode.
    -u  Apply user_agents library to obtain more info about visitors.

Help:

    python3 parse_nginx_log.py -h

Author: raiabril

"""

import re
from optparse import OptionParser

import pandas
from termcolor import colored
from user_agents import parse


def create_html_report(df):
    """ Function to generate the HTML report. """

    # Base HTML for the file
    base_html = """
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Report</title>
    </head>
    <body>
        body_content
    </body>
    </html>
    """

    # Generate content from DataFrame
    content = df.to_html(classes='table table-striped')
    content = '<h1>Content</h1>' + content
    html = base_html.replace("body_content", content)

    # Save the content to file
    with open("index.html", "w") as text_file:
        text_file.write(html)


def parse_log(filename, user_agent_check=False, output=False, verbose=False):
    """ 
        This function parses the file using a regex.
        Returns a Pandas DataFrame
    """

    # Open the file and read the lines.
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Initialize the list
    log_data = []

    # Split the lines and send to list
    for line in lines[:2]:
        log_data.append(
            list(map(''.join, re.findall(r'\"(.*?)\"|\[(.*?)\]|(\S+)', line))))

    # Create Dataframe from the list of lines
    df = pandas.DataFrame(log_data)

    # Assign column names
    df.columns = [
        "Source IP",
        "Client identity",
        "User ID",
        "Date",
        "Request",
        "HTTP Status code",
        "Body bytes sent",
        "HTTP Referer",
        "HTTP User Agent",
        "Upstream address",
        "Upstream response time"]

    # Parse the date column
    df['Date'] = pandas.to_datetime(
        df['Date'], format='%d/%b/%Y:%H:%M:%S +0000')

    return df


def main():
    """ Main function to control user interaction and launch parser. """

    # Define the parser.
    parser = OptionParser(
        usage="python3 %prog [options] filename", version="%prog 1.0")

    # Define the options
    parser.add_option('-u', '--user_agent', dest='user_agent',
                      help='Include User Agent check')
    parser.add_option('-o', '--output', dest='output',
                      help='Create a csv file in the current path with output')
    parser.add_option('-v', '--verbose', dest='verbose',
                      help='Extended details')

    # parse arguments when received
    (options, args) = parser.parse_args()

    # Check if the filename is included
    try:
        filename = args[0]

    except IndexError:
        exit(colored('[-] Please provide a valid filename', 'red'))

    # Check the options
    user_agent_check = options.user_agent
    output = options.output
    verbose = options.verbose

    # Run the port scanner
    df = parse_log(filename, user_agent_check, output, verbose)
    
    # TODO Improve CSS of the report
    create_html_report(df)

    # TODO User Agent Check
    # TODO Output
    # TODO verbose


if __name__ == '__main__':
    main()
