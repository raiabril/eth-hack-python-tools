import gzip

from termcolor import colored

from hasher import hasher


def try_open(wordlist):
    try:
        if wordlist[-3:] == '.gz':
            pass_file = gzip.open(wordlist, 'rb')
        else:
            pass_file = open(wordlist, 'r')
        lines = pass_file.readlines()
        lines = [line.decode("utf-8", errors='ignore').strip('\n')
                 for line in lines]
        pass_file.close()
        return lines

    except Exception as e:
        print(e)


hash_value = input("[*] Enter the hash: ").lower()
hash_type = input("[*] Select hash type (md5, sha1, sha224, sha256, sha512): ")
wordlist = input("[*] Enter Path to the password file: ")
lines = try_open(wordlist)
my_hasher = hasher()

for password in lines:
    print(colored(f"[i] Testing with {password}", 'yellow'))

    if hash_type == 'md4':
        calculated_hash = my_hasher.get_md4(password)
    elif hash_type == 'md5':
        calculated_hash = my_hasher.get_md5(password)
    elif hash_type == 'sha1':
        calculated_hash = my_hasher.get_sha1(password)
    elif hash_type == 'sha224':
        calculated_hash = my_hasher.get_sha224(password)
    elif hash_type == 'sha256':
        calculated_hash = my_hasher.get_sha256(password)
    elif hash_type == 'sha512':
        calculated_hash = my_hasher.get_sha512(password)
    else:
        print("[!!] Please return a valid hash type!")
        exit()

    if calculated_hash == hash_value:
        print(colored(f"[+] Password found: {password}", "green"))
        exit()

print(colored("[-] Password not found", "red"))
