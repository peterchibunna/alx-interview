#!/usr/bin/python3
"""
Main module
"""


def validUTF8(data):
    """Test if data is a valid utf8 and return True or False
    """
    num_of_bytes = 0
    for num in data:
        binary_representation = f'{num:08b}'
        if num_of_bytes == 0:
            for bit in binary_representation:
                if bit == '0':
                    break
                num_of_bytes += 1

            if num_of_bytes == 0:
                continue

            if num_of_bytes == 1 or num_of_bytes > 4:
                return False
        else:
            if not (binary_representation[0] == '1' and
                    binary_representation[1] == '0'):
                return False
        num_of_bytes -= 1

    return num_of_bytes == 0
