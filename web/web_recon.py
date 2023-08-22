#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from models import Target

target = Target(url='http://127.0.0.1:8080')

# Check if the web portal is up by using a GET request
def check_web_portal(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False


check_web_portal(target.url)


# Check which server is responding by checking the headers
def check_server_response(url):
    try:
        response = requests.get(url)
        if response.headers['Server'] == 'nginx/1.10.0':
            return True
        else:
            return False
    except:
        return False

# Print the response headers of the GET response


def print_response_headers(url):
    try:
        response = requests.get(url)
        print(response.headers)
    except:
        print('Error: Unable to print response headers')

# Get the text content from the web page using a GET request


def get_web_page_text(url):
    try:
        response = requests.get(url)
        return response.text
    except:
        return 'Error: Unable to get web page text'


# Print the response using Beautiful Soup
def print_response_soup(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.prettify())
    except:
        print('Error: Unable to print response soup')


# Print the title of the web portal
def print_web_page_title(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.title.string)
    except:
        print('Error: Unable to print web page title')


# Print the URLs for images present on the page
def print_web_page_images(url):
	try:
		response = requests.get(url)
		soup = BeautifulSoup(response.text, 'html.parser')
		for img in soup.find_all('img'):
			print(img.get('src'))
	except:
		print('Error: Unable to print web page images')


# Scrape all the URLs from the home page of the web portal
def scrape_web_page_urls(url):
	try:
		response = requests.get(url)
		soup = BeautifulSoup(response.text, 'html.parser')
		for a in soup.find_all('a'):
			print(a.get('href'))
	except:
		print('Error: Unable to scrape web page URLs')


