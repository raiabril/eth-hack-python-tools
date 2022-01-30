#!/usr/bin/env python3

key = 'encryptXOR'
cod = 'HQERKhYCLDc9KgQX'

code = cod.encode('utf-8').hex()
key = key.encode('utf-8').hex()

result = hex(int(code, 16) ^ int(key, 16)).split('x')[1]

print(bytes.fromhex(result).decode('utf-8'))