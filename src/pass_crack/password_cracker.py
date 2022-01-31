#!/usr/bin/env python3

"""
Password cracker SHA1

Author: Rai (grx6@naosinfosec.com)

"""
import hashlib

def calculate_hash(word) -> str:
  """ Function to calculate the sha1 hash of a given word. """
  return hashlib.sha1(bytes(word,'utf8')).hexdigest()

def calculate_salted_hash(word, salt_list) -> list:
  """ 
  Function to calculate the list of hashes given word and a list of hashes.
  The hashes can be prepend OR append.
  """

  # Format to bytes the password
  word_bytes = bytes(word, 'utf-8')

  # Create the append list word + salt
  append_list = [hashlib.sha1(word_bytes + bytes(salt,'utf-8')).hexdigest() for salt in salt_list]

  # Create the prepend list: salt + word
  prepend_list = [hashlib.sha1(bytes(salt,'utf-8') + word_bytes).hexdigest() for salt in salt_list]

  # Return the concat of both lists
  return prepend_list + append_list


def crack_sha1_hash(hash, use_salts=False):
  """ 
  Function to obtain the password from a hash.

  Will return:
  - String with password.
  - PASSWORD NOT IN DATABASE if the password is not found.

  """

  # Open the passwords file a single time
  with open("wordlists/top-10000-passwords.txt", 'r') as pass_file:
    passwords = pass_file.readlines()
    passwords = [password.strip('\n') for password in passwords]

  # Let's check for no salts
  if not use_salts:

    # Run a guess for each password in file and compare
    for password in passwords:
      hass_guess = calculate_hash(password)

      # If successful return the password found
      if hash == hass_guess:
        return password

  # For salted types
  else:

    # Open salt file a single time
    with open('wordlists/known-salts.txt', 'r') as salt_file:
      salt_list = salt_file.readlines()
      salt_list = [salt.strip('\n') for salt in salt_list]

    # For each password generate a 2n list with known salted.
    for password in passwords:
      hash_list = calculate_salted_hash(password, salt_list)

      # If found in the list return the password
      if hash in hash_list:
        return password

  # In case nothing is found
  return "PASSWORD NOT IN DATABASE"