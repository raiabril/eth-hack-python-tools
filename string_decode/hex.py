#! /usr/bin/python3

string = input("Input the hex string: ").split(' ')

print(bytes.fromhex(''.join(string)).decode('utf-8'))