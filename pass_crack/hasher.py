#!/usr/bin/python3

import hashlib

from Crypto.Hash import MD4


class hasher():

    def get_md4(self, hash_value):
        hash_obj_1 = MD4.new()
        hash_obj_1.update(hash_value.encode())
        return hash_obj_1.hexdigest()

    def get_md5(self, hash_value):
        hash_obj_1 = hashlib.md5()
        hash_obj_1.update(hash_value.encode())
        return hash_obj_1.hexdigest()

    def get_sha1(self, hash_value):
        hash_obj_2 = hashlib.sha1()
        hash_obj_2.update(hash_value.encode())
        return hash_obj_2.hexdigest()

    def get_sha224(self, hash_value):
        hash_obj_3 = hashlib.sha224()
        hash_obj_3.update(self.hash_value.encode())
        return hash_obj_3.hexdigest()

    def get_sha256(self, hash_value):
        hash_obj_4 = hashlib.sha256()
        hash_obj_4.update(self.hash_value.encode())
        return hash_obj_4.hexdigest()

    def get_sha512(self, hash_value):
        hash_obj_5 = hashlib.sha512()
        hash_obj_5.update(self.hash_value.encode())
        return hash_obj_5.hexdigest()
