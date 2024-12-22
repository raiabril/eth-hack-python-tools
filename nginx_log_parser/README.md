# parse-nginx-logs

This is a simple python script to parse nginx logs and produce a report.

## Usage

It is required to include a valid path to the nginx logs file.

    python3 parse_nginx_log.py <filename> [options]

## Options

The available options are as follows:

    Options:
    --version                               show program's version number and exit
    -h, --help                              show this help message and exit
    -u USER_AGENT, --user_agent=USER_AGENT  include User Agent check
    -o OUTPUT, --output=OUTPUT              create a csv file in the current path with output
    -v VERBOSE, --verbose=VERBOSE           extended details

## TBD

1. CSV report creation.
2. Improved HTML report stats.
3. Improved HTML CSS and style.
4. Support for User agent library.