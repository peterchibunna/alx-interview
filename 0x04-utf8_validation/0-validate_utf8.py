#!/usr/bin/python3
"""
Module: 
"""


def validUTF8(data):
    """Return: True if data is a valid UTF-8 encoding, else return False.
    """
    num_bytes = 0
    for num in data:
        binary_representation = format(num, '#010b')[-8:]
        if num_bytes == 0:
            for bit in binary_representation:
                if bit == '0':
                    break
                num_bytes += 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (binary_representation[0] == '1'
                    and binary_representation[1] == '0'):
                return False

        num_bytes -= 1

    return num_bytes == 0
