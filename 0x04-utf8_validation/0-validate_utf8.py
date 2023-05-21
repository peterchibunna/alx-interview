#!/usr/bin/python3
"""
Module: 0x04. UTF-8 Validation
"""


def bin8(x):
    """Get 'x' expressed in binary with 8-width padding
    @source https://stackoverflow.com/a/10411628/849417
    """
    return ''.join(reversed([str((x >> i) & 1) for i in range(8)]))


def validUTF8(data):
    """
    Return: True if data is a valid UTF-8 encoding, else return False.
    """
    can_decode = True
    for val in data:
        try:
            val.to_bytes(8, 'big').decode('utf8')
        except (UnicodeDecodeError, Exception):
            can_decode = False
    return can_decode
