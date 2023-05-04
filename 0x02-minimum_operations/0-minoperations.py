#!/usr/bin/python3
"""
0. Minimum Operations
mandatory
In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n,
write a method that calculates the fewest number of operations needed to
result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
"""


def minOperations(n) -> int:
    num_operations = 0
    copied_text = ''
    content = 'H'
    if isinstance(n, int):
        while len(content) < n:  # always evaluate content length in real time
            if len(copied_text) == 0:
                # there's nothing copied yet!
                copied_text = content  # copy all
                content += copied_text  # paste
                num_operations += 2
            elif n - len(content) > 0 \
                    and (n - len(content)) % len(content) == 0:
                # test to see if we can copy everything without overflow
                copied_text = content  # copy all
                content += copied_text  # and paste
                num_operations += 2
            elif len(copied_text) > 0:
                content += copied_text  # paste
                num_operations += 1
        return num_operations
    else:
        return 0
