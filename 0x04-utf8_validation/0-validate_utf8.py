#!/usr/bin/python3
"""
Main module:
0x04. UTF-8 Validation
"""
from typing import List


def validUTF8(data: List) -> bool:
    """Test if data is a valid utf8 and return True or False
    For each data in the data, convert to binary and test the bits
    to make sure t
    """
    num_of_bytes = 0
    for num in data:
        binary_representation = '{0:08b}'.format(num)
        if num_of_bytes == 0:
            for bit in binary_representation:
                if bit == '0':
                    break
                num_of_bytes = num_of_bytes + 1

            if num_of_bytes == 0:
                continue

            if num_of_bytes == 1 or num_of_bytes > 4:
                return False
        else:
            if not (binary_representation[0] == '1' and
                    binary_representation[1] == '0'):
                return False
        num_of_bytes = num_of_bytes - 1

    return num_of_bytes == 0
