#!/usr/bin/env python3
"""
token_manipulation.py - Set of functions to manipulate JWT tokens.

Author: @raiabril
"""

import jwt


########## "Fix" pyjwt
# pyjwt's HMACAlgorithm doesn't allow using public keys as secrets, so
# we override it here, removing the check
def prepare_key(self, key):
    key = jwt.utils.force_bytes(key)
    return key


jwt.algorithms.HMACAlgorithm.prepare_key = prepare_key


def get_token_header(token):
    """
    Get the header of a JWT token.

    :param token: JWT token.
    :return: Header of the token.
    """
    return jwt.get_unverified_header(token)


def get_token_payload(token, public_key=None, algorithm=['HS256']):
    """
    Get the payload of a JWT token.

    :param token: JWT token.
    :return: Payload of the token.
    """
    return jwt.decode(token, public_key, algorithms=algorithm)


def create_token(payload, secret, algorithm=['HS256']):
    """
    Create a JWT token.

    :param payload: Payload of the token.
    :param secret: Secret to sign the token.
    :param algorithm: Algorithm to sign the token.
    :return: JWT token.
    """
    return jwt.encode(payload, secret, algorithm=algorithm)
